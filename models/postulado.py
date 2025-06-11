# importar modelo base
from db import Base
#importaciones de las clases sqlalchemy
from sqlalchemy import Enum,Column, Integer, String, Boolean, ForeignKey, DateTime, Table
from datetime import datetime
from sqlalchemy.orm import relationship

# Tabla Postulados
class Postulado(Base):
    __tablename__ = "postulados"
    id = Column(Integer, primary_key=True)
    vacante_id = Column(Integer, ForeignKey("vacantes.id"))
    artista_id = Column(Integer, ForeignKey("artistas.usuario_id"))
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))

    vacante = relationship("Vacante", back_populates="postulaciones")