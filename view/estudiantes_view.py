from prettytable import PrettyTable
from model.Estudiante import Estudiante

def mostrar_estudiantes(estudiantes: list[Estudiante]):
    if not estudiantes:
        print("\nNo hay estudiantes registrados.\n")
        return

    tabla = PrettyTable()
    tabla.field_names = ["ID", "Número Identificación", "Nombre", "Apellido", "Email", "Teléfono", "Fecha Nacimiento"]

    for est in estudiantes:
        tabla.add_row([
            est.id,
            est.numero_identificacion,
            est.nombre,
            est.apellido,
            est.email,
            est.telefono,
            est.fecha_nacimiento
        ])

    print(tabla)


def mostrar_estudiante(est: Estudiante):
    if not est:
        print("Estudiante no encontrado.")
        return

    tabla = PrettyTable()
    tabla.field_names = ["Campo", "Valor"]
    for campo in ["id", "numero_identificacion", "nombre", "apellido", "email", "telefono", "fecha_nacimiento"]:
        tabla.add_row([campo, getattr(est, campo)])

    print(tabla)