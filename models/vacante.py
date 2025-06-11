# importar modelo base
from db import Base
#importaciones de las clases sqlalchemy
from sqlalchemy import Enum,Column, Integer, String, Boolean, ForeignKey, DateTime, Table
from datetime import datetime
from sqlalchemy.orm import relationship


# Tabla Vacantes
class Vacante(Base):
    __tablename__ = "vacantes"
    id = Column(Integer, primary_key=True)
    contrato_id = Column(Integer, ForeignKey("contratos.id"))
    artista_id = Column(Integer, ForeignKey("artistas.usuario_id"))
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    descripcion = Column(String(255))
    titulo = Column(String(100))
    estado = Column(String(50))

    contrato = relationship("Contrato", back_populates="vacantes")
    postulaciones = relationship("Postulado", back_populates="vacante")