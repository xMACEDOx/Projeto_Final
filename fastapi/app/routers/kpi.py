from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from ..database import SessionLocal
from ..models import KpiDashboard

router = APIRouter(prefix="/kpi", tags=["KPI"])

# Dependência para abrir/fechar sessão
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Retorna todas as linhas com seus KPIs
@router.get("/dashboard")
def get_all_kpis(db: Session = Depends(get_db)):
    data = db.query(KpiDashboard).all()
    return data

# Retorna uma linha específica
@router.get("/dashboard/{id_linha}")
def get_kpi_by_line(id_linha: str, db: Session = Depends(get_db)):
    data = db.query(KpiDashboard).filter(KpiDashboard.id_linha == id_linha).first()
    if not data:
        return {"error": "Linha não encontrada"}
    return data

# KPIs individuais

@router.get("/atraso")
def get_atraso_medio(db: Session = Depends(get_db)):
    try:
        # ✅ Corrigido: precisa envolver a query em text()
        result = db.execute(text("SELECT ROUND(AVG(atraso_medio_min), 2) AS atraso_medio FROM vw_kpi_dashboard"))
        row = result.fetchone()
        atraso = float(row[0]) if row and row[0] is not None else 0.0
        return {"atraso_medio_min": atraso}
    except Exception as e:
        print(" Erro no KPI atraso:", e)
        return {"error": str(e)}


@router.get("/frota")
def get_frota_total(db: Session = Depends(get_db)):
    try:
        # ✅ Corrigido: usa text() também
        result = db.execute(text("SELECT SUM(frota_ativa) AS total_frota_ativa FROM vw_kpi_dashboard"))
        row = result.fetchone()
        frota_total = int(row[0]) if row and row[0] is not None else 0
        return {"frota_ativa_total": frota_total}
    except Exception as e:
        print(" Erro no KPI frota:", e)
        return {"error": str(e)}
