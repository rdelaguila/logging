# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import logging
import logging.config
import yaml
import os
import sys

# Un filtro permite tener un nivel de control adicional sobre los mensajes. Imaginemos que queremos descartar
# que contengan la palbra 'pasa':
class MiFiltro(logging.Filter):
    def filter(self, record):

        return record.msg.find("pasa",0,len(record.msg)) <=0 #Si la condición es FALSE
# Press the green button in the gutter to run the script.

## Adicionalmente record contiene métodos y atributos útiles a la hora de personalizar los filtros.
## De los más utilizados es levelno record.levelno >= logging.WARNING
if __name__ == '__main__':
    with open("logging_handlers.yaml", "r") as f:
        yaml_config = yaml.safe_load(f.read())
        logging.config.dictConfig(yaml_config)

    logger = logging.getLogger(__name__)
    logger.addFilter(MiFiltro())

    logger.info("hello world")
    logger.error("Es un error, pero pasa de él")
    logger.error("Es un error digno de ese nombre")