from sqlalchemy.orm import Session
from model.Docente import Docente
from utils.logs_proyect import logger


def get_docentes(db: Session, skip: int = 0, limit: int = 100):
    try:
        return db.query(Docente).offset(skip).limit(limit).all()
    except Exception as e:
        logger.error(f"Error al obtener docentes: {e}")
        return []

def get_docente(db: Session, docente_id: int):
    return db.query(Docente).filter(Docente.id == docente_id).first()


def create_docente(db: Session, docente: Docente):
        db.add(docente)
        db.commit()
        db.refresh(docente)
        logger.info(f"Docente creado con ID: {docente.id}")
        return docente
    


def update_docente(db: Session, docente_id: int, updated_data: dict):
    docente = get_docente(db, docente_id)
    if not docente:
        return None
    for key, value in updated_data.items():
        setattr(docente, key, value)
    db.commit()
    db.refresh(docente)
    return docente


def delete_docente(db: Session, docente_id: int):
    docente = db.query(Docente).filter(Docente.id == docente_id).first()
    if not docente:
        return None
    db.delete(docente)
    db.commit()
    return docente_id
   
