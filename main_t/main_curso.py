from data.base import SessionLocal
from services.curso_service import CursoService
from utils.logs_proyect import logger
from utils.decorators import manejar_errores
from utils.validators import limpiar_pantalla as clear, validar_nombres as vno, validar_fecha as vfe
from view.cursos_view import mostrar_cursos as m_cursos, mostrar_curso as m_curso

db = SessionLocal()
service = CursoService(db)

# ========== OPCIONES DEL MENU ==========

@manejar_errores
def opcion_mostrar_cursos():
    cursos = service.mostrar_cursos()
    if cursos:
        logger.info(f"Se encontraron {len(cursos)} cursos")
        m_cursos(cursos)
    else:
        logger.warning("No hay cursos registrados.")
        print("No hay cursos registrados.")

@manejar_errores
def opcion_agregar_curso():
    codigo = input("Codigo del crso: ")
    nombre = vno(input("Nombre del curso: "))
    descripcion = input("Descripcion: ")
    fecha_inicio = vfe(input("Fecha de inicio (YYYY-MM-DD): "))
    fecha_fin = vfe(input("Fecha de fin (YYYY-MM-DD): "))
    docente_id = input("ID del docente (opcional): ")
    docente_id = int(docente_id) if docente_id.strip() != "" else None

    service.agregar_curso(codigo, nombre, descripcion, fecha_inicio, fecha_fin, docente_id)
    print("Curso agregado correctamente.")

@manejar_errores
def opcion_buscar_curso():
    curso_id = int(input("ID del curso: "))
    curso = service.buscar_curso(curso_id)
    if curso:
        m_curso(curso)
    else:
        print("No se encontro le curso.")

@manejar_errores
def opcion_modificar_curso():
    curso_id = int(input("ID del curso: "))
    codigo = input("Codigo del curso: ")
    nombre = vno(input("Nombre del curso: "))
    descripcion = input("Descripcion: ")
    fecha_inicio = vfe(input("Fecha de inicio (YYYY-MM-DD): "))
    fecha_fin = vfe(input("Fecha de fin (YYYY-MM-DD): "))
    docente_id = input("ID del docente (opcional): ")
    docente_id = int(docente_id) if docente_id.strip() != "" else None

    actualizado = service.modificar_curso(curso_id, codigo, nombre, descripcion, fecha_inicio, fecha_fin, docente_id)
    print("Curso modificado." if actualizado else "No se pudo modificar el curso.")

@manejar_errores
def opcion_eliminar_curso():
    curso_id = int(input("ID del curso: "))
    eliminado = service.eliminar_curso(curso_id)
    print("Curso eliminado." if eliminado else "No se encontro el curso.")

@manejar_errores
def opcion_buscar_curso_por_nombre():
    nombre = input("Ingrese el nombre exacto del curso: ")
    curso = service.buscar_curso_por_nombre(nombre)
    if curso:
        m_curso(curso)
    else:
        print("No se encontro el curso con ese nombre.")

@manejar_errores
def opcion_conteo_cursos():
    cantidad = service.conteo_cursos()
    print(f"Total de cursos registrados: {cantidad}")


def menu_cursos():
    while True:
        clear()
        print("\n===== MENU DE CURSOS =====")
        print("1. Mostrar Cursos")
        print("2. Agregar Curso")
        print("3. Buscar Curso")
        print("4. Modificar Curso")
        print("5. Eliminar Curso")
        print("6. Buscar curso por nombre")
        print("7. Conteo de cursos")
        print("8. Volver al menu principal")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            opcion_mostrar_cursos()
        elif opcion == "2":
            opcion_agregar_curso()
        elif opcion == "3":
            opcion_buscar_curso()
        elif opcion == "4":
            opcion_modificar_curso()
        elif opcion == "5":
            opcion_eliminar_curso()
        elif opcion == "6":
            opcion_buscar_curso_por_nombre()
        elif opcion == "7":
            opcion_conteo_cursos()
        elif opcion == "8":
            logger.info("Saliendo del menu de cursos.")
            break
        else:
            print("Opcion no valida.")
        
        input("\nPresione Enter para continuar...")
