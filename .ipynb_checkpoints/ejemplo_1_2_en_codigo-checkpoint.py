
import logging
# Creamos un logger
logger = logging.getLogger(__name__)

# Creamos los handlers
stream_handler = logging.StreamHandler()
file_handler = logging.FileHandler('logs/ejemplo_1.log')

# Establecemos los niveles
stream_handler.setLevel(logging.WARNING)
file_handler.setLevel(logging.ERROR)

# Establecemos los formatters y se los pasamos a los handlers
stream_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
file_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(stream_format)
file_handler.setFormatter(file_format)

# Añadimos los handlers al logger

logger.addHandler(stream_handler)
logger.addHandler(file_handler)

logger.warning('info!!!')

logger.error('ERROR!!!!')