# logging_config.py
import logging

def setup_logging(level=logging.INFO):
    logging.basicConfig(level=level,
                        format='%(levelname)s:%(name)s:%(filename)s:%(lineno)d:%(message)s')
