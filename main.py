from src.gmail_con import Gmail
from dotenv import load_dotenv
from src.ia import Gemini
from src.utils import menu, menu_resposta_manual, historico_formatado, exibicao, DIVISOR
from prompt_toolkit import prompt
from colorama import init, Fore, Back, Style
import pyperclip
import sys

load_dotenv()

# Descomente a linha a seguir se estiver usando Windows:
init(autoreset=True)

operador = Gmail()
agente = Gemini()

conversas = operador.read()

# acessa individualmente cada conversa

for conversa in reversed(conversas):

    assunto = conversa['assunto']
    historico = conversa['historico']
    hist_f = historico_formatado(historico)

    resposta_ia = agente.gerar_resposta(assunto, hist_f)

    exibicao(historico)
    print(Back.BLUE + f"Resposta gerada por IA:{Style.RESET_ALL}\n")
    print(Fore.GREEN + resposta_ia)

    while True:
        escolha = menu()

        match escolha:
            case 0:  # Sair
                print("Encerrando o programa.")
                sys.exit(0)

            case 1:  # Enviar Resposta
                operador.reply(conversa, resposta_ia)
                print(Back.BLUE + "Resposta enviada.")
                break

            case 2:  # Copiar resposta
                pyperclip.copy(resposta_ia)
                print(Back.BLUE + "texto copiado com suceso!")
                print(DIVISOR)
                continue

            case 3:  # Gerar nova resposta
                resposta_ia = agente.gerar_resposta(assunto, hist_f)
                print(Back.BLUE + "Nova mensagem gerada!")
                print(DIVISOR)
                print(Back.BLUE + f"Resposta gerada por IA:{Style.RESET_ALL}\n")
                print(DIVISOR)
                continue

            case 4:  # Responder manualmente
                print("Digite sua resposta:")
                print("(Para finalizar pressione (Esc ou Alt)+Enter)")
                resposta_manual = prompt(">> ", multiline=True)

                escolha_resposta_manual = None
                while escolha_resposta_manual is None:
                    escolha_resposta_manual = menu_resposta_manual(resposta_manual)

                match escolha_resposta_manual:

                    case 1:
                        operador.reply(conversa, resposta_manual)
                        print(Back.BLUE + "Resposta enviada.")
                        break

                    case 2:
                        continue

            case 5:  # Próximo e-mail
                break

        print(DIVISOR)
