# importar modelo base
from db import Base
#importaciones de las clases sqlalchemy
from sqlalchemy import   Column, Integer, String, Boolean, ForeignKey, DateTime, Table


# Tabla Géneros Musicales
class GeneroMusical(Base):
    __tablename__ = "generos_musicales"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50))
