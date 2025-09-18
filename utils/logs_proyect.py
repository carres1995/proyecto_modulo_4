import logging
from logging.handlers import TimedRotatingFileHandler
import os


os.makedirs("logs_files", exist_ok=True)

logger = logging.getLogger("ProyectoModulo4")
logger.setLevel(logging.INFO)

handler = TimedRotatingFileHandler('logs_files/app.log', when='midnight', backupCount=7, encoding='utf-8')

fomatter = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(message)s'
    )
handler.setFormatter(fomatter)
    
if not logger.handlers:
    logger.addHandler(handler)