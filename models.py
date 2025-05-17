# models.py
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Alumno(Base):
    __tablename__ = "alumnos"

    id = Column(Integer, primary_key=True, index=True)
    dni = Column(String, unique=True, index=True)
    nombre = Column(String)
    apellido = Column(String)
    email = Column(String, unique=True)
    fecha_nacimiento = Column(Date)
    direccion = Column(String, nullable=True)
    telefono = Column(String, nullable=True)
    fecha_inscripcion = Column(Date)
    codigo_alumno = Column(String, unique=True)

    # Relación con la tabla de Inscripciones (si la definimos más adelante)
    # inscripciones = relationship("Inscripcion", back_populates="alumno")
    # Relación con la tabla de Asistencias (si la definimos más adelante)
    # asistencias = relationship("Asistencia", back_populates="alumno")
    # Relación con la tabla de Pagos (si la definimos más adelante)
    # pagos = relationship("Pago", back_populates="alumno")

class Profesor(Base):
    __tablename__ = "profesores"

    id = Column(Integer, primary_key=True, index=True)
    dni = Column(String, unique=True, index=True)
    nombre = Column(String)
    apellido = Column(String)
    email = Column(String, unique=True)
    fecha_nacimiento = Column(Date)
    direccion = Column(String, nullable=True)
    telefono = Column(String, nullable=True)
    codigo_profesor = Column(String, unique=True)
    especialidad = Column(String, nullable=True)

    # Relación con la tabla de Horarios (si la definimos más adelante)
    # horarios = relationship("Horario", back_populates="profesor")