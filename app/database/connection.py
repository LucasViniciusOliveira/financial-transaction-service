# CONEXÃO SINCRONA

# from sqlalchemy import create_engine
# from sqlalchemy.orm import declarative_base, sessionmaker
#
# from app.config.settings import settings
#
# engine = create_engine(
#     settings.database_url,
#     pool_pre_ping=True,
# )
#
# SessionLocal = sessionmaker(
#     autocommit=False,
#     autoflush=False,
#     bind=engine,
# )
#
# Base = declarative_base()

# CONEXÃO ASINCRONA
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from app.config.settings import settings

engine = create_async_engine(
    settings.database_url,
    echo=False,
    future=True,
    # Pool tuning
    pool_size=10,  # conexões fixas por container
    max_overflow=20,  # conexões extras sob pico
    pool_timeout=30,  # tempo esperando conexão livre
    pool_recycle=240,  # recicla antes do MySQL matar
    # pool_pre_ping=True,  # evita usar conexão morta
)

async_session = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

async def get_db():
    async with async_session() as session:
        yield session