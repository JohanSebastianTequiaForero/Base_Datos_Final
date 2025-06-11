# importar modelo base
from db import Base
#importaciones de las clases sqlalchemy
from sqlalchemy import Enum,Column, Integer, String, Boolean, ForeignKey, DateTime, Table

# Tabla Contratistas
class Contratista(Base):
    __tablename__ = "contratistas"
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), primary_key=True)
    rol_id = Column(Integer, ForeignKey("roles.id"))
    contratos_realizados = Column(Integer)
    contratos_pendientes = Column(Integer)
    publicaciones = Column(Integer)
    activo = Column(Boolean, default=True)