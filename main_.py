from utils.logs_proyect import logger
from data.init_db import init_db
from main_t.menu_principal import menu_principal

if __name__ == "__main__":
    try:
        logger.info("Iniciando aplicación...")
        
        init_db()
        
        menu_principal()

    except Exception as e:
        logger.exception("Ocurrió un error inesperado: %s", str(e))
        raise Exception("Ocurrió un error inesperado")
        1