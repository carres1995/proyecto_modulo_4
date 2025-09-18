from prettytable import PrettyTable
from typing import List
from model.Docente import Docente


def mostrar_docentes(docentes: List[Docente]):
    if not docentes:
        print("\nNo hay docentes registrados.\n")
        return

    tabla = PrettyTable()
    tabla.field_names = ["ID", "Número Identificación", "Nombre", "Apellido", "Email", "Teléfono", "Especialidad"]

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

    print(f"\nID: {docente.id}")
    print(f"Número de Identificación: {docente.numero_identificacion}")
    print(f"Nombre: {docente.nombre}")
    print(f"Apellido: {docente.apellido}")
    print(f"Email: {docente.email}")
    print(f"Teléfono: {docente.telefono}")
    print(f"Especialidad: {docente.especialidad}\n")
