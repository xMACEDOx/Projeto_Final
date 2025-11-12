from sqlalchemy import Column, String, Float, Integer
from .database import Base

class KpiDashboard(Base):
    __tablename__ = "vw_kpi_dashboard"

    id_linha = Column(String, primary_key=True)
    total_registros = Column(Integer)
    frota_ativa = Column(Integer)
    atraso_medio_min = Column(Float)
    acessibilidade_perc = Column(Float)
    operacao_ativa_perc = Column(Float)