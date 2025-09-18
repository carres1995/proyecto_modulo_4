from prettytable import PrettyTable
from typing import List
from model.Curso import Curso


def mostrar_cursos(cursos: List[Curso]):
    if not cursos:
        print("\nNo hay cursos registrados.\n")
        return

    tabla = PrettyTable()
    tabla.field_names = ["ID", "Código", "Nombre", "Descripción", "Fecha Inicio", "Fecha Fin", "Docente_id"]

    for curso in cursos:
        tabla.add_row([
            curso.id,
            curso.codigo,
            curso.nombre,
            curso.descripcion,
            curso.fecha_inicio.strftime('%Y-%m-%d'),
            curso.fecha_fin.strftime('%Y-%m-%d'),
            curso.docente.id
        ])

    print(tabla)

def mostrar_curso(curso: Curso):
    if not curso:
        print("\nCurso no encontrado.\n")
        return

    print(f"\nID: {curso.id}")
    print(f"Código: {curso.codigo}")
    print(f"Nombre: {curso.nombre}")
    print(f"Descripción: {curso.descripcion}")
    print(f"Fecha de Inicio: {curso.fecha_inicio.strftime('%Y-%m-%d')}")
    print(f"Fecha de Fin: {curso.fecha_fin.strftime('%Y-%m-%d')}\n")
    print(f"Docente: {curso.docente.nombre if curso.docente else 'No asignado'}")