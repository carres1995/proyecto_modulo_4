from data.base import SessionLocal
from services.estudiante_services import EstudianteService
from utils.logs_proyect import logger 
from utils.validators import validar_email as vem, validar_fecha as vfe, validar_identidad as vid, validar_nombres as vno, limpiar_pantalla as clear


db = SessionLocal()
service = EstudianteService(db)

def menu_estudiantes():
    while True:
        clear()
        logger.info("Mostrando menú de estudiantes")
        print("\n Menu Estudiantes")
        print("1. Mostrar Estudiantes")
        print("2. Agregar Estudiante")
        print("3. Buscar Estudiante")
        print("4. Modificar Estudiante")
        print("5. Eliminar Estudiante")
        print("6. Volver al menu principal")
        
        opcion = input("Seleccione una opcion: ")

        try:
            if opcion == "1":
                
                estudiantes = service.mostrar_estudiantes()
                if estudiantes:
                    logger.info(f"Se encontraron {len(estudiantes)} estudiantes")
                    for e in estudiantes:
                        logger.info(f"Estudiante: {e}")
                        print(e)
                else:
                    logger.warning("No hay estudiantes registrados.")
                    raise Exception("No hay estudiantes registrados.")

            elif opcion == "2":
                clear()
                try:
                    numero_identificacion = vid(input("Número de Identificación: "))
                    nombre = vno(input("Nombre: "))
                    apellido = vno(input("Apellido: "))
                    email = vem(input("Email: "))
                    telefono = input("Teléfono: ")
                    fecha_nacimiento = vfe(input("Fecha de Nacimiento (YYYY-MM-DD): "))

                    estudiante = service.agregar_estudiante(numero_identificacion, nombre, apellido, email, telefono, fecha_nacimiento)
                    logger.info("Estudiante agregado correctamente")
                    print("Estudiante agregado correctamente")
                except Exception as e:
                    logger.error(f"Error al agregar estudiante: {e}")
                    raise Exception("Error al agregar estudiante")    

            elif opcion == "3":
                clear()
                try:
                    estudiante_id = int(input("ID del estudiante: "))
                except ValueError:
                    logger.error("ID ingresado no es válido.")
                    continue

                estudiante = service.buscar_estudiante(estudiante_id)
                if estudiante:
                    logger.info(f"Estudiante encontrado: {estudiante}")
                    print(estudiante)
                else:
                    logger.warning(f"No se encontró estudiante con ID {estudiante_id}")

            elif opcion == "4":
                clear()
                try:
                    estudiante_id = int(input("ID del estudiante: "))
                    numero_identificacion = vid(input("Número de Identificación: "))
                    nombre = vno(input("Nombre: "))
                    apellido = vno(input("Apellido: "))
                    email = vem(input("Email: "))
                    telefono = input("Teléfono: ")
                    fecha_nacimiento = vfe(input("Fecha de Nacimiento (YYYY-MM-DD): "))
                except ValueError:
                    logger.error("ID ingresado no es válido.")
                    raise Exception("ID ingresado no es válido.")    

                actualizado = service.modificar_estudiante(estudiante_id, numero_identificacion, nombre, apellido, email, telefono, fecha_nacimiento)
            
                if actualizado:
                    logger.info(f"Estudiante actualizado: {actualizado}")
                    print(actualizado)
                    
                else:
                    logger.warning(f"No se pudo actualizar estudiante con ID {estudiante_id}")
                    

            elif opcion == "5":
                clear()
                try:
                    estudiante_id = int(input("ID del estudiante: "))
                except ValueError:
                    logger.error("ID ingresado no es válido.")
                    continue

                eliminado = service.eliminar_estudiante(estudiante_id)
                if eliminado:
                    logger.info(f"Estudiante con ID {estudiante_id} eliminado.")
                    print("Estudiante eliminado.")
                else:
                    logger.warning(f"No se encontró estudiante con ID {estudiante_id}")

            elif opcion == "6":
                clear()
                logger.info("Saliendo del menú de estudiantes.")
                break

            else:
                logger.warning(f"Opción inválida: {opcion}")

        except Exception as e:
            logger.exception(f"Error inesperado en el menú de estudiantes: {e}")