# importar modelo base
from db import Base
#importaciones de las clases sqlalchemy
from sqlalchemy import Enum,Column, Integer, String, Boolean, ForeignKey, DateTime, Table

class Publicacion(Base):
    __tablename__ = "publicaciones"
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), primary_key=True)
    rol_id = Column(Integer, ForeignKey("roles.id"))
    likes = Column(Integer)
    reproducciones = Column(Integer)
    vistas = Column(Integer)
    tipo_de_publicacion = Column(String(80))
    nombre_del_archivo = Column(String(100))