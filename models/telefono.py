# importar modelo base
from db import Base
#importaciones de las clases sqlalchemy
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, Table

# Tabla Teléfonos
class Telefono(Base):
    __tablename__ = "telefonos"
    id = Column(Integer, primary_key=True)
    numero = Column(String(20))
    usuario_id = Column(Integer, 
                        ForeignKey("usuarios.id"))