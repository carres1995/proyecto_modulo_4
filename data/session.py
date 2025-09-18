"""from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from logs.logs_proyect import log_error, log_info
from typing import Generator


from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    log_error("DATABASE_URL no está configurada en el archivo .env")
    
def get_engine():
    try:
        engine = create_engine(DATABASE_URL)#type: ignore
        log_info("Motor de base de datos creado correctamente")
        return engine
    except Exception as e:
        log_error(f"Error al crear el motor de la base de datos: {e}")
    
engine = get_engine()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
      

def get_db() -> Generator:

    db = SessionLocal()
    try:
        yield db
    except Exception as e:
        log_error(f"Error al obtener la sesión de la base de datos: {e}")
        db.rollback()
        

          
    finally:
        db.close()  
        log_info("Sesión de la base de datos cerrada correctamente")

"""