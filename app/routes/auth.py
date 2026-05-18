from fastapi import APIRouter


auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get("/", tags=["auth"])
async def auth():
    """
    Aqui pode adicionar comentario na documento na pagina /docs
    """
    return {"message": "Hello World"}


