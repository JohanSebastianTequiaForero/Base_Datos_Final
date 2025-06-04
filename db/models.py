from.database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, Table
from sqlalchemy.orm import relationship
from datetime import datetime



#Crear la clase de modelo(Entidad)

class Rol(Base):
    __tablename__ = "roles"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(30), nullable=False)

# Tabla Usuarios
class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50))
    apellidos = Column(String(50))
    correo = Column(String(100))
    rol_id = Column(Integer, ForeignKey("roles.id"))
    creado_en = Column(DateTime, default=datetime.utcnow)
    finalizado_en = Column(DateTime, nullable=True)

# Tabla Teléfonos
class Telefono(Base):
    __tablename__ = "telefonos"
    id = Column(Integer, primary_key=True)
    numero = Column(String(20))
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))

# Tabla Géneros Musicales
class GeneroMusical(Base):
    __tablename__ = "generos_musicales"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50))

# Relación Usuario ↔ Género (muchos a muchos)
class UsuarioGenero(Base):
    __tablename__ = "usuarios_generos"
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), primary_key=True)
    genero_id = Column(Integer, ForeignKey("generos_musicales.id"), primary_key=True)

# Tabla Publicacion
class Publicacion(Base):
    __tablename__ = "publicaciones"
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), primary_key=True)
    rol_id = Column(Integer, ForeignKey("roles.id"))
    likes = Column(Integer)
    reproducciones = Column(Integer)
    vistas = Column(Integer)
    tipo_de_publicacion = Column(String(80))
    nombre_del_archivo = Column(String(100))
    

# Tabla Contratistas
class Contratista(Base):
    __tablename__ = "contratistas"
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), primary_key=True)
    rol_id = Column(Integer, ForeignKey("roles.id"))
    contratos_realizados = Column(Integer)
    contratos_pendientes = Column(Integer)
    publicaciones = Column(Integer)
    activo = Column(Boolean, default=True)

# Tabla Canciones
class Cancion(Base):
    __tablename__ = "canciones"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100))
    artista_id = Column(Integer, ForeignKey("artistas.usuario_id"))
    genero_id = Column(Integer, ForeignKey("generos_musicales.id"))
    fecha_creacion = Column(DateTime, default=datetime.utcnow)

# Tabla Espectadores
class Espectador(Base):
    __tablename__ = "espectadores"
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), primary_key=True)
    rol_id = Column(Integer, ForeignKey("roles.id"))
    artistas_seguidos = Column(Integer)
    artista_mas_reproducido = Column(Integer) 

class Artista(Base):
    __tablename__ = "artistas"
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), primary_key=True)
    nombre = Column(String(50))
    seguidores = Column(Integer)
    genero_id = Column(Integer, ForeignKey("generos_musicales.id"))

    genero = relationship("GeneroMusical")
    competencias = relationship("Competencia", back_populates="artista")

# Tabla Competencias (1 a muchos con Artista)
class Competencia(Base):
    __tablename__ = "competencias"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100))
    descripcion = Column(String(255))
    fecha_inicio = Column(DateTime)
    fecha_fin = Column(DateTime)
    artista_id = Column(Integer, ForeignKey("artistas.usuario_id"))

    artista = relationship("Artista", back_populates="competencias")

# Tabla Contrato
class Contrato(Base):
    __tablename__ = "contratos"
    id = Column(Integer, primary_key=True)
    creador_id = Column(Integer, ForeignKey("usuarios.id"))
    fecha_inicio = Column(DateTime)
    fecha_fin = Column(DateTime)
    descripcion = Column(String(255))

    vacantes = relationship("Vacante", back_populates="contrato")

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

# Tabla Postulados
class Postulado(Base):
    __tablename__ = "postulados"
    id = Column(Integer, primary_key=True)
    vacante_id = Column(Integer, ForeignKey("vacantes.id"))
    artista_id = Column(Integer, ForeignKey("artistas.usuario_id"))
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))

    vacante = relationship("Vacante", back_populates="postulaciones")

# Tabla Categoría
class Categoria(Base):
    __tablename__ = "categorias"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100))

# Tabla Intermedia Contratista - Categoría
class ContratistaCategoria(Base):
    __tablename__ = "contratista_categoria"
    id = Column(Integer, primary_key=True)
    contratista_id = Column(Integer, ForeignKey("usuarios.id"))
    categoria_id = Column(Integer, ForeignKey("categorias.id"))
