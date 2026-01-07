import pytest

@pytest.mark.asyncio
async def test_deposit_increases_balance(client):
    # Simula um depósito (Nota: Em um teste real, você precisaria do token JWT)
    # Aqui focamos na lógica que o CRUD executa
    payload = {"amount": 100.0, "type": "deposit", "description": "Pix recebido"}
    response = await client.post("/transactions/", json=payload)
    
    assert response.status_code == 201
    assert response.json()["amount"] == 100.0

@pytest.mark.asyncio
async def test_withdrawal_insufficient_funds(client):
    # Tenta sacar 500 sem ter saldo
    payload = {"amount": 500.0, "type": "withdrawal", "description": "Compra shopping"}
    response = await client.post("/transactions/", json=payload)
    
    assert response.status_code == 400
    assert response.json()["message"] == "Saldo insuficiente para realizar o saque."

@pytest.mark.asyncio
async def test_negative_value_validation(client):
    # Valida se o Pydantic bloqueia valores negativos (gt=0)
    payload = {"amount": -10.0, "type": "deposit"}
    response = await client.post("/transactions/", json=payload)
    
    assert response.status_code == 422 