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
    ## para los mensajes: https://docs.python.org/3/library/logging.html#levels.
    ## 0. NOTSET
    ## 10. DEBUG: INFORMACIÓN DE INTERÉS PARA UN DEPURADOR
    ## 20. INFO: CONFIRMACIÓN DE QUE LAS COSAS FUNCIONAN COMO DEBEN
    ## 30. WARNING: ALGO INESPERADO HA OCURRIDO Y PUEDE SER CAUSA DE UN PROBLEMA EN EL FUTURO
    ## 40. ERROR: DEBIDO A UN ERROR EL PROGRAMA NO HA FUNCIONADO COMO SE ESPERABA
    ## 50. CRITICAL: EL PROGRAMA DEBIDO A UN ERROR NO PUEDE SEGUIR FUNCIONANDO

    ## En este caso, lo hemos configurado mediante fichero de configuración y hemos establecido el nivel de criticidad en DEBUG. Vamos a analizar el fichero.

    
    ## Ojo, se pueden definir  los registros con __name__ (que se refiere al nombre del módulo en python)
    # o script, permitiendo un control más granular.
    logger = logging.getLogger(__name__) ## Un logger siempre se tiene que instanciar a través de getLogger

    logger.info("hello world")
    logger.error("fatal error")