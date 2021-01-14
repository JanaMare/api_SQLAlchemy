from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import json

from declare import API, Checksum, Base
from movies import data

engine = create_engine('sqlite:///api_sqlalchemy.sqlite')

Base.metadata.bind = engine

DBSession = sessionmaker( bind = engine )

session = DBSession()

print(type(data))

json_str = """{"id": 1, "name": "yetship"}"""
obj = json.loads(data)
api = API(**obj)

session.add(api)
session.commit