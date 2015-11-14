#!/usr/bin/env python3
# coding=utf-8

import argparse
import os

import tornado.ioloop
import tornado.gen
import tornado.web
import tornado.httpclient

import common
import json

watchlist = common.watchlist

watchlist = ["Journey92", "wayne379"]

"""
curl -H 'Accept: application/vnd.twitchtv.v3+json' \
-X GET https://api.twitch.tv/kraken/streams/sc2rain
"""

existslist = []


@tornado.gen.coroutine
def start():
    try:
        _existslist = []
        for i in watchlist:
            http_client = tornado.httpclient.AsyncHTTPClient()

            r = yield http_client.fetch(
                'https://api.twitch.tv/kraken/streams/'
                + i,
                headers={'Accept': 'application/vnd.twitchtv.v3+json'})
            bd = r.body
            #  print(bd)
            if json.loads(bd.decode('utf-8')).get('stream'):
                _existslist.append(i)
            #  print(_existslist, existslist)
            global existslist
            existslist = _existslist
    except Exception as e:
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
        '-t', '--looptime', type=int, default=60, help='loop query time')
    parser.add_argument(
        '-p', '--port', type=int, default=9400, help='set the listened port')
    parser.add_argument(
        '-d', '--logdir', default='log', help='set the listened port')
    parser.add_argument(
        '-n', '--logname', default='monitor.log', help='set the listened port')
    args = parser.parse_args()

    if not os.path.isdir(args.logdir):
        os.makedirs(args.logdir)

    common.config_log(args.logdir, args.logname, 'DEBUG',
                      enable_stream_handler=True)

    tornado.web.Application([('/monitor', MonitorHandler)]).listen(args.port)

    start()
    tornado.ioloop.PeriodicCallback(start, args.looptime*1000).start()
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    main()
