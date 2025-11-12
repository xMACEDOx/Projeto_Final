from fastapi import FastAPI
from .routers import kpi

app = FastAPI(
    title="SPTrans KPI API",
    description="API para disponibilizar KPIs do projeto SPTrans (camada Gold).",
    version="1.0.0"
)

app.include_router(kpi.router)

@app.get("/")
def root():
    return {"message": "SPTrans KPI API está online 🚍"}