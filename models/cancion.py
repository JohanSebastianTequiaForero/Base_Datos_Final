# importar modelo base
from db import Base
#importaciones de las clases sqlalchemy
from sqlalchemy import Enum,Column, Integer, String, Boolean, ForeignKey, DateTime, Table
from datetime import datetime

# Tabla Canciones
class Cancion(Base):
    __tablename__ = "canciones"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100))
    artista_id = Column(Integer, ForeignKey("artistas.usuario_id"))
    genero_id = Column(Integer, ForeignKey("generos_musicales.id"))
    fecha_creacion = Column(DateTime, default=datetime.now)