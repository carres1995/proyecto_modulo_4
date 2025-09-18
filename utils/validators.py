from utils.logs_proyect import logger
import os

def limpiar_pantalla():
    os.system('cls')
    
def validar_nombres(texto):
    if not texto.isalpha():
        logger.error("Texto incorrecto.")
        return False
    return texto
        
        
def validar_identidad(id):
    if not id.isdigit():
        logger.error(f"identidad invalida: {id}")
        return False 
    if len(id) < 5 or len(id) > 10:
        logger.error(f"Numero debe estar entre 5 y 10 digitos.")
        return False
    return id

def validar_email(email):
    if "@" not in email or "." not in email:
        logger.error(f"Email inválido: {email}")
        raise ValueError("El email no es válido.")
    return email

from datetime import datetime

def validar_fecha(fecha_str):
    try:
        return datetime.strptime(fecha_str, "%Y-%m-%d").date()
    except ValueError:
        raise ValueError(f"Fecha inválida: {fecha_str}")