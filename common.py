#!/usr/bin/env python3
# coding=utf-8

import logging
import os
from collections import OrderedDict

roomNameDict = OrderedDict([
    ('sc2rain', '大雨神'),
    ('egjd', '菜东'),
    ('khansolar', "Samsung's Zerg Solar"),
    ('sc2creator', 'sc2creator'),
    ('bostossmc', '神族总统MC'),
    ('krfantasy', '范太子'),
    ('polt', '高富帅 polt'),
    ('naniwasc2', 'naniwa'),
    ('axryung', 'Ryung LoTV'),
    ('forgg', 'forgg'),
    ('gayoung_kim', '韩国妹子 Aphrodite'),
    ('missmagitek', '星际妹子 missmagitek'),
    ('livibee', '星际妹子 livibee'),
    ('inksie', '星际妹子 inksie'),
    ('Journey92', 'SAMSUNG Journey'),
    ('mYiSacsri', 'mYiSacsri'),
    ('liquidmana', 'liquidMaNa '),
    ('mdstephano', 'Stephano LoTV'),
    ('liquidtlo', 'LiquidTLO 欧服'),
    ('firecake', '莽夫-火蛋糕'),
    ('wayne379', '台湾谐星-鬼手辉'),
    ('totalbiscuit', '咆哮杯~'),
    ('redbullesports', '红牛杯-执政官-LoTV'),
    ('starcraft', 'startcraft'),
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
