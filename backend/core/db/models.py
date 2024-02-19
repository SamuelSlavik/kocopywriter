from .databases import Base
from sqlalchemy import Column, String, Integer, TIMESTAMP, Boolean, UUID


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
