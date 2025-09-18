from data.base import SessionLocal
from services.docente_service import DocenteService
from utils.validators import validar_email as vem, validar_nombres as vno, validar_fecha as vfe, validar_identidad as vid
from view.docentes_view import mostrar_docente as m_docente,mostrar_docentes as m_docentes
from utils.decorators import manejar_errores


db = SessionLocal()
service = DocenteService(db)

@manejar_errores
def mostrar_docentes():
    docentes= service.mostrar_docentes()
    if docentes:
        m_docentes(docentes)
    else:
        print("No hay docentes registrados.")

@manejar_errores
def agregar_estudiante():
    n_id= vid(input("Numero de identificacion: ")) 
    nombre= vno(input("Nombre: "))
    apellido = vno(input("Apellido: "))
    email = vem(input("Email: "))
    telefono = input("Telefono: ")  
    especialidad= input("Especialidad: ")   
    service.agregar_docente(n_id, nombre, apellido, email, telefono, especialidad)  
    print("Docente agregado correctamente")  
    
@manejar_errores
def buscar_docente():
    docente_id= int(input("ID del docente: "))
    docente= service.buscar_docente(docente_id)
    if docente:  
        m_docente(docente)
    else:
        print("No se encontro el docente.")

def modificar_estudiante():
    docente_id= int(input("ID del docente: "))        
    n_id= vid(input("Numero de identificacion: ")) 
    nombre= vno(input("Nombre: "))
    apellido = vno(input("Apellido: "))
    email = vem(input("Email: "))
    telefono = input("Telefono: ")  
    especialidad= input("Especialidad: ") 
    actualizar= service.modificar_docente(docente_id, n_id,nombre, apellido, email, telefono, especialidad)
    print("Estudiante modificado." if actualizar else "No se pudo modificar.")  

def eliminar_docente():
    docente_id= int(input("ID del docente: "))  
    eliminar=service.eliminar_docente(docente_id)
    print("Docente eliminado con exito." if eliminar else "No se pudo eliminar al docente.")             
            
def menu_docentes():
    while True:
        print("\n Menu Docentes")
        print("1. Mostrar Docentes")
        print("2. Agregar Docente")
        print("3. Buscar Docente")
        print("4. Modificar Docente")
        print("5. Eliminar Docente")
        print("6. Volver al menú principal")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            mostrar_docentes()
        elif opcion == "2":
            agregar_estudiante()
        elif opcion == "3":
            buscar_docente()
        elif opcion =="4":
            modificar_estudiante()
        elif opcion == "5":
            eliminar_docente() 
        elif opcion =="6":
            break                 
        else:
            print("Opcion no valida.")
            input("\nPresione Enter para continuar...")