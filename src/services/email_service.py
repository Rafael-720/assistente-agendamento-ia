import smtplib
import os
from email.message import EmailMessage


def enviar_email(nome, data):
    remetente = os.getenv("EMAIL_ORIGEM")
    senha = os.getenv("EMAIL_SENHA")
    destinatario = os.getenv("EMAIL_DESTINO")
    

    assunto = "Confirmação de Reunião"
    corpo = f"Reunião com {nome} agendada para {data}."

    # ✅ Cria mensagem com suporte a acentos (UTF-8)
    msg = EmailMessage()
    msg["Subject"] = assunto
    msg["From"] = remetente
    msg["To"] = destinatario
    msg.set_content(corpo, charset="utf-8")

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(remetente, senha)
            server.send_message(msg)
            print("✅ E-mail enviado com sucesso!")
    except Exception as e:
        print("❌ Erro ao enviar e-mail:", e)
