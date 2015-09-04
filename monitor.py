#!/usr/bin/env python3
# coding=utf-8

import requests
import sys
import time
import argparse

import tornado.ioloop
import tornado.gen
import tornado.web

import common
import json

watchlist = ['sc2rain', 'egjd', 'krfantasy', 'naniwasc2', 'forgg']
# watchlist = ['sc2rain', 'ogamingsc2']

"""
curl -H 'Accept: application/vnd.twitchtv.v3+json' \
-X GET https://api.twitch.tv/kraken/streams/sc2rain
"""

existslist = []

@tornado.gen.coroutine
def start():
    # while True:
        try:
            global existslist
            existslist = []
            for i in watchlist:
                r = requests.get('https://api.twitch.tv/kraken/streams/' + i,\
                        headers={'Accept': 'application/vnd.twitchtv.v3+json'})
                if r.json().get('stream'):
                    existslist.append(i)       
        except Exception, e:
            raise e
        finally:
            pass

class MonitorHandler(tornado.web.RequestHandler):
    
    @tornado.gen.coroutine
    def get(self):
        self.write(json.dumps(existslist))

def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument(
        '-t', '--looptime', default=60, help='loop query time')
    parser.add_argument(
        '-p', '--port', default=9400, help='set the listened port')
    args = parser.parse_args()
    
    

    common.config_log('log', 'monitor.log', 'DEBUG', enable_stream_handler=True)
    
    application = tornado.web.Application([('/monitor', MonitorHandler)]).listen(args.port)

    tornado.ioloop.PeriodicCallback(start, args.looptime*1000).start()
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    main()


