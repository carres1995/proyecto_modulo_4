import logging
from logging.handlers import TimedRotatingFileHandler
import os


os.makedirs("utils", exist_ok=True)

logger = logging.getLogger("ProyectoModulo4")
logger.setLevel(logging.INFO)

handler = TimedRotatingFileHandler('utils/app.log', when='midnight', backupCount=7, encoding='utf-8')

formatter = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(message)s'
    )
handler.setFormatter(formatter)
    
if not logger.handlers:
    logger.addHandler(handler)