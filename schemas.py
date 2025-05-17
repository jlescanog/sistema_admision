# schemas.py
from typing import Optional
from datetime import date

from pydantic import BaseModel

class AlumnoBase(BaseModel):
    dni: str
    nombre: str
    apellido: str
    email: str
    fecha_nacimiento: date
    direccion: Optional[str] = None
    telefono: Optional[str] = None
    fecha_inscripcion: date
    codigo_alumno: str

class AlumnoCreate(AlumnoBase):
    pass

class Alumno(AlumnoBase):
    id: int

    class Config:
        orm_mode = True

class ProfesorBase(BaseModel):
    dni: str
    nombre: str
    apellido: str
    email: str
    fecha_nacimiento: date
    direccion: Optional[str] = None
    telefono: Optional[str] = None
    codigo_profesor: str
    especialidad: Optional[str] = None

class ProfesorCreate(ProfesorBase):
    pass

class Profesor(ProfesorBase):
    id: int

    class Config:
        orm_mode = True