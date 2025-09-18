from prettytable import PrettyTable
from typing import List
from model.Estudiante import Estudiante

def mostrar_estudiantes(estudiantes: List[Estudiante]):
    
    if not estudiantes:
        print("\nNo hay estudiantes registrados.\n")
        return

    tabla = PrettyTable()
    tabla.field_names = ["ID", "numero_identificacion", "Nombre", "Apellido", "Email"]

    for est in estudiantes:
        tabla.add_row([
            est.id,
            est.numero_identificacion,
            est.nombre,
            est.apellido,
            est.email
        ])

    print(tabla)
    
def mostrar_estudiante(estudiante: Estudiante):
    if not estudiante:
        print("\nEstudiante no encontrado.\n")
        return

    print(f"\nID: {estudiante.id}")
    print(f"Número de Identificación: {estudiante.numero_identificacion}")
    print(f"Nombre: {estudiante.nombre}")
    print(f"Apellido: {estudiante.apellido}")
    print(f"Email: {estudiante.email}")
    print(f"Teléfono: {estudiante.telefono}")
    print(f"Fecha de Nacimiento: {estudiante.fecha_nacimiento.strftime('%Y-%m-%d')}\n")       