from fastapi import FastAPI
app = FastAPI()

from app.routes.auth import auth_router
from app.routes.order import orders_router

app.include_router(auth_router)
app.include_router(orders_router)





