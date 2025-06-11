# importar modelo base
from db import Base
#importaciones de las clases sqlalchemy
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, Table


# Relación Usuario ↔ Género (muchos a muchos)
class UsuarioGenero(Base):
    __tablename__ = "usuarios_generos"
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), primary_key=True)
    genero_id = Column(Integer, ForeignKey("generos_musicales.id"), primary_key=True)