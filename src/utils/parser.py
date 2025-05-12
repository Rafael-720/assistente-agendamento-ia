from openai import OpenAI
import os
import json
from datetime import datetime


api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

def interpretar(comando):
    hoje = datetime.now().strftime("%d/%m/%Y")

    prompt = f"""
Hoje é {hoje}. Considere isso ao interpretar datas relativas como "amanhã" ou "depois de amanhã".

Extraia nome, data e hora do comando abaixo. Retorne JSON no formato:
{{"nome": "...", "data": "2025-05-09T10:00:00"}}

Comando: "{comando}"
"""
    resposta = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )

    conteudo = resposta.choices[0].message.content.strip()

    # 🔥 Remove blocos de código ```json ... ```
    if conteudo.startswith("```"):
        conteudo = conteudo.strip("```json").strip("`").strip()

    try:
        return json.loads(conteudo)
    except json.JSONDecodeError:
        print("❌ Erro ao interpretar resposta da OpenAI:")
        print("🔍 Conteúdo bruto:", repr(conteudo))
        raise
