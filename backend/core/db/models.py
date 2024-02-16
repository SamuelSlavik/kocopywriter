from database import Base
from sqlalchemy import Column, String, Integer, TIMESTAMP, Boolean, UUID


class User(Base):
    __tablename__ = "users"

    id = Column(UUID, primary_key=True, nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    password = Column(String(50), nullable=False)
    trusted = Column(Boolean, nullable=False)
