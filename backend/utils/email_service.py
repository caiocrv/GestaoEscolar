import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask import current_app

def enviar_email(nome, destinatario, email_academico):
    remetente = current_app.config["EMAIL_USERNAME"]
    senha = current_app.config["EMAIL_PASSWORD"]
    assunto = "Você concluiu o cadastro na UniGestao"
    corpo = f"""
    Olá, {nome}!
    
    Seu cadastro foi criado com sucesso.
    Seu usuário é: {email_academico}

    Bem-vindo à Universidade UniGestão!
    """

    mensagem = MIMEMultipart()
    mensagem['From'] = remetente
    mensagem['To'] = destinatario
    mensagem['Subject'] = assunto

    mensagem.attach(MIMEText(corpo, 'plain'))

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(remetente, senha)
            server.send_message(mensagem)
        print(f"E-mail enviado para {destinatario}")
    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")