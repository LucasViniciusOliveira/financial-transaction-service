# from .transaction import Transaction
# from .installment import Installment
# from .recurrence_rule import RecurrenceRule
# from .category import Category

from datetime import date, datetime, timezone
from typing import Any, Dict, Generic, List, Optional, Type, TypeVar

from pydantic import BaseModel
from sqlalchemy import Select, String, asc, cast, desc, func, or_, select, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.sqltypes import Boolean, Date, DateTime, Integer
from sqlalchemy.sql.sqltypes import String as SAString

ModelType = TypeVar("ModelType")

class BaseRepository(Generic[ModelType]):
    def __init__(self, db: AsyncSession, model: Type[ModelType]):
        """
        Repositório base para operações genéricas em modelos SQLAlchemy.

        Args:
            db (AsyncSession): Sessão assíncrona do banco de dados.
            model (Type[ModelType]): Modelo SQLAlchemy associado ao repositório.
        """
        self.db_session = db
        self.model = model

    async def refresh_entity(self, instance: Any) -> None:
        await self.db_session.refresh(instance)

    async def create_entity(
        self, model: Type[ModelType], entity_data: Dict
    ) -> Optional[ModelType]:
        """
        Cria uma nova entidade com base no dicionário fornecido.

        Args:
            model (Type[ModelType]): O modelo da entidade a ser criada.
            entity_data (Dict): Campos e valores para criar uma nova entidade.

        Returns:
            Optional[ModelType]: Instância criada da entidade, ou None em caso de erro.
        """
        try:
            new_entity = model(**entity_data)
            self.db_session.add(new_entity)
            await self.db_session.commit()
            await self.db_session.refresh(new_entity)
            return new_entity
        except Exception as e:
            await self.db_session.rollback()
            print(f"Erro ao criar a entidade: {e}")
            raise

    async def soft_delete(self, entity_id: int) -> bool:
        """
        Realiza a exclusão lógica de uma entidade, marcando o campo 'deleted_at'.

        Args:
            entity_id (int): ID da entidade a ser excluída logicamente.

        Returns:
            bool: True se a entidade foi atualizada (soft delete realizado), False caso contrário.
        """
        query = (
            update(self.model)
            .where(self.model.id == entity_id)
            .values(deleted_at=datetime.now(timezone.utc))
        )
        result = await self.db_session.execute(query)
        await self.db_session.commit()

        return result.rowcount > 0

    async def get(
        self, entity_id: int | str, options: Optional[List] = None
    ) -> Optional[ModelType]:
        """
        Busca uma entidade pelo ID com suporte a carregamento opcional.

        Args:
            entity_id (int): ID da entidade a ser buscada.
            options (Optional[List], opcional): Lista de opções ORM como
                selectinload para carregar relacionamentos. Padrão é None.

        Returns:
            A entidade encontrada ou None se não existir ou estiver deletada.
        """
        query = select(self.model).where(
            self.model.id == entity_id, self.model.deleted_at.is_(None)
        )

        if options:
            query = query.options(*options)

        result = await self.db_session.execute(query)
        return result.scalar_one_or_none()

    async def get_multi(
        self,
        filters: Optional[dict[str, Any]] = None,
        offset: int = 0,
        limit: int = 10,
        sort_by: str = "id",
        order: str = "asc",
        global_filter: Optional[dict[str, Any]] = None,
        filter_schema: Optional[type[BaseModel]] = None,
    ):
        query: Select = select(self.model).where(self.model.deleted_at.is_(None))
        applied_filter = False

        # Filtros normais
        if filters:
            for attr, value in filters.items():
                if value is not None and hasattr(self.model, attr):
                    column = getattr(self.model, attr)

                    if isinstance(value, date) or isinstance(value, bool):
                        query = query.where(column == value)
                    else:
                        query = query.where(cast(column, String).ilike(f"%{value}%"))
            applied_filter = True

        # Filtro global dinâmico
        if not applied_filter and global_filter:
            conditions = []
            allowed_fields = (
                set(filter_schema.model_fields.keys()) if filter_schema else None
            )

            for column in self.model.__table__.columns:
                if (
                    column.primary_key
                    or column.foreign_keys
                    or (allowed_fields and column.key not in allowed_fields)
                ):
                    continue

                if isinstance(
                    column.type, (SAString, Integer, Boolean, Date, DateTime)
                ):
                    conditions.append(cast(column, String).ilike(f"%{global_filter}%"))

            query = query.where(or_(*conditions)) if conditions else query

        if hasattr(self.model, sort_by):
            column = getattr(self.model, sort_by)
            query = query.order_by(desc(column) if order == "desc" else asc(column))

        total_stmt = select(func.count()).select_from(query.subquery())
        total_result = await self.db_session.execute(total_stmt)

        result = await self.db_session.execute(query.offset(offset).limit(limit))

        return total_result.scalar(), result.scalars().all()

    async def list(self, skip: int = 0, limit: int = 100):
        query = select(self.model).offset(skip).limit(limit)
        result = await self.db_session.execute(query)
        return result.scalars().all()

    async def patch_entity(
        self, entity: Type[ModelType], entity_id: int, update_data: Dict
    ) -> bool:
        """
        Atualiza parcialmente os campos da entidade com base no dicionário fornecido.

        Args:
            entity (Any): O modelo da entidade a ser atualizada (por exemplo, Company, Address).
            entity_id (int): ID da entidade a ser atualizada.
            update_data (Dict): Campos e valores a serem atualizados.

        Returns:
            bool: True se a entidade foi atualizada com sucesso, False caso contrário.
        """
        update_data["updated_at"] = datetime.now(timezone.utc)

        # Garante que a entidade que está sendo atualizada é a correta
        query = update(entity).where(entity.id == entity_id).values(**update_data)

        result = await self.db_session.execute(query)
        await self.db_session.commit()

        return result.rowcount > 0

    async def partial_update(self, entity_id: int | str, values: Dict) -> bool:
        if not values:
            return False

        query = (
            update(self.model)
            .where(self.model.id == entity_id, self.model.deleted_at.is_(None))
            .values(**values)
        )
        result = await self.db_session.execute(query)
        await self.db_session.commit()
        return result.rowcount > 0