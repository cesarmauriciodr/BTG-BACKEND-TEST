# models.py
from pydantic import BaseModel
from datetime import datetime

class User(BaseModel):
    """Modelo de usuario"""
    id: str
    name: str
    balance: float

class Fund(BaseModel):
    """Modelo de fondo"""
    id: str
    name: str
    category: str
    minimum_amount: float

class Transaction(BaseModel):
    """Modelo de transacción"""
    id: str
    user_id: str
    fund_id: str
    amount: float
    type: str  # suscripción o cancelación
    date: datetime = datetime.now()

class Notification(BaseModel):
    """Modelo de notificación"""
    user_id: str
    message: str
    via: str  # email or sms
