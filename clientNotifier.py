#!/usr/bin/env python3
# coding=utf-8

import os
import platform
import argparse
from subprocess import call
import json
import pickle

import requests

import common
from decisionMaker import make_decision


watchlist = common.watchlist
# mac - Darwin / linux - Linux
OS = platform.system()
#  OS = 'Linux'
CURR_DIR = os.path.dirname(os.path.realpath(__file__))
REMOTE_VPS_IP = None


def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument(
        '-i', '--host', default='localhost', help='monitor host')
    parser.add_argument(
        '-p', '--port', default=9400, help='monitor post')
    parser.add_argument(
        '-d', '--debug', default=False, type=bool, help='monitor post')
    parser.add_argument(
        '-id', '--identify',
        default='/root/.ssh/id_rsa', help='fabric remote vps ssh private key')
    args = parser.parse_args()

    r = requests.get('http://'+args.host + ':' + args.port + '/monitor')
    global REMOTE_VPS_IP
    if not REMOTE_VPS_IP:
        REMOTE_VPS_IP = args.host
    wl = r.json()

    if args.debug:
        print(wl)

    _fname = "/tmp/sc2now"

    # if file exists, and live list is same
    # do not call notification
    if os.path.isfile(_fname):
        with open(_fname, 'rb') as f:
            pdata = pickle.load(f)
            previous_wl = json.loads(pdata)
            if previous_wl != wl:
                call_notifier(previous_wl, wl, args.identify)
    else:
        call_notifier(None, wl, args.identify)

    with open(_fname, 'wb') as f:
        pickle.dump(json.dumps(wl), f, 0)


def call_notifier(pwl, wl, identifiy_file=''):
    if OS == 'Darwin':
        call(["/usr/bin/osascript", "-e", "display notification \"live - {}\" with title \"sc2\" subtitle \"now streaming {}\"".format(','.join(wl),  "")])
    elif OS == 'Linux':
        # elif OS == 'Darwin':
        #  print(pwl, wl)
        target = make_decision(pwl, wl)
        #  print('desicion', target)
        print('target', target)
        if target is not None:
            #  print(target, REMOTE_VPS_IP)
            # fix yourself
            #  print(["/usr/bin/python", CURR_DIR + '/fabfile.py', str(watchlist[target]), str(REMOTE_VPS_IP)])
            call(["/usr/bin/python", CURR_DIR + '/fabfile.py', str(watchlist[target]), str(REMOTE_VPS_IP), str(identifiy_file)])
            #  call(["python", CURR_DIR + '/fabfile.py', str(watchlist[target]), str(REMOTE_VPS_IP)])

if __name__ == '__main__':
    main()
