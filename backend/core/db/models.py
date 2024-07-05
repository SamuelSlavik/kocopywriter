from sqlalchemy.orm import relationship

from .databases import Base
from sqlalchemy import Column, String, Integer, TIMESTAMP, Boolean, UUID, LargeBinary, ForeignKey


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    email = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)


class Headline(Base):
    __tablename__ = "headlines"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    text = Column(String, nullable=False)


class Image(Base):
    __tablename__ = "images"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    url = Column(String, nullable=False)
    name = Column(String(255), nullable=False)


class PriceListItem(Base):
    __tablename__ = "price_list_items"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    second_description = Column(String, nullable=False)
    items = relationship("ItemWithPrice", collection_class=set)


class ItemWithPrice(Base):
    __tablename__ = "items_with_price"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    PriceListItem_id = Column(Integer, ForeignKey("price_list_items.id"))


class Brand(Base):
    __tablename__ = "brands"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(255), nullable=False)
    image = Column(String(255), nullable=False)


class Reference(Base):
    __tablename__ = "references_table"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    order = Column(Integer, nullable=False)
    name = Column(String(255), nullable=False)
    position = Column(String(255), nullable=False)
    url = Column(String, nullable=False)
    description = Column(String, nullable=False)
    image = Column(String(255), nullable=False)


class Project(Base):
    __tablename__ = "projects_table"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    order = Column(Integer, nullable=False)
    name = Column(String(255), nullable=False)
    url = Column(String, nullable=False)
    task = Column(String(255), nullable=False)
    description = Column(String, nullable=False)
    image = Column(String, nullable=False)


class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    title = Column(String(255), nullable=False)
    image = Column(String(255), nullable=False)
    short = Column(String, nullable=False)
    date = Column(String(255), nullable=False)
    content = Column(String, nullable=False)

