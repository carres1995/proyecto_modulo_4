from crud.inscripcion_crud import (
    get_inscripcion,
    get_inscripciones,
    create_inscripcion,
    update_inscripcion,
    delete_inscripcion,
    get_cursos_and_estudiantes
)
from model.Inscripcion import Inscripcion
from utils.logs_proyect import logger

class InscripcionService:
    def __init__(self, db):
        self.db = db

    def mostrar_inscripciones(self):
        logger.info("Listando inscripciones...")
        inscripciones = get_inscripciones(self.db)
        return inscripciones if inscripciones else []

    def agregar_inscripcion(self, estudiante_id, curso_id, fecha_inscripcion):
        try:
            inscripcion = Inscripcion(
                estudiante_id=estudiante_id,
                curso_id=curso_id,
                fecha_inscripcion=fecha_inscripcion
            )
            return create_inscripcion(self.db, inscripcion)
        except Exception as e:
            logger.error(f"Error al agregar inscripción: {e}")
            raise

    def buscar_inscripcion(self, inscripcion_id):
        return get_inscripcion(self.db, inscripcion_id)

    def modificar_inscripcion(self, inscripcion_id, estudiante_id, curso_id, fecha_inscripcion):
        data = {
            "estudiante_id": estudiante_id,
            "curso_id": curso_id,
            "fecha_inscripcion": fecha_inscripcion
        }
        return update_inscripcion(self.db, inscripcion_id, data)

    def eliminar_inscripcion(self, inscripcion_id):
        return delete_inscripcion(self.db, inscripcion_id)

    def obtener_cursos_y_estudiantes(self):
        logger.info("Obteniendo cursos y estudiantes...")
        cursos, estudiantes = get_cursos_and_estudiantes(self.db)
        return cursos, estudiantes