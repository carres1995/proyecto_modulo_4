from crud.estudiante_crud import get_estudiante, get_estudiantes, create_estudiante, update_estudiante, delete_estudiante
from model.Estudiante import Estudiante
from utils.logs_proyect import logger

class EstudianteService:
    def __init__(self, db):
        self.db = db

    def mostrar_estudiantes(self) -> list:
        logger.info("Listando estudiantes...")
        print("Listando estudiantes...")
        estudiantes = get_estudiantes(self.db)
        return estudiantes if estudiantes is not None else []

    def agregar_estudiante(self, numero_identificacion, nombre, apellido, email, telefono, fecha_nacimiento):
        try:
            email =email
            estudiante = Estudiante(numero_identificacion= numero_identificacion, nombre=nombre, apellido=apellido, email=email, telefono=telefono, fecha_nacimiento= fecha_nacimiento)
            resultado = create_estudiante(self.db, estudiante)
            logger.info(f"Estudiante agregado: {resultado}")
            print("Estudiante agregado exitosamente.")
            return resultado
        except Exception as e:
            logger.error(f"Error al agregar estudiante: {e}")
            raise Exception(f"Error al agregar estudiante: {e}")

    def buscar_estudiante(self, estudiante_id) -> Estudiante | None:
        logger.info(f"Buscando estudiante con ID: {estudiante_id}")
        print(f"Buscando estudiante con ID: {estudiante_id}")
        return get_estudiante(self.db, estudiante_id)

    def modificar_estudiante(self, estudiante_id, numero_identificacion, nombre, apellido, email, telefono, fecha_nacimiento):
        try:
            email = email
            resultado = update_estudiante(self.db, estudiante_id, {"numero_identificacion":numero_identificacion,"nombre": nombre, "apellido": apellido, "email": email, "telefono": telefono, "fecha_nacimiento": fecha_nacimiento})
            logger.info(f"Estudiante modificado: {resultado}")
            print("Estudiante modificado exitosamente.")
            return resultado
        except Exception as e:
            logger.error(f"Error al modificar estudiante: {e}")
            raise Exception(f"Error al modificar estudiante: {e}")

    def eliminar_estudiante(self, estudiante_id) -> int:
        logger.info(f"Eliminando estudiante con ID: {estudiante_id}")
        print(f"Eliminando estudiante con ID: {estudiante_id}")
        return delete_estudiante(self.db, estudiante_id)
