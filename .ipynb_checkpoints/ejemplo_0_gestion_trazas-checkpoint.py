
## El módulo de logging también te permite capturar las trazas, como vimos con las Excepciones.

import logging

numerador = 1
denominador = 0

try:
  resultado = numerador / denominador
except Exception as e:
  logging.error("Oooops!", exc_info=True)