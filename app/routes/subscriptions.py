from fastapi import APIRouter, HTTPException
from models import User, Fund, Transaction
from database import users_collection, funds_collection, transactions_collection
from notification import send_notification
import uuid
from datetime import datetime

router = APIRouter()


@router.get("/fondos/suscribirse")
def suscribirse(user_id: str, fund_id: str):
    user = users_collection.find_one({"id": user_id})
    fund = funds_collection.find_one({"id": fund_id})

    if not user or not fund:
        raise HTTPException(
            status_code=404, detail="Usuario o Fondo no encontrado")

    if user['balance'] < fund['minimum_amount']:
        raise HTTPException(
            status_code=400, detail=f"No tiene saldo disponible para vincularse al fondo {fund['name']}")

    transaction_id = str(uuid.uuid4())
    transaction = {
        "id": transaction_id,
        "user_id": user_id,
        "fund_id": fund_id,
        "amount": fund['minimum_amount'],
        "type": "suscripción",
        "date": datetime.now()
    }

    transactions_collection.insert_one(transaction)
    users_collection.update_one(
        {"id": user_id}, {"$inc": {"balance": -fund['minimum_amount']}})

    send_notification(
        user_id, f"Suscrito exitosamente al fondo {fund['name']}", "sms")

    return {"message": "Suscripción exitosa", "transaction_id": transaction_id}

# Endpoint para cancelar suscripción


@router.get("/fondos/cancelar")
def cancelar(user_id: str, fund_id: str):
    user = users_collection.find_one({"id": user_id})
    fund = funds_collection.find_one({"id": fund_id})

    if not user or not fund:
        raise HTTPException(
            status_code=404, detail="Usuario o Fondo no encontrado")

    transaction_id = str(uuid.uuid4())
    transaction = {
        "id": transaction_id,
        "user_id": user_id,
        "fund_id": fund_id,
        "amount": fund['minimum_amount'],
        "type": "cancelación",
        "date": datetime.now()
    }

    transactions_collection.insert_one(transaction)
    users_collection.update_one(
        {"id": user_id}, {"$inc": {"balance": fund['minimum_amount']}})

    send_notification(
        user_id, f"Cancelada la suscripción al fondo {fund['name']}", "email")

    return {"message": "Cancelación exitosa", "transaction_id": transaction_id}
