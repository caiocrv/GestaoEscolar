# 🎓 UniGestão – Sistema Acadêmico Integrado

O **UniGestão** é um sistema acadêmico desenvolvido para facilitar o gerenciamento de **alunos, professores, turmas, atividades e notas** em instituições de ensino.  
O projeto integra recursos de **autenticação segura, visualização de dados, upload de arquivos e atendimento virtual assistido por IA**.

---

## Funcionalidades Principais

| Funcionalidade | Descrição |
|---------------|-----------|
| 🎫 Cadastro e Login | Sistema de autenticação com JWT (JSON Web Token) |
| 👨‍🏫 Turmas e Disciplinas | Organização de disciplinas e acesso individual de alunos |
| 📄 Envio de Atividades | Upload de arquivos para atividades e trabalhos |
| 📝 Lançamento e Consulta de Notas | Alunos podem visualizar notas de maneira organizada |
| 🤖 Chatbot | Assistente virtual para tirar dúvidas sobre o sistema (integração com **Gemini IA**) |
| 🔐 Níveis de Acesso | Perfis com diferentes permissões (Admin, Professor, Aluno) |


## 🛠️ Tecnologias Utilizadas

### **Backend**
- Python + Flask
- JWT para autenticação
- MySQL (ou MariaDB)
- google-generativeai (Gemini API)

### **Frontend**
- HTML, CSS, JavaScript
- Fetch API para consumo da API backend


### **Criar e ativar ambiente virtual**

```bash
python -m venv venv
venv\Scripts\activate
```

### **Instalar dependências**

```bash
pip install -r requirements.txt
```


### **Configurar as variáveis de ambiente**

Para manter suas credenciais seguras, **não edite diretamente o código**.
Em vez disso, crie um arquivo chamado **`.env`** na raiz do projeto e defina nele:

```
MYSQL_HOST=localhost
MYSQL_USER=seu_usuario
MYSQL_PASSWORD=sua_senha
MYSQL_DB=nome_do_banco
MYSQL_PORT=3306

SECRET_KEY=SUA_CHAVE_SECRETA_JWT
JWT_EXPIRATION_HOURS=1

EMAIL_USERNAME=seu_email@gmail.com
EMAIL_PASSWORD=senha_do_email_ou_senha_de_app

GEMINI_API_KEY=SUA_CHAVE_API_GEMINI
```

Agora confira se o arquivo `backend/config.py` está assim:

```python

    MYSQL_HOST = os.getenv("MYSQL_HOST", "localhost")
    MYSQL_USER = os.getenv("MYSQL_USER", "root")
    MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "")
    MYSQL_DB = os.getenv("MYSQL_DB", "")
    MYSQL_PORT = int(os.getenv("MYSQL_PORT", 3306))

    SECRET_KEY = os.getenv("SECRET_KEY", "CHAVE_PADRAO")
    JWT_EXPIRATION = timedelta(hours=int(os.getenv("JWT_EXPIRATION_HOURS", 1)))

    EMAIL_USERNAME = os.getenv("EMAIL_USERNAME", "")
    EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD", "")

    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
```


## Autenticação (JWT)

Após login, o servidor retorna um **token**.
Ele deve ser enviado no header de todas as requisições protegidas:

```http
Authorization: Bearer seu_token_aqui
```



## Endpoints Principais da API

| Método | Rota                     | Descrição                      |
| ------ | ------------------------ | ------------------------------ |
| POST   | `/login`                 | Login do usuário               |
| POST   | `/register`              | Cadastro                       |
| GET    | `/media`                 | Retorna notas + média do aluno |
| POST   | `/api/chatbot/perguntar` | Envia mensagem ao chatbot      |



## Chatbot (Gemini IA)

O chatbot responde sobre:

* Como usar o sistema
* Cadastro e login
* Informações gerais da UniGestão

Se o usuário tentar perguntar algo fora do contexto → resposta educada orientando o limite.


## Autores

| Nome              | Responsabilidade                    | Linkedin                                                                                                       |
| ----------------- | ----------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| **Caio Carvalho** | Backend / Integrações / Arquitetura | [https://github.com/caiocrv](https://www.linkedin.com/in/caiocrv/)                                             |
| **Khimberlly**    | UI/UX / Frontend                    | [https://www.linkedin.com/in/khimberlly-lino-149592260](https://www.linkedin.com/in/khimberlly-lino-149592260) |
