import logging

# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#                     datefmt='%m/%d/%Y  %H/%M/%S')

# logging.debug("this is a debug message")
# logging.info("this is a info message")
# logging.warning("this is a warning message")
# logging.error("this is a error message")
# logging.critical("this is a critical message")


import helper


#log handlers---> dispatch message to specific destination
logger = logging.getLogger(__name__)

#create handler
stream = logging.StreamHandler()
file = logging.FileHandler('file.log')

#level and format for each handler
stream.setLevel(logging.WARNING)
file.setLevel(logging.ERROR)

formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
stream.setFormatter(formatter)
file.setFormatter(formatter)

logger.addHandler(stream)
logger.addHandler(file)

logger.warning('this is a warning')
logger.error('this is an error')


