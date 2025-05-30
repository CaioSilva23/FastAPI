from fastapi.testclient import TestClient
from main import app


client = TestClient(app)


def test_get_contas():
    response = client.get("/contas/listar")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_criar_conta():
    data = {"descricao": "Conta Teste", "valor": 100.0, 'tipo': "Despesa"}
    response = client.post("/contas/criar", json=data)
    assert response.status_code == 201
    assert response.json()["descricao"] == "Conta Teste"
    assert response.json()["valor"] == "100.0"
    assert response.json()["tipo"] == "Despesa"
