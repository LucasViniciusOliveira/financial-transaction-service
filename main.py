from fastapi import FastAPI



app = FastAPI()

from app.routes.category import category_router
from app.routes.transaction import transaction_router


app.include_router(category_router)
app.include_router(transaction_router)





