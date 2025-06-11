# importar modelo base
from db import Base
#importaciones de las clases sqlalchemy
from sqlalchemy import Enum,Column, Integer, String, Boolean, ForeignKey, DateTime, Table
from datetime import datetime
from sqlalchemy.orm import relationship

# Tabla Competencias (1 a muchos con Artista)
class Competencia(Base):
    __tablename__ = "competencias"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100))
    descripcion = Column(String(255))
    fecha_inicio = Column(DateTime)
    fecha_fin = Column(DateTime)
    artista_id = Column(Integer, ForeignKey("artistas.usuario_id"))

    artista = relationship("Artista", back_populates="competencias")