from fastapi import FastAPI
from routes import subscriptions, transactions

app = FastAPI()

# Incluir las rutas de las suscripciones y transacciones
app.include_router(subscriptions.router, prefix="/fondos")
app.include_router(transactions.router, prefix="/transacciones")

# Ruta raíz de prueba
@app.get("/")
def read_root():
    return {"message": "API de gestión de fondos funcionando correctamente"}
