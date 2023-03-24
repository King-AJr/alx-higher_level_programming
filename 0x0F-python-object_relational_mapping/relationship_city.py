#!/usr/bin/python3
"""
class definition of a City and 
an instance Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class City(Base):
    """
    class definition of a City and 
    an instance Base = declarative_base()
    __table_name__ : stores the table name
    id: auto-generated primary key
    name: stores name of the city
    state_id: foreign key linking to the state the city belongs to
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
