# importar modelo base
from db import Base
#importaciones de las clases sqlalchemy
from sqlalchemy import Enum,Column, Integer, String, Boolean, ForeignKey, DateTime, Table

# Tabla Espectadores
class Espectador(Base):
    __tablename__ = "espectadores"
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), primary_key=True)
    rol_id = Column(Integer, ForeignKey("roles.id"))
    artistas_seguidos = Column(Integer)
    artista_mas_reproducido = Column(Integer) 