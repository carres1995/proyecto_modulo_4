from utils.logs_proyect import logger
from data.init_db import init_db
from main_t.menu_principal import menu_principal

if __name__ == "__main__":
    try:
        logger.info("Iniciando aplicacion...")
        init_db()
        menu_principal()
    except Exception as e:
        logger.exception("Ocurrio un error inesperado en la aplicacion: ", e)
        print(f"Ocurrio un error inesperado: {e}")
