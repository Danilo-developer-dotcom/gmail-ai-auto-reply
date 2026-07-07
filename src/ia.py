import time

from google import genai
import os

class Gemini:
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

    def __init__(self):
        """Estabelece a conexão com o Gemini Client e prepara os arquivos que serão utilizados na classe"""

        self.client = genai.Client(
            api_key=Gemini.GEMINI_API_KEY,
        )

        with open('data/rules.txt', 'r', encoding='utf-8') as arquivo:
            self.regra = arquivo.read()

        with open('data/politicas.txt', 'r', encoding='utf-8') as arquivo:
            self.politicas = arquivo.read()

    def gerar_resposta(self, assunto, conversa) -> str:
        """Gera a resposta baseada nas instruções + politicas + contexto"""

        formato = (f"Assunto recebido: {assunto}\n"
                   f"Conversa: {conversa}\n"
                   f"Com base em tudo isso, gere sua resposta para o ultimo e-mail")

        tentativas = 3
        while tentativas > 0:
            try:
                resposta = self.client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents= self.regra + self.politicas + formato
                )
                return resposta.text

            except Exception as e:
                print("Falha ao tentar gerar mensagem")
                tentativas -= 1

                if tentativas == 0:
                    print(f"Não foi possível acessar a Gemini API: {e}")
                    return ''

                print(f"Tentando novamente... {tentativas} tentativa(s) restante(s)")
                print(f"Aguarde 5 segundos ")
                time.sleep(5)
                continue
