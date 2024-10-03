from fastapi.testclient import TestClient
from app.main import app
from app.database import users_collection, funds_collection, transactions_collection

client = TestClient(app)

# Datos de prueba
USER_ID = "user123"
FUND_ID = "fund123"
INVALID_FUND_ID = "fund999"

# Setup inicial (Crear usuario y fondo en la base de datos)
def setup_module(module):
    users_collection.insert_one({"id": USER_ID, "name": "Test User", "balance": 1000})
    funds_collection.insert_one({"id": FUND_ID, "name": "Test Fund", "minimum_amount": 500})

# Teardown (Eliminar datos de prueba al finalizar)
def teardown_module(module):
    users_collection.delete_one({"id": USER_ID})
    funds_collection.delete_one({"id": FUND_ID})
    transactions_collection.delete_many({"user_id": USER_ID})

# Prueba para suscribirse a un fondo
def test_suscribirse_a_fondo():
    response = client.post(f"/fondos/suscribirse?user_id={USER_ID}&fund_id={FUND_ID}")
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Suscripción exitosa"
    assert "transaction_id" in data

# Prueba para cancelar la suscripción de un fondo
def test_cancelar_fondo():
    response = client.post(f"/fondos/cancelar?user_id={USER_ID}&fund_id={FUND_ID}")
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Cancelación exitosa"
    assert "transaction_id" in data

# Prueba de error al suscribirse a un fondo no existente
def test_suscribirse_fondo_invalido():
    response = client.post(f"/fondos/suscribirse?user_id={USER_ID}&fund_id={INVALID_FUND_ID}")
    assert response.status_code == 404
    data = response.json()
    assert data["detail"] == "Usuario o Fondo no encontrado"
