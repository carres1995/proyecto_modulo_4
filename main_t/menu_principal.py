from utils.logs_proyect import logger
from data.init_db import init_db
from main_t.main_estudiante import menu_estudiantes
from main_t.main_docente import menu_docentes
from main_t.main_curso import menu_cursos
from main_t.main_inscripcion import menu_inscripciones
from utils.validators import limpiar_pantalla as clear

def menu_principal():
    while True:
        clear()
        print("\n===== MENÚ PRINCIPAL =====")
        print("1. Gestión de Estudiantes")
        print("2. Gestión de Docentes")
        print("3. Gestión de Cursos")
        print("4. Gestión de Inscripciones")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        try:
            if opcion == "1":
                clear()
                logger.info("Entrando al menú de estudiantes")
                menu_estudiantes()
            elif opcion == "2":
                clear()
                logger.info("Entrando al menú de docentes")
                menu_docentes()
            elif opcion == "3":
                clear()
                logger.info("Entrando al menú de cursos")
                menu_cursos()
            elif opcion == "4":
                clear()
                logger.info("Entrando al menú de inscripciones")
                menu_inscripciones()
            elif opcion == "5":
                clear()
                logger.info("Saliendo de la aplicación...")
                print("Hasta luego 👋")
                break
            else:
                logger.warning(f"Opción inválida seleccionada: {opcion}")
                print("Opción inválida, intente nuevamente.")
        except Exception as e:
            logger.error(f"Error en el menú principal: {e}")
            print(f"Ocurrió un error: {e}")