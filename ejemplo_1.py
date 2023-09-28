# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

#El módulo loging está diseñado para registrar eventos del sistema que se esté desarrollando y mostrarlos
# por diferentes salidas o, incluso, hacer filtros sobre ellos.

import logging
import logging.config
import yaml
import os
import sys

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    with open("logging_handlers.yaml", "r") as f:
        yaml_config = yaml.safe_load(f.read())
        logging.config.dictConfig(yaml_config)

    ## Para registrar los mensajes, necesitamos un logger.  El logger tiene, por defecto, 5 niveles de criticidad
    ## para los mensajes.
    ## En este caso, lo hemos configurado mediante fichero de configuración. Vamos a ello.
    ## Para cada módulo, puedo definir los registros con __name__ o script, permitiendo un control más granular.
    logger = logging.getLogger(__name__)

    logger.info("hello world")
    logger.error("fatal error")