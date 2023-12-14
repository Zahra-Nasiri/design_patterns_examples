# main.py

import logging
from singleton import Singleton

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    pass

class LogManager(Singleton):
    def __init__(self, log_file='app.log'):
        self.log_file = log_file
        self._configure_logging()

    def _configure_logging(self):
        logging.basicConfig(
            filename=self.log_file,
            level=logging.INFO,
            format="%(asctime)s [%(levelname)s]: %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )
    
    def log_info(self, message):
        logging.info(message)

    def log_warning(self, message):
        logging.warning(message)

    def log_error(self, message):
        logging.error(message)

log_manager = LogManager()

log_manager.log_info("This is an informational message.")
log_manager.log_warning("This is a warning message.")
log_manager.log_error("This is an error message.")
