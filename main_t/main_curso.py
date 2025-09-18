from data.base import SessionLocal
from services.curso_service import CursoService
from utils.validators import validar_fecha as vfe, validar_nombres as vno, limpiar_pantalla as clear
from utils.logs_proyect import logger



db = SessionLocal()
service = CursoService(db)

def menu_cursos():
    while True:
        clear()
        logger.info("Mostrando menú de cursos")
        print("\n===== Menú Cursos =====")
        print("1. Mostrar Cursos")
        print("2. Agregar Curso")
        print("3. Buscar Curso")
        print("4. Modificar Curso")
        print("5. Eliminar Curso")
        print("6. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        try:
            if opcion == "1":
                clear()
                cursos = service.mostrar_cursos()
                if cursos:
                    logger.info(f"Se encontraron {len(cursos)} cursos")
                else:
                    logger.warning("No hay cursos registrados.")

            elif opcion == "2":
                clear()
                codigo = input("Código: ")
                nombre = vno(input("Nombre: "))
                descripcion = input("Descripción: ")
                fecha_inicio = vfe(input("Fecha Inicio (YYYY-MM-DD): "))
                fecha_fin = vfe(input("Fecha Fin (YYYY-MM-DD): "))
                docente_id = input("ID del docente (opcional): ")
                docente_id = int(docente_id) if docente_id.strip() else None

                curso = service.agregar_curso(codigo, nombre, descripcion, fecha_inicio, fecha_fin, docente_id)
                if curso:
                    print("Curso agregado correctamente.")

            elif opcion == "3":
                clear()
                curso_id = int(input("ID del curso: "))
                curso = service.buscar_curso(curso_id)
                if curso:
                    print(curso)

            elif opcion == "4":
                clear()
                curso_id = int(input("ID del curso: "))
                codigo = input("Código: ")
                nombre = vno(input("Nombre: "))
                descripcion = input("Descripción: ")
                fecha_inicio = vfe(input("Fecha Inicio (YYYY-MM-DD): "))
                fecha_fin = vfe(input("Fecha Fin (YYYY-MM-DD): "))
                docente_id = input("ID del docente (opcional): ")
                docente_id = int(docente_id) if docente_id.strip() else None

                actualizado = service.modificar_curso(curso_id, codigo, nombre, descripcion, fecha_inicio, fecha_fin, docente_id)
                if actualizado:
                    print("Curso actualizado correctamente.")

            elif opcion == "5":
                clear()
                curso_id = int(input("ID del curso: "))
                eliminado = service.eliminar_curso(curso_id)
                if eliminado:
                    print("Curso eliminado correctamente.")

            elif opcion == "6":
                clear()
                logger.info("Saliendo del menú de cursos")
                break

            else:
                logger.warning(f"Opción inválida: {opcion}")
                print("Opción inválida, intente nuevamente.")
        except Exception as e:
            logger.exception(f"Error inesperado en el menú de cursos: {e}")
            print(f"Ocurrió un error: {e}")
