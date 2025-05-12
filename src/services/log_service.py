import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os


def registrar_log(nome, data, acao, status):
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("credenciais_google.json", scope)
    client = gspread.authorize(creds)

    sheet = client.open_by_key(os.getenv("GOOGLE_SHEET_ID")).sheet1
    sheet.append_row([nome, data, acao, status])
