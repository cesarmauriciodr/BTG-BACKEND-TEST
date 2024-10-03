from fastapi.testclient import TestClient
from app.main import app
from app.database import transactions_collection, users_collection

client = TestClient(app)

# Datos de prueba
USER_ID = "user123"

# Teardown (Eliminar datos de prueba al finalizar)
def teardown_module(module):
    transactions_collection.delete_many({"user_id": USER_ID})

# Prueba para obtener el historial de transacciones
def test_obtener_transacciones():
    # Insertar una transacción de prueba
    transactions_collection.insert_one({
        "id": "trans123",
        "user_id": USER_ID,
        "fund_id": "fund123",
        "amount": 500,
        "type": "suscripción",
        "date": "2023-01-01T00:00:00"
    })

    response = client.get(f"/transacciones?user_id={USER_ID}")
    assert response.status_code == 200
    data = response.json()
    assert len(data["transacciones"]) > 0
    assert data["transacciones"][0]["user_id"] == USER_ID
    assert data["transacciones"][0]["type"] == "suscripción"
