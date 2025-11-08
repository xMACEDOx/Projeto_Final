from fastapi import FastAPI
from sqlalchemy import create_engine, text
import os

app = FastAPI()

# 🔹 Variáveis de ambiente do Docker
POSTGRES_USER = os.getenv("POSTGRES_USER", "PROJETO_FINAL")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "PROJETO_FINAL")
POSTGRES_DB = os.getenv("POSTGRES_DB", "sptrans_gold")
POSTGRES_HOST = os.getenv("POSTGRES_HOST", "postgres")
POSTGRES_PORT = os.getenv("POSTGRES_PORT", "5432")

DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

engine = create_engine(DATABASE_URL)

@app.get("/")
def root():
    return {"message": "API FastAPI conectada com sucesso ao Postgres!"}

@app.get("/linhas")
def get_linhas():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM linhas LIMIT 10"))
        data = [dict(row._mapping) for row in result]
    return {"linhas": data}