# main.py
from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import models, schemas
from .database import SessionLocal, engine, create_tables

create_tables()

app = FastAPI()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoint para crear un nuevo alumno
@app.post("/alumnos/", response_model=schemas.Alumno)
def create_alumno(alumno: schemas.AlumnoCreate, db: Session = Depends(get_db)):
    db_alumno = db.query(models.Alumno).filter(models.Alumno.dni == alumno.dni).first()
    if db_alumno:
        raise HTTPException(status_code=400, detail="Alumno con este DNI ya existe")
    db_alumno_email = db.query(models.Alumno).filter(models.Alumno.email == alumno.email).first()
    if db_alumno_email:
        raise HTTPException(status_code=400, detail="Alumno con este correo electrónico ya existe")
    db_alumno_codigo = db.query(models.Alumno).filter(models.Alumno.codigo_alumno == alumno.codigo_alumno).first()
    if db_alumno_codigo:
        raise HTTPException(status_code=400, detail="Alumno con este código ya existe")
    db_alumno = models.Alumno(**alumno.dict())
    db.add(db_alumno)
    db.commit()
    db.refresh(db_alumno)
    return db_alumno

# Endpoint para obtener todos los alumnos
@app.get("/alumnos/", response_model=List[schemas.Alumno])
def read_alumnos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    alumnos = db.query(models.Alumno).offset(skip).limit(limit).all()
    return alumnos

# Endpoint para obtener un alumno por su ID
@app.get("/alumnos/{alumno_id}", response_model=schemas.Alumno)
def read_alumno(alumno_id: int, db: Session = Depends(get_db)):
    db_alumno = db.query(models.Alumno).filter(models.Alumno.id == alumno_id).first()
    if db_alumno is None:
        raise HTTPException(status_code=404, detail="Alumno no encontrado")
    return db_alumno

# Endpoint para crear un nuevo profesor
@app.post("/profesores/", response_model=schemas.Profesor)
def create_profesor(profesor: schemas.ProfesorCreate, db: Session = Depends(get_db)):
    db_profesor = db.query(models.Profesor).filter(models.Profesor.dni == profesor.dni).first()
    if db_profesor:
        raise HTTPException(status_code=400, detail="Profesor con este DNI ya existe")
    db_profesor_email = db.query(models.Profesor).filter(models.Profesor.email == profesor.email).first()
    if db_profesor_email:
        raise HTTPException(status_code=400, detail="Profesor con este correo electrónico ya existe")
    db_profesor_codigo = db.query(models.Profesor).filter(models.Profesor.codigo_profesor == profesor.codigo_profesor).first()
    if db_profesor_codigo:
        raise HTTPException(status_code=400, detail="Profesor con este código ya existe")
    db_profesor = models.Profesor(**profesor.dict())
    db.add(db_profesor)
    db.commit()
    db.refresh(db_profesor)
    return db_profesor

# Endpoint para obtener todos los profesores
@app.get("/profesores/", response_model=List[schemas.Profesor])
def read_profesores(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    profesores = db.query(models.Profesor).offset(skip).limit(limit).all()
    return profesores

# Endpoint para obtener un profesor por su ID
@app.get("/profesores/{profesor_id}", response_model=schemas.Profesor)
def read_profesor(profesor_id: int, db: Session = Depends(get_db)):
    db_profesor = db.query(models.Profesor).filter(models.Profesor.id == profesor_id).first()
    if db_profesor is None:
        raise HTTPException(status_code=404, detail="Profesor no encontrado")
    return db_profesor