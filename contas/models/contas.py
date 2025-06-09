from shared.database import Base
from sqlalchemy import Column, Integer, String, Numeric


class Contas(Base):
    __tablename__ = "contas"

    id = Column(Integer, primary_key=True, autoincrement=True)
    descricao = Column(String(100), nullable=False)
    valor = Column(Numeric, nullable=False)
    tipo = Column(String(30), nullable=False)
