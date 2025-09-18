from sqlalchemy.orm import Session
from model.Estudiante import Estudiante
from view.estudiantes_view import mostrar_estudiantes, mostrar_estudiante
from utils.logs_proyect import logger

def get_estudiante(db: Session, estudiante_id: int):
    data = db.query(Estudiante).filter(Estudiante.id == estudiante_id).first()
    if data:
        return mostrar_estudiante(data)
    else:
        logger.error(f"Estudiante con ID {estudiante_id} no encontrado.")
        return None

def get_estudiantes(db: Session, skip: int = 0, limit: int = 100):
    data=db.query(Estudiante).offset(skip).limit(limit).all()
    if data:
        return mostrar_estudiantes(data)
    else:
        logger.error("No se encontraron estudiantes.")
        return None
        
def create_estudiante(db: Session, estudiante: Estudiante):
    try:
        db.add(estudiante)
        db.commit()
        db.refresh(estudiante)
        logger.info(f"Estudiante creado con ID: {estudiante.id}")
        if estudiante:
            return mostrar_estudiante(estudiante)
        else:
            logger.error("Error al crear el estudiante.")
            return None
    except Exception as e:
        logger.error(f"Error al crear estudiante: {e}")
        db.rollback()
        return None

def update_estudiante(db: Session, estudiante_id: int, updated_data: dict):
    try:
        estudiante = db.query(Estudiante).filter(Estudiante.id == estudiante_id).first()
        if not estudiante:
            logger.error(f"Estudiante con ID {estudiante_id} no encontrado para actualización.")
            return None
        for key, value in updated_data.items():
            setattr(estudiante, key, value)
        db.commit()
        db.refresh(estudiante)
        logger.info(f"Estudiante con ID {estudiante_id} actualizado.")
        return mostrar_estudiante(estudiante)
    except Exception as e:
        logger.error(f"Error al actualizar estudiante: {e}")
        db.rollback()
        return None

def delete_estudiante(db: Session, estudiante_id: int):
    try:
        estudiante = db.query(Estudiante).filter(Estudiante.id == estudiante_id).first()
        if not estudiante:
            logger.error(f"Estudiante con ID {estudiante_id} no encontrado para eliminación.")
            return None
        db.delete(estudiante)
        db.commit()
        logger.info(f"Estudiante con ID {estudiante_id} eliminado.")
        return estudiante
    except Exception as e:
        logger.error(f"Error al eliminar estudiante: {e}")
        db.rollback()
        return None
