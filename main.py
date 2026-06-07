from fastapi import FastAPI

from app.routes.transaction import transaction_router

app = FastAPI()

from app.routes.auth import auth_router
from app.routes.order import orders_router

app.include_router(auth_router)
app.include_router(orders_router)
app.include_router(transaction_router)





