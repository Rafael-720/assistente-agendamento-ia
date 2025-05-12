from fastapi import APIRouter
import requests
from src.services.stt_service import transcrever_audio
import sounddevice as sd
from scipy.io.wavfile import write
import tempfile
import os

voz_router = APIRouter()

@voz_router.post("/voz")
def processar_voz():
    try:
        # Grava áudio temporário
        taxa = 44100
        duracao = 5  # segundos
        print("🎙 Pressione Enter para dar um comando...")
        input()
        print("⏺ Ouvindo...")
        audio = sd.rec(int(duracao * taxa), samplerate=taxa, channels=1, dtype='int16')
        sd.wait()

        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmpfile:
            caminho_audio = tmpfile.name
            write(caminho_audio, taxa, audio)

        # Transcreve
        texto = transcrever_audio(caminho_audio)
        print("📝 Texto transcrito:", texto)

        # Chama o endpoint /comando local
        resposta = requests.post("http://localhost:8000/comando", json={"comando": texto})
        resultado = resposta.json()

        return {
            "transcricao": texto,
            "resultado": resultado
        }

    except Exception as e:
        return {"status": "erro", "mensagem": str(e)}
