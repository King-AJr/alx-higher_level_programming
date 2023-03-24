#!/usr/bin/python3
"""
class definition of a State and 
an instance Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String
from relationship_city import Base, City
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


class State(Base):
    """
    class definition of a State and 
    an instance Base = declarative_base()
    __table_name__ : stores the table name
    id: auto-generated primary key
    name: stores name of state
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade = "all, delete")
