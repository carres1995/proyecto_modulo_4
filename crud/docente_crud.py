from sqlalchemy.orm import Session
from model.Docente import Docente
from view.docentes_view import mostrar_docentes, mostrar_docente
from utils.logs_proyect import logger


def get_docente(db: Session, docente_id: int):
    data = db.query(Docente).filter(Docente.id == docente_id).first()
    if data:
        return mostrar_docente(data)
    else:
        logger.error(f"Docente con ID {docente_id} no encontrado.")
        return None


def get_docentes(db: Session, skip: int = 0, limit: int = 100):
    data = db.query(Docente).offset(skip).limit(limit).all()
    if data:
        return mostrar_docentes(data)
    else:
        logger.error("No se encontraron docentes.")
        return None


def create_docente(db: Session, docente: Docente):
    try:
        db.add(docente)
        db.commit()
        db.refresh(docente)
        logger.info(f"Docente creado con ID: {docente.id}")
        if docente:
            return mostrar_docente(docente)
        else:
            logger.error("Error al crear el docente.")
            return None
    except Exception as e:
        logger.error(f"Error al crear docente: {e}")
        db.rollback()
        return None


def update_docente(db: Session, docente_id: int, updated_data: dict):
    try:
        docente = db.query(Docente).filter(Docente.id == docente_id).first()
        if not docente:
            logger.error(f"Docente con ID {docente_id} no encontrado para actualización.")
            return None
        for key, value in updated_data.items():
            setattr(docente, key, value)
        db.commit()
        db.refresh(docente)
        logger.info(f"Docente con ID {docente_id} actualizado.")
        return mostrar_docente(docente)
    except Exception as e:
        logger.error(f"Error al actualizar docente: {e}")
        db.rollback()
        return None


def delete_docente(db: Session, docente_id: int):
    try:
        docente = db.query(Docente).filter(Docente.id == docente_id).first()
        if not docente:
            logger.error(f"Docente con ID {docente_id} no encontrado para eliminación.")
            return None
        db.delete(docente)
        db.commit()
        logger.info(f"Docente con ID {docente_id} eliminado.")
        return docente
    except Exception as e:
        logger.error(f"Error al eliminar docente: {e}")
        db.rollback()
        return None
