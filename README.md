# assistente-agendamento-ia
voice-scheduling-assistant

# 🤖 Assistente de Agendamento com IA

Este é um protótipo funcional de um assistente inteligente capaz de entender comandos em linguagem natural, agendar eventos, enviar confirmações por e-mail, registrar logs e gerar resposta por voz.

## 🚀 Funcionalidades

- ✍️ Interpretação de comandos de texto com OpenAI GPT
- 📅 Criação automática de eventos no Google Calendar
- 📧 Envio de e-mail de confirmação via Gmail SMTP
- 📊 Registro de eventos no Google Sheets
- 🎙 Entrada por voz (gravação e transcrição com Whisper)
- 🔊 Saída por voz (resposta falada com TTS OpenAI)

## 🛠 Requisitos

- Python 3.10+
- Conta e credenciais da OpenAI
- Conta Google com permissões para Calendar e Sheets
- `.env` configurado

## 📂 Estrutura

```
src/
├── controllers/
│   ├── comando_controller.py
│   └── voz_controller.py
├── services/
│   ├── calendar_service.py
│   ├── email_service.py
│   ├── log_service.py
│   ├── stt_service.py
│   └── tts_service.py
├── utils/
│   └── parser.py
└── main.py
```

## ⚙️ Variáveis de Ambiente (.env)

```env
OPENAI_API_KEY=sk-...
EMAIL_ORIGEM=seu@email.com
EMAIL_SENHA=senha_de_app
EMAIL_DESTINO=destinatario@email.com
GOOGLE_SHEET_ID=ID_da_planilha
GOOGLE_CALENDAR_ID=ID_do_calendario
PLAY_AUDIO=True
```

## ▶️ Como rodar

1. Instale as dependências:
```bash
pip install -r requirements.txt
```

2. Rode a API:
```bash
uvicorn src.main:app --reload
```

3. Teste:
- Comando de texto:
```bash
curl -X POST http://localhost:8000/comando -H "Content-Type: application/json" -d "{"comando": "Agendar reunião com a Regina amanhã às 11h"}"
```

- Comando de voz:
```bash
curl -X POST http://localhost:8000/voz
```

## 🎥 Demonstração

Veja o vídeo com o sistema funcionando em tempo real (link a ser adicionado).

## 📄 Licença

Uso educacional e demonstrativo.


## 📞 Contato

Rafael Oliveira - [LinkedIn](https://linkedin.com/in/rafael-oliveira720)

---

💡 Projeto dedicado ao avanço e aplicação prática de tecnologias de IA em processamento de linguagem natural.
