from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from utils.logs_proyect import logger
from dotenv import load_dotenv
import os


load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if DATABASE_URL is None:
    logger.error("DATABASE_URL environment variable is not set.")
    raise Exception("DATABASE_URL environment variable is not set.")


try:
    engine = create_engine(DATABASE_URL, echo=False)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base = declarative_base()
    logger.info("Base de datos configurada correctamente en %s", DATABASE_URL)
except Exception as e:
    logger.error("Error al configurar la base de datos: %s", str(e))
    raise Exception("Error al configurar la base de datos") 