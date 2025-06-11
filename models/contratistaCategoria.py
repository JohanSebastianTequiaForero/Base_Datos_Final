# importar modelo base
from db import Base
#importaciones de las clases sqlalchemy
from sqlalchemy import Enum,Column, Integer, String, Boolean, ForeignKey, DateTime, Table
from datetime import datetime
from sqlalchemy.orm import relationship

# Tabla Intermedia Contratista - Categoría
class ContratistaCategoria(Base):
    __tablename__ = "contratista_categoria"
    id = Column(Integer, primary_key=True)
    contratista_id = Column(Integer, ForeignKey("usuarios.id"))
    categoria_id = Column(Integer, ForeignKey("categorias.id"))