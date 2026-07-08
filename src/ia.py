import time
from google import genai
from google.genai import errors
import os


class Gemini:
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

    def __init__(self):
        """Estabelece a conexão com o Gemini Client e prepara os arquivos que serão utilizados na classe"""

        self.client = genai.Client(
            api_key=Gemini.GEMINI_API_KEY,
        )

        with open('data/rules.txt', 'r', encoding='utf-8') as arquivo:
            self.rules = arquivo.read()

        with open('data/politicas.txt', 'r', encoding='utf-8') as arquivo:
            self.politicas = arquivo.read()

    def gerar_resposta(self, assunto, conversa, tentativas=3) -> str:
        """Gera a resposta baseada nas instruções + politicas + contexto"""

        formato = (f"Assunto recebido: {assunto}\n"
                   f"Conversa: {conversa}\n"
                   f"Com base em tudo isso, gere sua resposta para o ultimo e-mail")

        for tentativa in range(tentativas):
            try:
                resposta = self.client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=self.rules + self.politicas + formato
                )
                return resposta.text

            # Erros temporários de requisição da Gemini API
            except errors.APIError as e:
                status = e.code

                if status in [429, 500, 502, 503, 504]:
                    print(f"Erro temporário Gemini API ({status})\n"
                          f"Tentativa {tentativa + 1}/{tentativas}")
                    time.sleep(2 ** (tentativa + 1))  # aumento progressivo no tempo de espera
                    continue

                print(f"Erro Gemini API ({status}): {e}\n")
                return ""
