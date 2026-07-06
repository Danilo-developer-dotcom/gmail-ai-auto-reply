from colorama import Fore, Back, Style, init

# Descomente a linha a seguir se estiver usando Windows:
init(autoreset=True)

DIVISOR = "-" * 35 + "\n"


def menu():
    """Menu Principal de escolhas para controle das respostas"""

    print("\n", DIVISOR)
    print("O que deseja fazer agora?\n")
    print("1 - Enviar resposta")
    print("2 - Copiar resposta")
    print("3 - Gerar nova resposta")
    print("4 - Responder manualmente")
    print("5 - Próximo e-mail")
    print("0 - Sair")

    resposta = valida_int(0, 5, ">> ")
    if resposta is not None:
        return resposta
    else:
        resposta = menu()
    return resposta


def extrair_remetente(remetente: str) -> str:
    """Garante que o remetente será apresentado apenas pelo email"""

    if '<' in remetente and '>' in remetente:
        remetente = remetente.split('<')[1].replace('>', '').strip()
    return remetente


def valida_int(min: int, max: int, mensagem: str) -> int | None:
    """validação de valor inteiro dentro de um intervalo"""

    try:
        valor = int(input(mensagem))
        if min <= valor <= max:
            return valor

        else:
            print(Back.BLUE + "Valor inválido")
            return None

    except ValueError:
        print(Back.BLUE + "Formato inválido, por favor digite um número.")
        return None


def menu_resposta_manual(resposta_manual) -> int:
    """Menu para a confirmação de envio da resposta manual"""

    print(DIVISOR)
    print(f"Sua resposta:\n{Fore.GREEN}{resposta_manual}")
    print("Deseja enviar sua resposta?")
    print("1 - Sim")
    print("2 - Não")
    resposta = valida_int(1, 2, ">> ")
    return resposta


def historico_formatado(historico: dict):
    """Formata o histórico de mensagens de dicionário para uma string legivel para o Gemini"""

    texto_formatado = ""

    for mensagem in historico:
        texto_formatado += f"Remetente: {extrair_remetente(mensagem['remetente'])}\n"
        texto_formatado += f"Mensagem:\n{mensagem['mensagem']}\n"
        texto_formatado += DIVISOR

    return texto_formatado


def exibicao(historico: dict) -> None:
    """Exibe as mensagens do remetente original em vermelho, enquanto as do destinatário em verde
    para a melhor compreensão"""

    print(Back.RED + f"Assunto: {historico[0]['assunto']}\n")

    for email in historico:

        if email["remetente"] == historico[0]["remetente"]:
            cor_fundo = Back.RED
            cor_fonte = Fore.RED

        else:
            cor_fundo = Back.GREEN
            cor_fonte = Fore.GREEN

        print(cor_fundo + f"Remetente: {extrair_remetente(email['remetente'])}")
        print(cor_fundo + f"Mensagem:{Style.RESET_ALL}\n\n{cor_fonte}{email['mensagem']}")
        print(DIVISOR)

    return None
