from sqlalchemy.orm import Session
from model.Estudiante import Estudiante
from utils.logs_proyect import logger

def get_estudiantes(db: Session, skip: int = 0, limit: int = 100):
    try:
        return db.query(Estudiante).offset(skip).limit(limit).all()
    except Exception as e:
        logger.error(f"Error al obtener estudiantes: {e}")
        return []

def get_estudiante(db: Session, estudiante_id: int):
    return db.query(Estudiante).filter(Estudiante.id == estudiante_id).first()

def create_estudiante(db: Session, estudiante: Estudiante):
    db.add(estudiante)
    db.commit()
    db.refresh(estudiante)
    return estudiante

def update_estudiante(db: Session, estudiante_id: int, data: dict):
    estudiante = get_estudiante(db, estudiante_id)
    if not estudiante:
        return None
    for key, value in data.items():
        setattr(estudiante, key, value)
    db.commit()
    db.refresh(estudiante)
    return estudiante

def delete_estudiante(db: Session, estudiante_id: int):
    estudiante = get_estudiante(db, estudiante_id)
    if not estudiante:
        return None
    db.delete(estudiante)
    db.commit()
    return estudiante_id