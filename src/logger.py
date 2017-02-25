# -*- coding:UTF-8 -*-
import logging
import logging.config

from logutils.colorize import ColorizingStreamHandler


class ColorHandler(ColorizingStreamHandler):

    def __init__(self, *args, **kwargs):
        super(ColorHandler, self).__init__(*args, **kwargs)
        self.level_map = {
            # Provide you custom coloring information here
            logging.DEBUG: (None, 'cyan', False),
            logging.INFO: (None, 'magenta', False),
            logging.WARNING: (None, 'yellow', False),
            logging.ERROR: (None, 'red', False),
            logging.CRITICAL: ('red', 'white', True),
        }


CONFIG = {
    'version': 1,
    'disable_existing_loggers': True,
    'handlers': {
        'console': {
            '()': ColorHandler,
            'info': 'white',
            'level': 'DEBUG',
            'formatter': 'detailed',
            'stream': 'ext://sys.stdout',
        },
    },
    'formatters': {
        'detailed': {
            'format': '[%(asctime)s] [%(levelname)s] %(message)s',
            'datefmt': '%H:%M:%S',
        },
    },
    'loggers': {
        'info': {
            'level': 'DEBUG',
            'handlers': ['console'],
        },
    },
}

logging.config.dictConfig(CONFIG)
logger = logging.getLogger('info')

if __name__ == '__main__':
    logger.debug("Hello world")  # output should be in blue
    logger.info("Hello world")  # output should be in green
    logger.warn("Hello world")  # output should be in yellow
    logger.error("Hello world")  # output should be in red
    logger.critical("Hello world")  # output should be in white with a red back ground
