from prettytable import PrettyTable
from typing import List
from model.Inscripcion import Inscripcion
from model.Curso import Curso
from model.Estudiante import Estudiante

def mostrar_inscripciones(inscripciones: List[Inscripcion]):
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
        print("\nInscripcion no encontrada.\n")
        return

    print(f"\nID: {inscripcion.id}")
    print(f"Estudiante ID: {inscripcion.estudiante_id}")
    print(f"Curso ID: {inscripcion.curso_id}")
    print(f"Fecha Inscripcion: {inscripcion.fecha_inscripcion.strftime('%Y-%m-%d')}\n")
    
#crear una tabla para visualizar cursos y docentes
def mostrar_cursos_docentes(cursos: List[Curso], Estudiantes: List[Estudiante]):
    if not cursos:
        print("\nNo hay cursos registrados.\n")
        return
    if not Estudiantes:
        print("\nNo hay estudiantes registrados.\n")
        return

    tabla = PrettyTable()
    tabla.field_names = ["Curso ID", "Nombre Curso", "Estudiante ID", "Nombre Estudiante",]

    for curso in cursos:
        for estudiante in Estudiantes:
            tabla.add_row([
                curso.id,
                curso.nombre,
                estudiante.id,
                estudiante.nombre
            ])

    print(tabla)
