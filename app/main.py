# app/main.py
from fastapi import FastAPI
from .middleware import ProcessTimeMiddleware
from .routers import tasks, music # <--- 1. IMPORTE O NOVO ROTEADOR

# Cria a aplicação FastAPI
app = FastAPI(
    title="API de Tarefas e Músicas (Estruturada)",
    description="Um projeto prático com FastAPI, Pydantic e Starlette bem organizado.",
    version="1.0.0"
)

# 1. Adiciona o Middleware (Starlette)
app.add_middleware(ProcessTimeMiddleware)

# 2. Inclui os Roteadores (FastAPI)
app.include_router(tasks.router)
app.include_router(music.router)

# Ponto de entrada básico
@app.get("/", include_in_schema=False)
async def read_root():
    return {"message": "Bem-vindo à API! Acesse /docs para ver a documentação."}