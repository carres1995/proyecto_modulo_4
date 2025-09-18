from data.base import Base, engine
from utils.logs_proyect import logger

# 🔹 Importar modelos aquí para registrar las tablas
from model.Estudiante import Estudiante
from model.Curso import Curso
from model.Docente import Docente
from model.Inscripcion import Inscripcion
from model.estu_curso import estudiante_curso  # si es tabla intermedia

def init_db():
    try:
        Base.metadata.create_all(bind=engine)
        logger.info("Tablas verificadas/creadas correctamente.")
    except Exception as e:
        logger.error(f"Error al crear/verificar tablas: {e}")
        raise Exception("Error al crear/verificar tablas")
