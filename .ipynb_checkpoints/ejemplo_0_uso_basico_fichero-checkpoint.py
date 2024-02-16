import logging

#logging.basicConfig(level=logging.DEBUG)
#logging.debug('This will get logged')


#logging.error('This error will + get logged')


logging.basicConfig(filename='./logs/ejemplo_0.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
logging.warning('This will get logged to a file')