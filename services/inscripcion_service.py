from crud.inscripcion_crud import get_inscripcion, get_inscripciones, create_inscripcion, update_inscripcion, delete_inscripcion, get_cursos_and_estudiantes
from model.Inscripcion import Inscripcion
from utils.logs_proyect import logger

class InscripcionService:
    def __init__(self, db):
        self.db = db

    def mostrar_inscripciones(self):
        logger.info("Listando inscripciones...")
        print("Listando inscripciones...")
        return get_inscripciones(self.db) or []

    def mostrar_cursos_y_estudiantes(self):
        logger.info("Listando cursos y estudiantes...")
        print("Listando cursos y estudiantes...")
        return get_cursos_and_estudiantes(self.db)

    def agregar_inscripcion(self, estudiante_id, curso_id, fecha_inscripcion):
        try:
            inscripcion = Inscripcion(
                estudiante_id=estudiante_id,
                curso_id=curso_id,
                fecha_inscripcion=fecha_inscripcion
            )
            logger.info(f"Agregando inscripción: {inscripcion}")
            print("Agregando inscripción...")
            return create_inscripcion(self.db, inscripcion)
        except Exception as e:
            logger.error(f"Error al agregar inscripción: {e}")
            raise

    def buscar_inscripcion(self, inscripcion_id):
        logger.info(f"Buscando inscripción con ID: {inscripcion_id}")
        print(f"Buscando inscripción con ID: {inscripcion_id}")
        return get_inscripcion(self.db, inscripcion_id)

    def modificar_inscripcion(self, inscripcion_id, estudiante_id, curso_id, fecha_inscripcion):
        try:
            logger.info(f"Modificando inscripción con ID: {inscripcion_id}")
            print(f"Modificando inscripción con ID: {inscripcion_id}")
            return update_inscripcion(
                self.db, inscripcion_id,
                {"estudiante_id": estudiante_id, "curso_id": curso_id, "fecha_inscripcion": fecha_inscripcion}
            )
        except Exception as e:
            logger.error(f"Error al modificar inscripción: {e}")
            raise

    def eliminar_inscripcion(self, inscripcion_id):
        logger.info(f"Eliminando inscripción con ID: {inscripcion_id}")
        print(f"Eliminando inscripción con ID: {inscripcion_id}")
        return delete_inscripcion(self.db, inscripcion_id)
