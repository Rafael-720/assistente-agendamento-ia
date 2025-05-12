from openai import OpenAI
from pathlib import Path
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def gerar_audio(texto, nome_arquivo="resposta.mp3", voz="nova"):
    caminho = Path(__file__).parent.parent / nome_arquivo

    with client.audio.speech.with_streaming_response.create(
        model="gpt-4o-mini-tts",
        voice=voz,
        input=texto,
        instructions="Fale de forma clara e natural com tom amigável.",
    ) as response:
        response.stream_to_file(caminho)

    return str(caminho)
