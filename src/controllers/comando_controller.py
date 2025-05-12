from fastapi import APIRouter
from pydantic import BaseModel
from src.utils.parser import interpretar
from src.services.calendar_service import criar_evento
from src.services.email_service import enviar_email
from src.services.log_service import registrar_log
from src.services.tts_service import gerar_audio
from datetime import datetime
import os

interpretar_comando = APIRouter()

class Comando(BaseModel):
    comando: str

@interpretar_comando.post("/comando")
def executar(comando: Comando):
    try:
        dados = interpretar(comando.comando)

        # converte a data ISO para formato amigável
        data_formatada = datetime.fromisoformat(dados["data"]).strftime("%d/%m/%Y às %Hh")

        criar_evento(dados["nome"], dados["data"])
        enviar_email(dados["nome"], data_formatada)
        registrar_log(dados["nome"], data_formatada, "evento criado", "OK")

        #Geração de resposta por voz
        texto_audio = f"Reunião com {dados['nome']} agendada para {data_formatada}."
        caminho_audio = gerar_audio(texto_audio)

        #Executa o áudio automaticamente (Windows)
        if os.getenv("PLAY_AUDIO", "False") == "True":
            try:
                os.system(f'start {caminho_audio}')  # Windows
            except Exception as e:
                print("⚠️ Erro ao tentar executar o áudio:", e)

        return {
            "status": "sucesso",
            "dados": dados,
            "audio": caminho_audio
        }

    except Exception as e:
        return {"status": "erro", "mensagem": str(e)}
