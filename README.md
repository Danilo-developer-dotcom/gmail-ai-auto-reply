# gmail-ai-auto-reply

Sistema desenvolvido em Python para leitura, análise e resposta semiautomática de e-mails do Gmail utilizando a API do Gmail e a API Gemini.

O projeto foi desenvolvido para estudos sobre integração de APIs, OAuth 2.0, engenharia de prompts e automação de atendimento.

---

## Como funciona

1. O sistema autentica o usuário utilizando OAuth 2.0.
2. Busca todas as conversas que possuem mensagens não lidas.
3. Recupera todo o histórico de cada conversa.
4. Formata o histórico em texto.
5. Envia a conversa completa para o Gemini.
6. O Gemini gera uma resposta considerando todo o contexto.
7. O operador decide se:
   - envia;
   - copia;
   - gera outra resposta;
   - escreve manualmente;
   - ignora a conversa.

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
git clone https://github.com/seu-usuario/nome-do-repositorio.git
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
GEMINI_API_KEY="sua chave aqui"
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

Após o login será criado automaticamente o arquivo `token.json`.

Esse arquivo armazena o token de acesso e não deve ser enviado ao GitHub.

---

## Arquivos de configuração da IA

O projeto utiliza dois arquivos independentes:

### rules.txt

Responsável pelo comportamento da IA.

Exemplo:

- tom de escrita;
- formalidade;
- estilo de resposta.

### politicas.txt

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
- depende da revisão humana antes do envio.

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
