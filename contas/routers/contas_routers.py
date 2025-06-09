from fastapi import APIRouter, Depends
from pydantic import BaseModel
from decimal import Decimal
from typing import List
from sqlalchemy.orm import Session
from shared.depedencies import get_db
from contas.models.contas import Contas

router = APIRouter(prefix="/contas", tags=["Contas"])


class ContaResponse(BaseModel):
    """
    Classe de resposta para contas.
    Contém os atributos id e nome.
    """
    id: int
    descricao: str
    valor: Decimal
    tipo: str

    class Config:
        orm_mode = True


class ContaRequest(BaseModel):
    """
    Classe de resposta para contas.
    Contém os atributos id e nome.
    """
    descricao: str
    valor: Decimal
    tipo: str


@router.get("/listar", summary="Listar contas")
def listar_contas(db: Session = Depends(get_db)) -> List[ContaResponse]:
    """
    Função para listar contas.
    Retorna uma lista de contas.
    """
    contas = db.query(Contas).all()
    return contas


@router.post(
        path="/criar",
        summary="Criar conta",
        response_model=ContaResponse,
        status_code=201
)
def criar_conta(conta: ContaRequest, db: Session = Depends(get_db)) -> ContaRequest:
    """
    Função para criar uma nova conta.
    Retorna a conta criada.
    """

    nova_conta = Contas(**conta.model_dump())
    db.add(nova_conta)
    db.commit()
    db.refresh(nova_conta)

    return nova_conta
