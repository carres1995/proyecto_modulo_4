from prettytable import PrettyTable
from model.Curso import Curso
from utils.logs_proyect import logger

def mostrar_cursos(cursos: list[Curso]):
    """Muestra una tabla con todos los cursos"""
    if not cursos:
        print("\nNo hay cursos registrados.\n")
        return

    tabla = PrettyTable()
    tabla.field_names = [
        "ID",
        "Codigo",
        "Nombre",
        "Descripcion",
        "Fecha Inicio",
        "Fecha Fin",
        "Docente ID"
    ]

    for curso in cursos:
        tabla.add_row([
            curso.id,
            curso.codigo,
            curso.nombre,
            curso.descripcion,
            curso.fecha_inicio,
            curso.fecha_fin,
            curso.docente_id if hasattr(curso, "docente_id") else "N/A"
        ])

    print(tabla)


def mostrar_curso(curso):
    """Muestra los datos detallados de un solo curso"""
    if not curso:
        print("Curso no encontrado.")
        return

    logger.info(f"Mostrando curso con ID: {curso.id}")

    tabla = PrettyTable()
    tabla.field_names = ["Campo", "Valor"]

    campos = [
        "id",
        "codigo",
        "nombre",
        "descripcion",
        "fecha_inicio",
        "fecha_fin",
        "docente_id"
    ]

    for campo in campos:
        valor = getattr(curso, campo, "N/A")
        tabla.add_row([campo, valor])

    print(tabla)
    
def mostrar_conteo_cursos(conteo: int):
    print(f"\nTotal de cursos registrados: {conteo}\n")    
