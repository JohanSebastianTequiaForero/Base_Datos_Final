#enum: Tipo de dato personalizado
#uso: Restringir variables
#     solo algunos valores
from enum import Enum

class TipoDocumento(Enum):
    CC = "Cédula de Ciudadanía"
    CE = "Cédula de Extranjería"
    TI = "Tarjeta de Identidad"
    PASAPORTE = "Pasaporte"
    NIT = "Número de Identificación Tributaria"
  