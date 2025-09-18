from crud.docente_crud import get_docente, get_docentes, create_docente, update_docente, delete_docente
from model.Docente import Docente
from utils.logs_proyect import logger

class DocenteService:
    def __init__(self, db):
        self.db = db

    def mostrar_docentes(self) -> list:
        logger.info("Listando docentes...")
        docentes = get_docentes(self.db)
        return docentes if docentes is not None else []

    def agregar_docente(self, numero_identificacion, nombre, apellido, email, telefono, especialidad):
        try:
            docente = Docente(
                numero_identificacion=numero_identificacion,
                nombre=nombre,
                apellido=apellido,
                email=email,
                telefono=telefono,
                especialidad=especialidad
            )
            return create_docente(self.db, docente)
        except Exception as e:
            logger.error(f"Error al agregar docente: {e}")
            raise 

    def buscar_docente(self, docente_id):
        return get_docente(self.db, docente_id)

    def modificar_docente(self, docente_id, numero_identificacion, nombre, apellido, email, telefono, especialidad):
        data= {
            "numero_identificacion": numero_identificacion,
            "nombre": nombre,
            "apellido": apellido,
            "email": email,
            "telefono": telefono,
            "especialidad": especialidad
        }
        return update_docente(self.db, docente_id, data)   

    def eliminar_docente(self, docente_id):
        return delete_docente(self.db, docente_id)
