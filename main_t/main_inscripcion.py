from data.base import SessionLocal
from services.inscripcion_service import InscripcionService
from utils.validators import validar_fecha as vfe
from view.inscripciones_view import (
    mostrar_inscripciones as m_inscripciones,
    mostrar_inscripcion as m_inscripcion,
    mostrar_cursos_y_estudiantes as m_cursos_estudiantes
)
from utils.decorators import manejar_errores

db = SessionLocal()
service = InscripcionService(db)


@manejar_errores
def mostrar_inscripciones():
    inscripciones = service.mostrar_inscripciones()
    if inscripciones:
        m_inscripciones(inscripciones)
    else:
        print("No hay inscripciones registradas.")


@manejar_errores
def agregar_inscripcion():
    # Mostrar cursos y estudiantes para elegir
    cursos, estudiantes = service.obtener_cursos_y_estudiantes()
    m_cursos_estudiantes(cursos, estudiantes)

    estudiante_id = int(input("ID del estudiante: "))
    curso_id = int(input("ID del curso: "))
    fecha_inscripcion = vfe(input("Fecha de inscripcion (YYYY-MM-DD): "))
    service.agregar_inscripcion(estudiante_id, curso_id, fecha_inscripcion)
    print("Inscripcion agregada correctamente.")


@manejar_errores
def buscar_inscripcion():
    inscripcion_id = int(input("ID de la inscripcion: "))
    inscripcion = service.buscar_inscripcion(inscripcion_id)
    if inscripcion:
        m_inscripcion(inscripcion)
    else:
        print("No se encontro la inscripcion.")


@manejar_errores
def modificar_inscripcion():
    inscripcion_id = int(input("ID de la inscripcion: "))
    estudiante_id = int(input("Nuevo ID del estudiante: "))
    curso_id = int(input("Nuevo ID del curso: "))
    fecha_inscripcion = vfe(input("Nueva fecha de inscripcion (YYYY-MM-DD): "))

    actualizado = service.modificar_inscripcion(inscripcion_id, estudiante_id, curso_id, fecha_inscripcion)
    print("Inscripcion modificada." if actualizado else "No se pudo modificar.")


@manejar_errores
def eliminar_inscripcion():
    inscripcion_id = int(input("ID de la inscripcion: "))
    eliminado = service.eliminar_inscripcion(inscripcion_id)
    print("Inscripcion eliminada." if eliminado else "No se encontro la inscripcion.")


def menu_inscripciones():
    while True:
        print("\n===== MENU DE INSCRIPCIONES =====")
        print("1. Mostrar Inscripciones")
        print("2. Agregar Inscripcion")
        print("3. Buscar Inscripcion")
        print("4. Modificar Inscripcion")
        print("5. Eliminar Inscripcion")
        print("6. Volver al menu principal")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            mostrar_inscripciones()
        elif opcion == "2":
            agregar_inscripcion()
        elif opcion == "3":
            buscar_inscripcion()
        elif opcion == "4":
            modificar_inscripcion()
        elif opcion == "5":
            eliminar_inscripcion()
        elif opcion == "6":
            break
        else:
            print("Opcion no valida.")
            input("\nPresione Enter para continuar...")
