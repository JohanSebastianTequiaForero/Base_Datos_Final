# importar modelo base
from db import Base
#importaciones de las clases sqlalchemy
from sqlalchemy import Enum,Column, Integer, String, Boolean, ForeignKey, DateTime, Table
from datetime import datetime
from sqlalchemy.orm import relationship

# Tabla Contrato
class Contrato(Base):
    __tablename__ = "contratos"
    id = Column(Integer, primary_key=True)
    creador_id = Column(Integer, ForeignKey("usuarios.id"))
    fecha_inicio = Column(DateTime)
    fecha_fin = Column(DateTime)
    descripcion = Column(String(255))

    vacantes = relationship("Vacante", back_populates="contrato")