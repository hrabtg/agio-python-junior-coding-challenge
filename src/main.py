from fastapi import FastAPI
from src.api.routes import router as api_router

app = FastAPI(title="Desafio Técnico – Desenvolvedor Python")
app.include_router(api_router)