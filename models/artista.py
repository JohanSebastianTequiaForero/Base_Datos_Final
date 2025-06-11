# importar modelo base
from db import Base
#importaciones de las clases sqlalchemy
from sqlalchemy import Enum,Column, Integer, String, Boolean, ForeignKey, DateTime, Table
from datetime import datetime
from sqlalchemy.orm import relationship

class Artista(Base):
    __tablename__ = "artistas"
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), primary_key=True)
    nombre = Column(String(50))
    seguidores = Column(Integer)
    genero_id = Column(Integer, ForeignKey("generos_musicales.id"))

    genero = relationship("GeneroMusical")
    competencias = relationship("Competencia", back_populates="artista")