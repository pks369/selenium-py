import logging
logging.basicConfig(filename="C:\\Users\\Dell\\PycharmProjects\\selenium\\seleniumLogs\\test.log",
                    format='%(asctime)s: %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y  %I:%M:%S %p')
logger=logging.getLogger()
logger.setLevel(logging.DEBUG)

logger.debug('This is debugg message')
logger.info('This is info message')
logger.warning('This is warning')
logger.error('This is error message')
logger.critical('This is critical message')