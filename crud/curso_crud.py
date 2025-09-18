from sqlalchemy.orm import Session
from model.Curso import Curso
from view.cursos_view import mostrar_cursos, mostrar_curso
from utils.logs_proyect import logger

def get_curso(db: Session, curso_id: int):
    data = db.query(Curso).filter(Curso.id == curso_id).first()
    if data:
        return mostrar_curso(data)
    else:
        logger.error(f"Curso con ID {curso_id} no encontrado.")
        return None

def get_cursos(db: Session, skip: int = 0, limit: int = 100):
    data = db.query(Curso).offset(skip).limit(limit).all()
    if data:
        return mostrar_cursos(data)
    else:
        logger.error("No se encontraron cursos.")
        return None

def create_curso(db: Session, curso: Curso):
    try:
        db.add(curso)
        db.commit()
        db.refresh(curso)
        logger.info(f"Curso creado con ID: {curso.id}")
        return mostrar_curso(curso) if curso else None
    except Exception as e:
        logger.error(f"Error al crear curso: {e}")
        db.rollback()
        return None

def update_curso(db: Session, curso_id: int, updated_data: dict):
    try:
        curso = db.query(Curso).filter(Curso.id == curso_id).first()
        if not curso:
            logger.error(f"Curso con ID {curso_id} no encontrado para actualización.")
            return None
        for key, value in updated_data.items():
            setattr(curso, key, value)
        db.commit()
        db.refresh(curso)
        logger.info(f"Curso con ID {curso_id} actualizado.")
        return mostrar_curso(curso)
    except Exception as e:
        logger.error(f"Error al actualizar curso: {e}")
        db.rollback()
        return None

def delete_curso(db: Session, curso_id: int):
    try:
        curso = db.query(Curso).filter(Curso.id == curso_id).first()
        if not curso:
            logger.error(f"Curso con ID {curso_id} no encontrado para eliminación.")
            return None
        db.delete(curso)
        db.commit()
        logger.info(f"Curso con ID {curso_id} eliminado.")
        return curso
    except Exception as e:
        logger.error(f"Error al eliminar curso: {e}")
        db.rollback()
        return None