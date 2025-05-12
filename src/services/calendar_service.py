from google.oauth2 import service_account
from googleapiclient.discovery import build
import os

def criar_evento(nome, data_iso):
    SCOPES = ['https://www.googleapis.com/auth/calendar']
    creds = service_account.Credentials.from_service_account_file(
        'credenciais_google.json', scopes=SCOPES)
    service = build('calendar', 'v3', credentials=creds)

    calendar_id = os.getenv("GOOGLE_CALENDAR_ID")

    evento = {
        'summary': f'Reunião com {nome}',
        'start': {'dateTime': data_iso, 'timeZone': 'America/Sao_Paulo'},
        'end': {'dateTime': data_iso, 'timeZone': 'America/Sao_Paulo'},
    }
    try:
        service.events().insert(calendarId=calendar_id, body=evento).execute()
        print("✅ Evento criado no Google Calendar")
    except Exception as e:
        print("❌ Erro ao criar evento no Calendar:", e)
        raise
