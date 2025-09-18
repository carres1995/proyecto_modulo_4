from prettytable import PrettyTable
from typing import List
from model.Docente import Docente


def mostrar_docentes(docentes: List[Docente]):
    if not docentes:
        print("\nNo hay docentes registrados.\n")
        return

    tabla = PrettyTable()
    tabla.field_names = ["ID", "Número Identificacion", "Nombre", "Apellido", "Email", "Teléfono", "Especialidad"]

    for doc in docentes:
        tabla.add_row([
            doc.id,
            doc.numero_identificacion,
            doc.nombre,
            doc.apellido,
            doc.email,
            doc.telefono,
            doc.especialidad
        ])

    print(tabla)


def mostrar_docente(docente: Docente):
    if not docente:
        print("\nDocente no encontrado.\n")
        return

    tabla = PrettyTable()
    tabla.field_names = ["Campo", "Valor"]
    for campo in ["id", "numero_identificacion", "nombre", "apellido", "email", "telefono", "especialidad"]:
        tabla.add_row([campo, getattr(docente, campo)])
    print(tabla)    

