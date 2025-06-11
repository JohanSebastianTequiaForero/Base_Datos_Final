# importar modelo base
from db import Base
#importaciones de las clases sqlalchemy
from sqlalchemy import Enum,Column, Integer, String, Boolean, ForeignKey, DateTime, Table
from datetime import datetime
from models.enums import TipoDocumento


class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50))
    apellidos = Column(String(50))
    documento = Column(Enum(TipoDocumento))
    correo = Column(String(100))
    rol_id = Column(Integer, ForeignKey("roles.id"))
    creado_en = Column(DateTime, default=datetime.now)
    finalizado_en = Column(DateTime, nullable=True)