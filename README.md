<h1 align="center">
gmail-ai-auto-reply
</h1>

[![Python](https://img.shields.io/badge/Python-3.13-blue)](https://www.python.org/)
[![Gemini](https://img.shields.io/badge/Google-Gemini-orange)](https://ai.google.dev/)
[![Gmail API](https://img.shields.io/badge/API-Gmail-red)](https://developers.google.com/gmail/api)
[![OAuth](https://img.shields.io/badge/Auth-OAuth_2.0-green)](https://oauth.net/2/)
[![Status](https://img.shields.io/badge/Status-Active-success)](https://github.com/Danilo-developer-dotcom/gmail-ai-auto-reply)
[![Project](https://img.shields.io/badge/Type-Study_Project-lightgrey)](https://github.com/Danilo-developer-dotcom/gmail-ai-auto-reply)


Automatize a análise e a sugestão de respostas para e-mails do Gmail utilizando a API do Gemini, mantendo o controle humano antes do envio.

Este projeto foi desenvolvido em Python para estudar integração com APIs, autenticação OAuth 2.0, engenharia de prompts e automação de processos. Ele utiliza a Gmail API para recuperar conversas e a API Gemini para gerar sugestões de resposta contextualizadas.


---

## Como funciona

1. O sistema autentica o usuário utilizando OAuth 2.0.
2. Busca todas as conversas que possuem mensagens não lidas.
3. Recupera todo o histórico de cada conversa.
4. Formata o histórico em texto.
5. Envia a conversa completa para o Gemini.
6. O Gemini gera uma resposta considerando todo o contexto.
7. O operador decide se:
   - envia a resposta gerada pela IA;
   - copia a resposta gerada;
   - gera uma nova resposta;
   - escreve e envia uma resposta manualmente;
   - pula a conversa.
8. Após o envio da resposta ou a decisão de pular a conversa, ela é marcada como lida para evitar novo processamento.

---

## Tecnologias utilizadas

- Python
- Gmail API
- Google OAuth 2.0
- Google Gemini API
- Google API Client
- Prompt Toolkit
- Colorama
- Python Dotenv

---

## Configuração

### 1. Clone o projeto

```bash
git clone https://github.com/Danilo-developer-dotcom/gmail-ai-auto-reply.git
```

---

### 2. Crie um ambiente virtual

Windows

```bash
python -m venv .venv
```

Ative:

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

---

### 4. Configure a API Gemini

Crie um arquivo `.env`:

```
GEMINI_API_KEY=sua_api_key_aqui
```

---

### 5. Configure a Gmail API

Este projeto utiliza OAuth 2.0.

É necessário possuir um projeto no Google Cloud.

Passos:

1. Criar um projeto no Google Cloud Console.
2. Ativar a Gmail API.
3. Criar credenciais OAuth para Desktop.
4. Baixar o arquivo `credentials.json`.
5. Colocar o arquivo na raiz do projeto.

Na primeira execução será aberta uma janela do navegador para autenticação.

Após conceder as permissões, o arquivo `token.json` será criado automaticamente e reutilizado nas próximas execuções.

---

## Execução

Após concluir todas as configurações, execute o projeto com:

```bash
python main.py
```

O sistema buscará automaticamente conversas com mensagens não lidas, gerará uma sugestão de resposta utilizando o Gemini e permitirá ao operador enviá-la, regenerá-la, escrever uma resposta manualmente ou pular a conversa.

---

## Arquivos de configuração da IA

O projeto utiliza dois arquivos independentes:

### `rules.txt`

Responsável pelo comportamento da IA.

Exemplo:

- tom de escrita;
- formalidade;
- estilo de resposta.

### `politicas.txt`

Responsável pelas regras de negócio da empresa.

Exemplo:

- prazos;
- garantia;
- devoluções;
- políticas de atendimento.

Essa separação permite alterar as políticas sem modificar o código.

---

## Limitações

Este projeto foi desenvolvido para fins de estudo.

Atualmente:

- suporta apenas mensagens em texto simples (`text/plain`);
- utiliza Gmail como provedor de e-mail;
- não realiza consultas em sistemas externos (ERP, CRM, Shopify etc.);
- não realiza o envio automático de respostas; todas as mensagens dependem de confirmação do operador.

---

## Objetivos de aprendizado

Este projeto foi utilizado para estudar:

- Programação Orientada a Objetos
- Integração com APIs REST
- OAuth 2.0
- Gmail API
- Google Gemini API
- Engenharia de Prompts
- Manipulação de MIME
- Automação de processos
- Estruturação de projetos Python

---

## Licença

Projeto desenvolvido exclusivamente para fins de estudo.
