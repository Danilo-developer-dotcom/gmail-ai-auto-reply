import os
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from email.message import EmailMessage
from src.utils import extrair_remetente
import base64


class Gmail:
    SCOPES = ["https://www.googleapis.com/auth/gmail.modify"]

    def __init__(self):
        creds = None

        # O arquivo token.json armazena o acesso do usuário e atualiza tokens, e é criado automaticamente quando o
        # fluxo de autorização completa pela primeira vez

        if os.path.exists("token.json"):
            creds = Credentials.from_authorized_user_file("token.json", Gmail.SCOPES)

        # Se não houver uma credencial (ou não houver valida) disponivel, faça o login do usuário.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    "credentials.json", Gmail.SCOPES
                )
                creds = flow.run_local_server(port=0)

            # Salva as credenciais para a próxima execução
            with open("token.json", "w") as token:
                token.write(creds.to_json())

        # Chama a Gmail API
        self.service = build("gmail", "v1", credentials=creds)

    def _extrair_texto(self, conteudo):
        """Percorre as partes do email de forma recursiva para encontrar o texto do corpo"""

        if conteudo.get("mimeType") == "text/plain":
            data = conteudo.get("body", {}).get("data")

            if data:
                return base64.urlsafe_b64decode(data).decode("utf-8")

        for subpart in conteudo.get("parts", []):
            texto = self._extrair_texto(subpart)

            if texto:
                return texto

        return ""

    def _ler_email(self, msg, thread_id):
        """Faz a leitura dos componentes do e-mail a serem utilizados"""
        payload = msg["payload"]
        headers = payload.get("headers", [])
        mensagem = self._extrair_texto(payload)

        email = {
            "id": msg["id"],
            "threadId": thread_id,
            "messageId": "",
            "remetente": "",
            "assunto": "",
            "mensagem": mensagem
        }

        for header in headers:

            match header["name"]:

                case "From":
                    email["remetente"] = header["value"]
                case "Subject":
                    email["assunto"] = header["value"]
                case "Message-ID":
                    email["messageId"] = header["value"]

        return email

    def read(self) -> list:
        """Solicita e armazena uma lista de dicionários com o histórico de conversas"""

        conversas = []

        # Busca apenas mensagens não lidas
        resultado = self.service.users().messages().list(
            userId="me",
            q="is:unread"
        ).execute()

        mensagens = resultado.get("messages", [])  # retorna uma lista com todas as mensagens não lidas

        # descobre quais Threads possuem, mensagens não lidas:
        thread_ids = {msg["threadId"] for msg in mensagens}  # não quero mensagens, apenas conversas

        # Percorrendo CONVERSAS
        for thread_id in thread_ids:

            # Aqui é a requisição de TODAS as mensagens de uma CONVERSA através do Id da CONVERSA
            thread = self.service.users().threads().get(
                userId="me",
                id=thread_id,
                format="full"
            ).execute()

            historico = []

            # Percorre cada mensagem de uma conversa
            for msg in thread["messages"]:
                historico.append(
                    self._ler_email(msg, thread["id"])  # traduz a mensagem para um objeto
                )

            ultima = historico[-1]

            # Armazena o conjunto de conversas, cada uma com seu conjunto de mensagens
            conversas.append({
                "threadId": thread["id"],
                "remetente": ultima["remetente"],
                "assunto": historico[0]["assunto"],
                "messageId": ultima["messageId"],
                "historico": historico
            })

        return conversas

    def reply(self, conversa: dict, resposta: str) -> None:

        """Realiza o envio do e-mail de resposta para o cliente ainda dentro da mesma conversa"""

        # cria um objeto que representa um e-mail:
        mensagem = EmailMessage()

        # destinatário:
        mensagem["To"] = extrair_remetente(conversa["remetente"])

        # assunto
        assunto = conversa["assunto"]
        if not assunto.lower().startswith('re:'):
            assunto = f"Re: {assunto}"

        mensagem["Subject"] = assunto

        # cabeçalhos responsáveis pelo reply
        mensagem["In-Reply-To"] = conversa["messageId"]
        mensagem["References"] = conversa["messageId"]

        # corpo do email:
        mensagem.set_content(resposta)

        # converte todos os e-mails para bytes
        raw = base64.urlsafe_b64encode(
            mensagem.as_bytes()
        ).decode()

        # envia mantendo a mesma conversa
        self.service.users().messages().send(
            userId="me",
            body={
                "raw": raw,
                "threadId": conversa["threadId"]
            }
        ).execute()

        self.mark_thread_as_read(conversa)

        return None

    def mark_thread_as_read(self, conversa: dict) -> None:
        """Altera o Label de toda a conversa para Lida"""
        self.service.users().threads().modify(
            userId="me",
            id=conversa["threadId"],
            body={"removeLabelIds": ["UNREAD"]}
        ).execute()
        return None
