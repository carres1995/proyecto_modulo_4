from sqlalchemy.orm import Session
from model.Inscripcion import Inscripcion
from model.Curso import Curso
from model.Estudiante import Estudiante
from utils.logs_proyect import logger
from view.inscripciones_view import mostrar_inscripcion, mostrar_inscripciones, mostrar_cursos_docentes

def get_inscripcion(db: Session, inscripcion_id: int):
    data = db.query(Inscripcion).filter(Inscripcion.id == inscripcion_id).first()
    if data:
        return mostrar_inscripcion(data)
    else:
        logger.error(f"Inscripción con ID {inscripcion_id} no encontrada.")
        return None
def get_cursos_and_estudiantes(db: Session):
    cursos = db.query(Curso).all()
    estudiantes = db.query(Estudiante).all()
    return mostrar_cursos_docentes(cursos, estudiantes)

def get_inscripciones(db: Session, skip: int = 0, limit: int = 100):
    data = db.query(Inscripcion).offset(skip).limit(limit).all()
    if data:
        return mostrar_inscripciones(data)
    else:
        logger.error("No se encontraron inscripciones.")
        return None

def create_inscripcion(db: Session, inscripcion: Inscripcion):
    try:
        db.add(inscripcion)
        db.commit()
        db.refresh(inscripcion)
        logger.info(f"Inscripción creada con ID: {inscripcion.id}")
        return mostrar_inscripcion(inscripcion)
    except Exception as e:
        logger.error(f"Error al crear inscripción: {e}")
        db.rollback()
        return None

def update_inscripcion(db: Session, inscripcion_id: int, updated_data: dict):
    try:
        inscripcion = db.query(Inscripcion).filter(Inscripcion.id == inscripcion_id).first()
        if not inscripcion:
            logger.error(f"Inscripción con ID {inscripcion_id} no encontrada.")
            return None

        for key, value in updated_data.items():
            setattr(inscripcion, key, value)
        db.commit()
        db.refresh(inscripcion)
        logger.info(f"Inscripción con ID {inscripcion_id} actualizada.")
        return mostrar_inscripcion(inscripcion)
    except Exception as e:
        logger.error(f"Error al actualizar inscripción: {e}")
        db.rollback()
        return None

def delete_inscripcion(db: Session, inscripcion_id: int):
    try:
        inscripcion = db.query(Inscripcion).filter(Inscripcion.id == inscripcion_id).first()
        if not inscripcion:
            logger.error(f"Inscripción con ID {inscripcion_id} no encontrada.")
            return None

        db.delete(inscripcion)
        db.commit()
        logger.info(f"Inscripción con ID {inscripcion_id} eliminada.")
        return inscripcion
    except Exception as e:
        logger.error(f"Error al eliminar inscripción: {e}")
        db.rollback()
        return None
