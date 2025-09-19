from prettytable import PrettyTable
from model.Inscripcion import Inscripcion
from model.Curso import Curso
from model.Estudiante import Estudiante


def mostrar_inscripciones(inscripciones: list[Inscripcion]):
    if not inscripciones:
        print("\nNo hay inscripciones registradas.\n")
        return

    tabla = PrettyTable()
    tabla.field_names = ["ID", "Estudiante ID", "Curso ID", "Fecha Inscripcion"]

    for ins in inscripciones:
        tabla.add_row([
            ins.id,
            ins.estudiante_id,
            ins.curso_id,
            ins.fecha_inscripcion.strftime("%Y-%m-%d")
        ])

    print(tabla)


def mostrar_inscripcion(inscripcion: Inscripcion):
    if not inscripcion:
        print("Inscripcion no encontrada.")
        return

    tabla = PrettyTable()
    tabla.field_names = ["Campo", "Valor"]

    for campo in ["id", "estudiante_id", "curso_id", "fecha_inscripcion"]:
        valor = getattr(inscripcion, campo)
        if campo == "fecha_inscripcion":
            valor = valor.strftime("%Y-%m-%d")
        tabla.add_row([campo, valor])

    print(tabla)


def mostrar_cursos_y_estudiantes(cursos: list[Curso], estudiantes: list[Estudiante]):
    if not cursos:
        print("\nNo hay cursos registrados.\n")
        return
    if not estudiantes:
        print("\nNo hay estudiantes registrados.\n")
        return

    tabla = PrettyTable()
    tabla.field_names = ["Curso ID", "Nombre Curso", "Estudiante ID", "Nombre Estudiante"]

    for curso in cursos:
        for estudiante in estudiantes:
            tabla.add_row([
                curso.id,
                curso.nombre,
                estudiante.id,
                estudiante.nombre
            ])

    print(tabla)
