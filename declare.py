import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, JSON, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class API(Base):
  __tablename__ = 'api'
  id = Column(Integer, Sequence("item_id_seq"), primary_key=True, nullable=False)
  information = Column(JSON, nullable=True)

class Checksum(Base):
  __tablename__ = 'checksum'
  id = Column(Integer, primary_key = True)
  checkSum = Column(String)

engine = create_engine('sqlite:///api_sqlalchemy.sqlite')
 
from sqlalchemy.orm import sessionmaker
session = sessionmaker()
session.configure(bind=engine)
Base.metadata.create_all(engine)