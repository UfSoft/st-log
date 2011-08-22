# -*- coding: utf-8 -*-
"""
    st.log
    ~~~~~~

    Simple package that extends python's standard logging by adding to it
    two(2) additional levels, lower than `DEBUG`, `TRACE` and `GARBAGE`.

    Also helps setting up a console and/or a logfile handler(s).

    :copyright: © 2011 UfSoft.org - :email:`Pedro Algarvio (pedro@algarvio.me)`
    :license: BSD, see LICENSE for more details.
"""

__version__         = '0.9'
__package_name__    = 'ST-Log'
__summary__         = "Python's standard logging helpers"
__author__          = 'Pedro Algarvio'
__email__           = 'pedro@algarvio.me'
__license__         = 'BSD'
__url__             = 'http://dev.ufsoft.org/projects/log'
__description__     = __doc__

import new
import logging

LOG_LEVELS = {
    "none": logging.NOTSET,
    "info": logging.INFO,
    "warn": logging.WARNING,
    "warning": logging.WARNING,
    "error": logging.ERROR,
    "none": logging.CRITICAL,
    "debug": logging.DEBUG,
    "trace": 5,
    "garbage": 1
}

LoggingLoggerClass = logging.getLoggerClass()


def setup_logging():
    """
    Setup overall logging engine and add 2 more levels of logging lower than
    DEBUG, TRACE and GARBAGE.
    """
    import logging
    if not hasattr(LoggingLoggerClass, 'trace'):
        def trace(cls, msg, *args, **kwargs):
            return cls.log(5, msg, *args, **kwargs)

        logging.addLevelName(5, 'TRACE')
        LoggingLoggerClass.trace = new.instancemethod(trace, None, LoggingLoggerClass)


    if not hasattr(LoggingLoggerClass, 'garbage'):
        def garbage(cls, msg, *args, **kwargs):
            return cls.log(1, msg, *args, **kwargs)

        logging.addLevelName(1, 'GARBAGE')
        LoggingLoggerClass.garbage = new.instancemethod(garbage, None, LoggingLoggerClass)

    # Set the root logger at the lowest level possible
    logging.getLogger().setLevel(1)


def setup_console_logger(level, fmt=None):
    """
    Setup console logging.
    """
    setup_logging()
    level = LOG_LEVELS.get(level.lower(), logging.ERROR)
    rootLogger = logging.getLogger()
    handler = logging.StreamHandler()

    if fmt is None:
        fmt = '%(asctime)s,%(msecs)03.0f [%(name)-15s][%(levelname)-8s] %(message)s'

    handler.setLevel(level)
    formatter = logging.Formatter(fmt, datefmt="%H:%M:%S")
    handler.setFormatter(formatter)
    rootLogger.addHandler(handler)


def setup_logfile_logger(level, logfile, fmt=None):
    """
    Setup logfile logging.
    """
    setup_logging()
    level = LOG_LEVELS.get(level.lower(), logging.ERROR)
    rootLogger = logging.getLogger()

    import logging.handlers
    handler = getattr(
        logging.handlers, 'WatchedFileHandler', logging.FileHandler)(
            logfile, 'a', 'utf-8', delay=0
    )

    if fmt is None:
        fmt = '%(asctime)s [%(name)-15s][%(levelname)-8s] %(message)s'

    handler.setLevel(level)
    formatter = logging.Formatter(fmt, datefmt="%H:%M:%S")

    handler.setFormatter(formatter)
    rootLogger.addHandler(handler)


def set_logger_level(logger_name, level):
    """
    Tweak a specific logger's logging level
    """
    setup_logging()
    logging.getLogger(logger_name).setLevel(
        LOG_LEVELS.get(level.lower(), logging.ERROR)
    )
