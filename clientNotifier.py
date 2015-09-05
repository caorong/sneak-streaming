#!/usr/bin/env python3
# coding=utf-8

import os
import argparse
from subprocess import call
import json
import pickle

        
import requests

def main():
    parser = argparse.ArgumentParser(
            formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument(
            '-i', '--host', default='localhost', help='monitor host')
    parser.add_argument(
            '-p', '--port', default=9400, help='monitor post')
    parser.add_argument(
            '-d', '--debug', default=False, type=bool, help='monitor post')
    args = parser.parse_args()

    r = requests.get('http://'+args.host + ':' + args.port + '/monitor')
    wl = r.json()

    if args.debug:
        print(wl)
        
    _fname = "/tmp/sc2now"

    # if file exists, and live list is same
    # do not call notification

    if os.path.isfile(_fname):
        with open(_fname, 'rb') as f:
            pdata = pickle.load(f)
            if json.loads(pdata) != wl:
                call_notifier(wl)
    else:
        call_notifier(wl)


    with open(_fname, 'wb') as f:
        pickle.dump(json.dumps(wl), f, 0)
        
def call_notifier(wl):
    call(["/usr/bin/osascript", "-e", "display notification \"live - {}\" with title \"sc2\" subtitle \"now streaming {}\"".format(','.join(wl),  "")])


if __name__ == '__main__':
    main()



