from fastapi import APIRouter
from database import transactions_collection

router = APIRouter()


@router.get("/")
# Historial de transacciones
def obtener_transacciones(user_id: str):
    transacciones = list(transactions_collection.find({"user_id": user_id}))
    return {"transacciones": transacciones}
