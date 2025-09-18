from crud.docente_crud import get_docente, get_docentes, create_docente, update_docente, delete_docente
from model.Docente import Docente
from utils.validators import validar_email
from utils.logs_proyect import logger

class DocenteService:
    def __init__(self, db):
        self.db = db

    def mostrar_docentes(self) -> list:
        logger.info("Listando docentes...")
        print("Listando docentes...")
        docentes = get_docentes(self.db)
        return docentes if docentes is not None else []

    def agregar_docente(self, numero_identificacion, nombre, apellido, email, telefono, especialidad):
        try:
            email = validar_email(email)
            docente = Docente(
                numero_identificacion=numero_identificacion,
                nombre=nombre,
                apellido=apellido,
                email=email,
                telefono=telefono,
                especialidad=especialidad
            )
            resultado = create_docente(self.db, docente)
            logger.info(f"Docente agregado: {resultado}")
            print(f"Docente agregado: {resultado}")
            return resultado
        except Exception as e:
            logger.error(f"Error al agregar docente: {e}")
            raise Exception(f"Error al agregar docente: {e}")

    def buscar_docente(self, docente_id) -> Docente | None:
        logger.info(f"Buscando docente con ID: {docente_id}")
        print(f"Buscando docente con ID: {docente_id}")
        return get_docente(self.db, docente_id)

    def modificar_docente(self, docente_id, numero_identificacion, nombre, apellido, email, telefono, especialidad):
        try:
            email = validar_email(email)
            resultado = update_docente(
                self.db,
                docente_id,
                {
                    "numero_identificacion": numero_identificacion,
                    "nombre": nombre,
                    "apellido": apellido,
                    "email": email,
                    "telefono": telefono,
                    "especialidad": especialidad
                }
            )
            logger.info(f"Docente modificado: {resultado}")
            print(f"Docente modificado: {resultado}")
            return resultado
        except Exception as e:
            logger.error(f"Error al modificar docente: {e}")
            raise Exception(f"Error al modificar docente: {e}")

    def eliminar_docente(self, docente_id) -> int:
        logger.info(f"Eliminando docente con ID: {docente_id}")
        print(f"Eliminando docente con ID: {docente_id}")
        return delete_docente(self.db, docente_id)
