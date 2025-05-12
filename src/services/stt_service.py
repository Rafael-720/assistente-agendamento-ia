import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def transcrever_audio(caminho_arquivo):
    with open(caminho_arquivo, "rb") as audio_file:
        resposta = client.audio.transcriptions.create(
            model="gpt-4o-transcribe",
            file=audio_file,
            response_format="text"
        )
    return resposta
