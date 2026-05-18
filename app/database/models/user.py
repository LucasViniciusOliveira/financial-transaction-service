from sqlalchemy import Column, String, Integer

from app.database.connection import Base

class User(Base):
    __tablename__ = "users"

    id = Column("id", Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column("name", String, nullable=False)
    email = Column("email", String, nullable=False)
    password = Column("password", String, nullable=False)
    status = Column("status", String, default="active")
    roles = Column("roles", String)

    def __init__(self, name, email, password, roles, status = "active",):
        self.name = name
        self.email = email
        self.password = password
        self.status = status
        self.roles = roles