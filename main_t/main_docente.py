from data.base import SessionLocal
from services.docente_service import DocenteService
from utils.logs_proyect import logger
from utils.validators import validar_email as vem, validar_nombres as vno, validar_fecha as vfe, validar_identidad as vid


db = SessionLocal()
service = DocenteService(db)

def menu_docentes():
    while True:
        logger.info("Mostrando menú de docentes")
        print("\n Menu Docentes")
        print("1. Mostrar Docentes")
        print("2. Agregar Docente")
        print("3. Buscar Docente")
        print("4. Modificar Docente")
        print("5. Eliminar Docente")
        print("6. Volver al menú principal")
        
        opcion = input("Seleccione una opción: ")

        try:
            if opcion == "1":
                docentes = service.mostrar_docentes()
                if docentes:
                    logger.info(f"Se encontraron {len(docentes)} docentes")
                    for d in docentes:
                        logger.info(f"Docente: {d}")
                        print(d)
                else:
                    logger.warning("No hay docentes registrados.")
                    raise Exception("No hay docentes registrados.")

            elif opcion == "2":
                try:
                    numero_identificacion = vid(input("Número de Identificación: "))
                    nombre = vno(input("Nombre: "))
                    apellido = vno(input("Apellido: "))
                    email = vem(input("Email: "))
                    telefono = input("Teléfono: ")
                    especialidad = input("Especialidad: ")

                    docente = service.agregar_docente(
                        numero_identificacion, nombre, apellido, email, telefono, especialidad
                    )
                    logger.info("Docente agregado correctamente")
                    print("Docente agregado correctamente")
                except Exception as e:
                    logger.error(f"Error al agregar docente: {e}")
                    raise Exception("Error al agregar docente")    

            elif opcion == "3":
                try:
                    docente_id = int(input("ID del docente: "))
                except ValueError:
                    logger.error("ID ingresado no es válido.")
                    continue

                docente = service.buscar_docente(docente_id)
                if docente:
                    logger.info(f"Docente encontrado: {docente}")
                    print(docente)
                else:
                    logger.warning(f"No se encontró docente con ID {docente_id}")

            elif opcion == "4":
                try:
                    docente_id = int(input("ID del docente: "))
                    numero_identificacion = vid(input("Número de Identificación: "))
                    nombre = vno(input("Nombre: "))
                    apellido = vno(input("Apellido: "))
                    email = vem(input("Email: "))
                    telefono = input("Teléfono: ")
                    especialidad = input("Especialidad: ")
                except ValueError:
                    logger.error("ID ingresado no es válido.")
                    raise Exception("ID ingresado no es válido.")    

                actualizado = service.modificar_docente(
                    docente_id, numero_identificacion, nombre, apellido, email, telefono, especialidad
                )
            
                if actualizado:
                    logger.info(f"Docente actualizado: {actualizado}")
                    print(actualizado)
                else:
                    logger.warning(f"No se pudo actualizar docente con ID {docente_id}")

            elif opcion == "5":
                try:
                    docente_id = int(input("ID del docente: "))
                except ValueError:
                    logger.error("ID ingresado no es válido.")
                    continue

                eliminado = service.eliminar_docente(docente_id)
                if eliminado:
                    logger.info(f"Docente con ID {docente_id} eliminado.")
                    print("Docente eliminado.")
                else:
                    logger.warning(f"No se encontró docente con ID {docente_id}")

            elif opcion == "6":
                logger.info("Saliendo del menú de docentes.")
                break

            else:
                logger.warning(f"Opción inválida: {opcion}")

        except Exception as e:
            logger.exception(f"Error inesperado en el menú de docentes: {e}")
