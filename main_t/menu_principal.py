from utils.logs_proyect import logger
from data.init_db import init_db
from main_t.main_estudiante import menu_estudiantes
from main_t.main_docente import menu_docentes
from main_t.main_curso import menu_cursos
from main_t.main_inscripcion import menu_inscripciones
from utils.decorators import manejar_errores

@manejar_errores
def menu_principal():
    while True:
        print("\n===== MENU PRINCIPAL =====")
        print("1. Gestion de Estudiantes")
        print("2. Gestion de Docentes")
        print("3. Gestion de Cursos")
        print("4. Gestion de Inscripciones")
        print("5. Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            logger.info("Entrando al menu de estudiantes")
            menu_estudiantes()
        elif opcion == "2":
            logger.info("Entrando al menu de docentes")
            menu_docentes()
        elif opcion == "3":
            logger.info("Entrando al menu de cursos")
            menu_cursos()
        elif opcion == "4":
            logger.info("Entrando al menu de inscripciones")
            menu_inscripciones()
        elif opcion == "5":
            logger.info("Saliendo de la aplicacion...")
            print("Hasta luego")
            break
        else:
            print("Opcion invalida, intente nuevamente.")

    
        