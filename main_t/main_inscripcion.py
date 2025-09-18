from data.base import SessionLocal
from services.inscripcion_service import InscripcionService
from utils.logs_proyect import logger

db = SessionLocal()
service = InscripcionService(db)

def menu_inscripciones():
    while True:
        logger.info("Mostrando menú de inscripciones")
        print("\n Menu Inscripciones")
        print("1. Mostrar Inscripciones")
        print("2. Agregar Inscripción")
        print("3. Buscar Inscripción")
        print("4. Modificar Inscripción")
        print("5. Eliminar Inscripción")
        print("6. Volver al menú principal")
        
        opcion = input("Seleccione una opción: ")

        try:
            if opcion == "1":
                service.mostrar_inscripciones()

            elif opcion == "2":
                service.mostrar_cursos_y_estudiantes()
                estudiante_id = int(input("ID del estudiante: "))
                curso_id = int(input("ID del curso: "))
                fecha_inscripcion = input("Fecha de inscripción (YYYY-MM-DD): ")
                service.agregar_inscripcion(estudiante_id, curso_id, fecha_inscripcion)

            elif opcion == "3":
                inscripcion_id = int(input("ID de la inscripción: "))
                service.buscar_inscripcion(inscripcion_id)

            elif opcion == "4":
                inscripcion_id = int(input("ID de la inscripción: "))
                estudiante_id = int(input("Nuevo ID del estudiante: "))
                curso_id = int(input("Nuevo ID del curso: "))
                fecha_inscripcion = input("Nueva fecha (YYYY-MM-DD): ")
                service.modificar_inscripcion(inscripcion_id, estudiante_id, curso_id, fecha_inscripcion)

            elif opcion == "5":
                inscripcion_id = int(input("ID de la inscripción: "))
                service.eliminar_inscripcion(inscripcion_id)

            elif opcion == "6":
                break
            else:
                logger.warning(f"Opción inválida: {opcion}")
        except Exception as e:
            logger.exception(f"Error en menú de inscripciones: {e}")
            print(f"Ocurrió un error: {e}")