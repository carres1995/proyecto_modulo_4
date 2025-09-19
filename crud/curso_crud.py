from sqlalchemy.orm import Session
from sqlalchemy import func
from model.Curso import Curso
from view.cursos_view import mostrar_cursos, mostrar_curso
from utils.logs_proyect import logger


def get_curso(db: Session, curso_id: int):
    """Obtiene un curso por su ID"""
    data = db.query(Curso).filter(Curso.id == curso_id).first()
    if data:
        return mostrar_curso(data)
    else:
        logger.error(f"Curso con ID {curso_id} no encontrado.")
        return None


def get_cursos(db: Session, skip: int = 0, limit: int = 100):
    """Obtiene todos los cursos con paginación opcional"""
    data = db.query(Curso).offset(skip).limit(limit).all()
    if data:
        return mostrar_cursos(data)
    else:
        logger.error("No se encontraron cursos.")
        return None


def create_curso(db: Session, curso: Curso):
    """Crea un nuevo curso en la base de datos"""
    try:
        db.add(curso)
        db.commit()
        db.refresh(curso)
        logger.info(f"Curso creado con ID: {curso.id}")
        return mostrar_curso(curso)
    except Exception as e:
        logger.error(f"Error al crear curso: {e}")
        db.rollback()
        return None


def update_curso(db: Session, curso_id: int, updated_data: dict):
    """Actualiza un curso existente por su ID"""
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
    """Elimina un curso por su ID"""
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
    
def buscar_curso_por_nombre(db: Session, nombre: str):
    curso = db.query(Curso).filter(Curso.nombre == nombre).first()
    if curso:
        logger.info(f"Curso encontrado con nombre: {nombre}")
        return mostrar_curso(curso)
    else:
        logger.error(f"No se encontró curso con el nombre: {nombre}")
        return None

def contar_cursos(db: Session):
    return db.query(func.count(Curso.id)).scalar()    