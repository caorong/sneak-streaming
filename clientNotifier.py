#!/usr/bin/env python3
# coding=utf-8

import os
import argparse
from subprocess import call

        
import requests

def main():
    parser = argparse.ArgumentParser(
            formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument(
            '-i', '--host', default='localhost', help='monitor host')
    parser.add_argument(
            '-p', '--port', default=9400, help='monitor post')
    args = parser.parse_args()

    r = requests.get('http://'+args.host + ':' + args.port + '/monitor')
    wl = r.json()
    # print(wl)

    if wl:
        call(["/usr/bin/osascript", "-e", "display notification \"live - {}\" with title \"sc2\" subtitle \"now streaming {}\"".format(','.join(wl),  "")])


if __name__ == '__main__':
    main()



