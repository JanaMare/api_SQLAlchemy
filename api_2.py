from sqlalchemy import create_engine, Integer, JSON, Column, Sequence
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from movies import data

Base = declarative_base()


class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, Sequence("item_id_seq"), primary_key=True, nullable=False)
    information = Column(JSON, nullable=True)

engine = create_engine("sqlite://", echo=True)

Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)


first_item = Item()
first_item.information = dict(data)


session.add(first_item)
session.commit()


for item in session.query(Item).all():
    print(type(item.information))
    print(item.id, item.information)
