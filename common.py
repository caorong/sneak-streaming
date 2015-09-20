#!/usr/bin/env python3
# coding=utf-8

import logging
import os

watchlist = ['sc2rain','egjd','krfantasy','sc2creator','khansolar','Journey92','forgg','naniwasc2', 'bostossmc', 'liquidmana', 'redbullesports', 'mdstephano']

def config_log(log_dir, log_file, log_level='INFO',
               back_count=7, name="", enable_stream_handler=True,
               multithreading=False, multiprocessing=False):

    log_file = os.path.join(log_dir, log_file)

    log_format = '[%(levelname)s]'
    if multithreading:
        log_format += '<t%(thread)d - %(threadName)s>'
    if multiprocessing:
        log_format += '<p%(process)d - %(processName)s>'
    log_format += '<%(module)s>-%(funcName)s: %(message)s --- %(asctime)s'
    log_formatter = logging.Formatter(log_format)

    loghandler_file_rotated = logging.handlers.TimedRotatingFileHandler(
        log_file, when='midnight', interval=1, backupCount=back_count)
    loghandler_file_rotated.setFormatter(log_formatter)
    loghandler_file_rotated.setLevel(getattr(logging, log_level.upper(), None))

    if enable_stream_handler:
        loghandler_stream = logging.StreamHandler()
        loghandler_stream.setFormatter(log_formatter)
        loghandler_stream.setLevel(logging.DEBUG)

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(loghandler_file_rotated)
    if enable_stream_handler:
        logger.addHandler(loghandler_stream)
