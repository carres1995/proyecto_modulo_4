from functools import wraps
from validators import limpiar_pantalla as clear
from utils.logs_proyect import logger

def manejar_errores(func):
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        clear()
        try:
            return func(*args, **kwargs)
        except ValueError as ve:
            logger.error(f"Valor invalido: {ve}")
            print(f"⚠️ Valor invalido: {ve}")
        except Exception as e:
            logger.exception(f"Error inesperado en {func.__name__}: {e}")
            print(f"⚠️ Error inesperado: {e}")
        finally:
            input("\nPresione Enter para continuar...")
    return wrapper