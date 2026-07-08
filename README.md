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

## Tecnologias utilizadas

- Python
- Gmail API
- Google OAuth 2.0 (Gmail API)
- Google Gemini API
- Google API Client
- Prompt Toolkit
- Colorama
- Python Dotenv

---

## Funcionalidades

- Leitura de conversas não lidas utilizando a Gmail API
- Recuperação do histórico completo de cada thread
- Geração de respostas contextuais com Google Gemini
- Regras e políticas da IA configuráveis por arquivos externos
- Envio da resposta preservando a thread original da conversa
- Regeneração de respostas com IA
- Resposta manual pelo operador
- Cópia da resposta para a área de transferência
- Marcação automática das conversas como lidas
- Tratamento de falhas temporárias nas APIs com retentativas automáticas

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
5. Colocar o arquivo dentro da pasta `data/` do projeto.

Na primeira execução será aberta uma janela do navegador para autenticação.

Após conceder as permissões, o arquivo `token.json` será criado em `data/` automaticamente e reutilizado nas próximas execuções.

> **Observação**
>
> Os arquivos `credentials.json`, `token.json` e `.env` não fazem parte do repositório por conterem informações sensíveis.
> Você deverá criar/configurar esses arquivos antes da primeira execução.

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

## Conceitos praticados

Este projeto foi utilizado para estudar:

- Programação Orientada a Objetos
- Integração com APIs REST
- Integração com OAuth 2.0 para autenticação na Gmail API
- Google Gemini API
- Engenharia de Prompts
- Manipulação de MIME
- Automação de processos
- Estruturação de projetos Python

---

## Licença

Este projeto foi desenvolvido para fins de estudo e demonstração de integração entre Gmail API e Google Gemini.

Sinta-se à vontade para utilizá-lo como referência, respeitando os termos das APIs utilizadas.
