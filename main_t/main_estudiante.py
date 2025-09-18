from data.base import SessionLocal
from services.estudiante_services import EstudianteService
from utils.validators import validar_email as vem, validar_fecha as vfe, validar_identidad as vid, validar_nombres as vno
from view.estudiantes_view import mostrar_estudiantes as m_estudiantes, mostrar_estudiante as m_estudiante
from utils.decorators import manejar_errores

db = SessionLocal()
service = EstudianteService(db)

@manejar_errores
def opcion_mostrar_estudiantes():
    estudiantes = service.mostrar_estudiantes()
    if estudiantes:
        m_estudiantes(estudiantes)
    else:
        print("No hay estudiantes registrados.")

@manejar_errores
def opcion_agregar_estudiante():
    numero_identificacion = vid(input("Numero de Identificacion: "))
    nombre = vno(input("Nombre: "))
    apellido = vno(input("Apellido: "))
    email = vem(input("Email: "))
    telefono = input("Telefono: ")
    fecha_nacimiento = vfe(input("Fecha de Nacimiento (YYYY-MM-DD): "))
    service.agregar_estudiante(numero_identificacion, nombre, apellido, email, telefono, fecha_nacimiento)
    print("Estudiante agregado correctamente.")

@manejar_errores
def opcion_buscar_estudiante():
    estudiante_id = int(input("ID del estudiante: "))
    estudiante = service.buscar_estudiante(estudiante_id)
    if estudiante:
        m_estudiante(estudiante)
    else:
        print("No se encontro el estudiante.")

@manejar_errores
def opcion_modificar_estudiante():
    estudiante_id = int(input("ID del estudiante: "))
    numero_identificacion = vid(input("Numero de Identificacion: "))
    nombre = vno(input("Nombre: "))
    apellido = vno(input("Apellido: "))
    email = vem(input("Email: "))
    telefono = input("Telefono: ")
    fecha_nacimiento = vfe(input("Fecha de Nacimiento (YYYY-MM-DD): "))
    actualizado = service.modificar_estudiante(estudiante_id, numero_identificacion, nombre, apellido, email, telefono, fecha_nacimiento)
    print("Estudiante modificado." if actualizado else "No se pudo modificar.")

@manejar_errores
def opcion_eliminar_estudiante():
    estudiante_id = int(input("ID del estudiante: "))
    eliminado = service.eliminar_estudiante(estudiante_id)
    print("Estudiante eliminado." if eliminado else "no se encontro el estudiante.")

def menu_estudiantes():
    while True:
        print("\n===== MENÚ DE ESTUDIANTES =====")
        print("1. Mostrar Estudiantes")
        print("2. Agregar Estudiante")
        print("3. Buscar Estudiante")
        print("4. Modificar Estudiante")
        print("5. Eliminar Estudiante")
        print("6. Volver al menu principal")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            opcion_mostrar_estudiantes()
        elif opcion == "2":
            opcion_agregar_estudiante()
        elif opcion == "3":
            opcion_buscar_estudiante()
        elif opcion == "4":
            opcion_modificar_estudiante()
        elif opcion == "5":
            opcion_eliminar_estudiante()
        elif opcion == "6":
            break
        else:
            print("Opcion no valida.")
            input("\nPresione Enter para continuar...")