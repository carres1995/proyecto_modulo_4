from crud.estudiante_crud import get_estudiante, get_estudiantes, create_estudiante, update_estudiante, delete_estudiante
from model.Estudiante import Estudiante
from utils.logs_proyect import logger

class EstudianteService:
    def __init__(self, db):
        self.db = db

    def mostrar_estudiantes(self):
        logger.info("Listando estudiantes...")
        estudiantes = get_estudiantes(self.db)
        return estudiantes if estudiantes else []

    def agregar_estudiante(self, numero_identificacion, nombre, apellido, email, telefono, fecha_nacimiento):
        try:
            estudiante = Estudiante(
                numero_identificacion=numero_identificacion,
                nombre=nombre,
                apellido=apellido,
                email=email,
                telefono=telefono,
                fecha_nacimiento=fecha_nacimiento
            )
            return create_estudiante(self.db, estudiante)
        except Exception as e:
            logger.error(f"Error al agregar estudiante: {e}")
            raise

    def buscar_estudiante(self, estudiante_id):
        return get_estudiante(self.db, estudiante_id)

    def modificar_estudiante(self, estudiante_id, numero_identificacion, nombre, apellido, email, telefono, fecha_nacimiento):
        data = {
            "numero_identificacion": numero_identificacion,
            "nombre": nombre,
            "apellido": apellido,
            "email": email,
            "telefono": telefono,
            "fecha_nacimiento": fecha_nacimiento
        }
        return update_estudiante(self.db, estudiante_id, data)

    def eliminar_estudiante(self, estudiante_id):
        return delete_estudiante(self.db, estudiante_id)