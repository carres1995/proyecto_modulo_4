from sqlalchemy.orm import Session
from model.Inscripcion import Inscripcion
from model.Curso import Curso
from model.Estudiante import Estudiante
from utils.logs_proyect import logger

def get_inscripciones(db: Session, skip: int = 0, limit: int = 100):
    try:
        return db.query(Inscripcion).offset(skip).limit(limit).all()
    except Exception as e:
        logger.error(f"Error al obtener inscripciones: {e}")
        return []

def get_inscripcion(db: Session, inscripcion_id: int):
    return db.query(Inscripcion).filter(Inscripcion.id == inscripcion_id).first()

def get_cursos_and_estudiantes(db: Session):
    try:
        cursos = db.query(Curso).all()
        estudiantes = db.query(Estudiante).all()
        return cursos, estudiantes
    except Exception as e:
        logger.error(f"Error al obtener cursos y estudiantes: {e}")
        return [], []

def create_inscripcion(db: Session, inscripcion: Inscripcion):
    try:
        db.add(inscripcion)
        db.commit()
        db.refresh(inscripcion)
        return inscripcion
    except Exception as e:
        logger.error(f"Error al crear inscripción: {e}")
        db.rollback()
        return None

def update_inscripcion(db: Session, inscripcion_id: int, data: dict):
    inscripcion = get_inscripcion(db, inscripcion_id)
    if not inscripcion:
        return None
    try:
        for key, value in data.items():
            setattr(inscripcion, key, value)
        db.commit()
        db.refresh(inscripcion)
        return inscripcion
    except Exception as e:
        logger.error(f"Error al actualizar inscripción: {e}")
        db.rollback()
        return None

def delete_inscripcion(db: Session, inscripcion_id: int):
    inscripcion = get_inscripcion(db, inscripcion_id)
    if not inscripcion:
        return None
    try:
        db.delete(inscripcion)
        db.commit()
        return inscripcion_id
    except Exception as e:
        logger.error(f"Error al eliminar inscripción: {e}")
        db.rollback()
        return None
