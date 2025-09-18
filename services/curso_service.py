from crud.curso_crud import get_curso, get_cursos, create_curso, update_curso, delete_curso
from model.Curso import Curso
from model.Docente import Docente
from utils.logs_proyect import logger

class CursoService:
    def __init__(self, db):
        self.db = db

    def mostrar_cursos(self) -> list:
        logger.info("Listando cursos...")
        print("Listando cursos...")
        cursos = get_cursos(self.db)
        return cursos if cursos is not None else []

    def agregar_curso(self, codigo, nombre, descripcion, fecha_inicio, fecha_fin, docente_id=None):
        try:
            curso = Curso(
                codigo=codigo,
                nombre=nombre,
                descripcion=descripcion,
                fecha_inicio=fecha_inicio,
                fecha_fin=fecha_fin
            )

            # Asociar docente si se pasa el ID
            if docente_id:
                docente = self.db.query(Docente).filter(Docente.id == docente_id).first()
                if not docente:
                    logger.error(f"No existe docente con ID {docente_id}")
                    raise Exception(f"No existe docente con ID {docente_id}")
                curso.docente = docente

            resultado = create_curso(self.db, curso)
            logger.info(f"Curso agregado: {resultado}")
            print(f"Curso agregado: {resultado}")
            return resultado
        except Exception as e:
            logger.error(f"Error al agregar curso: {e}")
            raise Exception(f"Error al agregar curso: {e}")

    def buscar_curso(self, curso_id) -> Curso | None:
        logger.info(f"Buscando curso con ID: {curso_id}")
        print(f"Buscando curso con ID: {curso_id}")
        return get_curso(self.db, curso_id)

    def modificar_curso(self, curso_id, codigo, nombre, descripcion, fecha_inicio, fecha_fin, docente_id=None):
        try:
            data_update = {
                "codigo": codigo,
                "nombre": nombre,
                "descripcion": descripcion,
                "fecha_inicio": fecha_inicio,
                "fecha_fin": fecha_fin
            }

            curso = self.db.query(Curso).filter(Curso.id == curso_id).first()
            if not curso:
                logger.error(f"Curso con ID {curso_id} no encontrado.")
                raise Exception(f"Curso con ID {curso_id} no encontrado.")

            # Actualizar docente si se pasa un ID
            if docente_id:
                docente = self.db.query(Docente).filter(Docente.id == docente_id).first()
                if not docente:
                    logger.error(f"No existe docente con ID {docente_id}")
                    raise Exception(f"No existe docente con ID {docente_id}")
                curso.docente = docente

            resultado = update_curso(self.db, curso_id, data_update)
            logger.info(f"Curso modificado: {resultado}")
            print(f"Curso modificado: {resultado}")
            return resultado
        except Exception as e:
            logger.error(f"Error al modificar curso: {e}")
            raise Exception(f"Error al modificar curso: {e}")

    def eliminar_curso(self, curso_id) -> int:
        logger.info(f"Eliminando curso con ID: {curso_id}")
        print(f"Eliminando curso con ID: {curso_id}")
        return delete_curso(self.db, curso_id)
