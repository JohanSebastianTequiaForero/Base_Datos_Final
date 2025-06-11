# importar modelo base
from db import Base
#importaciones de las clases sqlalchemy
from sqlalchemy import Enum,Column, Integer, String, Boolean, ForeignKey, DateTime, Table
from datetime import datetime

# Tabla Categoría
class Categoria(Base):
    __tablename__ = "categorias"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100))