# assistente-agendamento-ia
voice-scheduling-assistant

# 🤖 Assistente de Agendamento com IA

Protótipo funcional de um assistente inteligente capaz de entender comandos de texto ou voz, agendar eventos no Google Calendar, enviar e-mail de confirmação, registrar log em planilha e responder com áudio gerado por IA.

## 🚀 Funcionalidades

- ✍️ Interpretação de comandos de texto com OpenAI GPT (GPT-4o)
- 📅 Criação de evento no Google Calendar
- 📧 Envio de e-mail de confirmação com SMTP
- 📊 Registro de evento no Google Sheets
- 🎙 Entrada por voz com gravação e transcrição via Whisper
- 🔊 Resposta por voz com TTS (Text-to-Speech)

## 🛠 Requisitos

- Python 3.10+
- Conta e credenciais da OpenAI
- Conta Google com permissões para Calendar e Sheets
- `.env` configurado

## 📂 Estrutura

```
src/
├── controllers/
│ ├── comando_controller.py # Lida com /comando
│ └── voz_controller.py # Lida com /voz (gravação e transcrição)
├── services/
│ ├── calendar_service.py # Integra com Google Calendar
│ ├── email_service.py # Envia e-mail
│ ├── log_service.py # Registra no Google Sheets
│ ├── stt_service.py # Transcrição de áudio
│ └── tts_service.py # Geração de áudio TTS
├── utils/
│ └── parser.py # Interpreta comando em linguagem natural
└── main.py
```


## ▶️ Como rodar

1. Clone o repositório e crie um ambiente virtual
   
2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Crie e configure o arquivo .env
```env
OPENAI_API_KEY=sk-...
EMAIL_ORIGEM=seu@email.com
EMAIL_SENHA=senha_de_app
EMAIL_DESTINO=destinatario@email.com
GOOGLE_SHEET_ID=ID_da_planilha
GOOGLE_CALENDAR_ID=ID_do_calendario
PLAY_AUDIO=True  #Para desativar a reprodução automática do áudio, use no .env
```
A senha de app deve ser criada no Google Conta > Segurança > Senhas de app.

4. Configurar Google Sheets e Calendar
   ✅ Google Cloud Platform
   4.1 Acesse: https://console.cloud.google.com

   4.2 Crie um novo projeto

   4.3 Ative as APIs:

      * Google Sheets API

      * Google Calendar API

   4.4 Vá em "Credenciais" e crie uma chave de conta de serviço (JSON)

   4.5 Salve como credenciais_google.json na raiz do projeto

   4.6 Compartilhe a planilha e o calendário com o e-mail da conta de serviço (xxx@xxx.iam.gserviceaccount.com) com permissão de editor

5. Rode a API:
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
* Pressione Enter

* Fale algo como: “Agendar reunião com Rafael amanhã às 15h”

* O sistema:

   * Transcreve

   * Agenda

   * Envia e-mail

   * Registra no Sheets

   * Reponde com áudio 🎧



## 📄 Licença

Uso educacional e demonstrativo.


## 📞 Contato

Rafael Oliveira - [LinkedIn](https://linkedin.com/in/rafael-oliveira720)

----

💡 Projeto dedicado ao avanço e aplicação prática de tecnologias de IA em processamento de linguagem natural.
