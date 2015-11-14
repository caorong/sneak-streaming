#!/usr/bin/env python3
# coding=utf-8

import logging
import os
from collections import OrderedDict

roomNameDict = OrderedDict([
    ('sc2rain', '大雨神'),
    ('egjd', '菜东'),
    ('krfantasy', '范太子'),
    ('naniwasc2', 'naniwa'),
    ('sc2creator', 'sc2creator'),
    ('khansolar', "Samsung's Zerg Solar"),
    ('bostossmc', '神族总统MC'),
    ('axryung', 'Ryung LoTV'),
    ('forgg', 'forgg'),
    ('Journey92', 'SAMSUNG Journey'),
    ('missmagitek', '星际妹子 missmagitek'),
    ('livibee', '星际妹子 livibee'),
    ('inksie', '星际妹子 inksie'),
    ('starcraft', 'startcraft'),
    ('liquidmana', 'liquidMaNa '),
    ('mdstephano', 'Stephano LoTV'),
    ('redbullesports', '红牛杯-执政官-LoTV'),
    ('wayne379', '台湾谐星-鬼手辉'),
    ])

watchlist = list(map(lambda x: x[0], roomNameDict.items()))

#  print(roomNameDict['egjd'])
#  print(watchlist)

#  watchlist = ['sc2rain', 'egjd','krfantasy','sc2creator','khansolar','axryung','Journey92','forgg', 'bostossmc', 'mdstephano','naniwasc2','liquidmana', 'inksie', 'missmagitek', 'livibee','redbullesports', 'wayne379']


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


def only_stream(name, log_level='INFO', multithreading=False,
                multiprocessing=False):
    log_format = '[%(levelname)s]'
    if multithreading:
        log_format += '<t%(thread)d - %(threadName)s>'
    if multiprocessing:
        log_format += '<p%(process)d - %(processName)s>'
    log_format += '<%(module)s>-%(funcName)s: %(message)s --- %(asctime)s'
    log_formatter = logging.Formatter(log_format)

    loghandler_stream = logging.StreamHandler()
    loghandler_stream.setFormatter(log_formatter)
    loghandler_stream.setLevel(logging.DEBUG)

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(loghandler_stream)
