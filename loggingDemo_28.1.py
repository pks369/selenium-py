'''
Agenda:
    1.)Logging
    2.)Log Levels

Logging: Is very useful tool in a programmer's toolbox. It can help you develop a better understanding of the  flow  of a program
and discover  scenarios that you might not even  have thought  of while developing.

Log Levels: |DEBUG| |INFO| |WARNING| |ERROR| | CRITICAL|

'''
import logging
logging.basicConfig(filename="C:\\Users\\Dell\\PycharmProjects\\selenium\\seleniumLogs\\test.log",
                    format='%(asctime)s: %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y  %I:%M:%S %p' ,level=logging.DEBUG)

logging.debug('This is debugg message')
logging.info('This is info message')
logging.warning('This is warning')
logging.error('This is error message')
logging.critical('This is critical message')