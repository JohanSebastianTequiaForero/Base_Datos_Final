# importar modelo base
from db import Base
#importaciones de las clases sqlalchemy
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, Table

class Rol(Base):
    __tablename__ = "roles"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(30), nullable=False)