from fastapi import APIRouter
from pydantic import BaseModel
from decimal import Decimal
from typing import List

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


class ContaRequest(BaseModel):
    """
    Classe de resposta para contas.
    Contém os atributos id e nome.
    """
    descricao: str
    valor: Decimal
    tipo: str


@router.get("/listar", summary="Listar contas")
def listar_contas() -> List[ContaResponse]:
    """
    Função para listar contas.
    Retorna uma lista de contas.
    """
    return [
        ContaResponse(
            id=1,
            descricao="Conta de Luz",
            valor=Decimal("150.00"),
            tipo="Despesa"
        ),
        ContaResponse(
            id=2,
            descricao="Conta de Luz 1",
            valor=Decimal("150.00"),
            tipo="Despesa"
        ),
    ]


@router.post(
        path="/criar",
        summary="Criar conta",
        response_model=ContaResponse,
        status_code=201
)
def criar_conta(conta: ContaRequest) -> ContaRequest:
    """
    Função para criar uma nova conta.
    Retorna a conta criada.
    """
    return ContaResponse(
        id=3,
        descricao=conta.descricao,
        valor=conta.valor,
        tipo=conta.tipo
    )
