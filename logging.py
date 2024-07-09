import logging

# logger = logging.getLogger(__name__)

# # Creae handler
# stream_h = logging.StreamHandler
# file_h = logging.FileHandler('file.log')

# # leveland the handler
# stream_h.setLevel(logging.WARNING)
# file_h.setLevel(logging.ERROR)

# formatter = logging.Formatter()
# stream_h,setFormatter(formatter)
# file_h.setFormatter(formatter)

# logger.addHandler(stream_h)
# logger.addHandler(file_h)

# logger.warning('This is a warning')
# logger.error('This is an error')
# logging.debug['This is degug message']
# logging.info('This is an info message')
# logging.warning('This us s warning message')
# logging.error('This is an error message')
# logging.critical('This is a critical message')

try:
    a = [1,2,3]
    val = a[4]
except Exception as e:
        logging.error(e,exc_info=True)