from fastapi import FastAPI
from src.controllers.comando_controller import interpretar_comando
from src.controllers.voz_controller import voz_router
from dotenv import load_dotenv
load_dotenv()


app = FastAPI()

app.include_router(interpretar_comando)
app.include_router(voz_router)