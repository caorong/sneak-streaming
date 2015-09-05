#!/usr/bin/env python2
# coding=utf-8

import json
import socket, datetime, os, requests, urllib2, sys
from fabric.api import env, roles, with_settings, sudo, lcd, cd, run, parallel, local, hosts
from fabric.contrib.files import exists
from livestreamer import Livestreamer

"""
watchlist = ['sc2rain', 'egjd', 'krfantasy', 'naniwasc2', 'forgg']

fab streaming:target='xxx',dycode='xxx'

"""

def _getLiveUrl(target):
   livestreamer = Livestreamer()
   streams = livestreamer.streams("http://www.twitch.tv/" + target)
   print(streams)
   if streams:
       # default
       # xx = streams.popitem()
       # return xx[1].url
       xx = streams.get('high')
       return xx.url
   return None

def streaming(target, dycode):
    url = _getLiveUrl(target)

    cmd = "/root/FFmpeg/ffmpeg -re -i '{}' -c:v libx264 -b:v 1000k -c:a libfdk_aac -profile:a aac_he -ac 2 -ar 44100 -ab 64k -f flv 'rtmp://send3.douyutv.com/live/{}'".format(url, dycode)
    print
    print(cmd)
    # kill old
    pid = run("ps -ef|grep SCREEN|grep -v grep |awk '{print $2}'")
    if pid:
        run('kill -9 {}'.format(pid))
    run("/usr/bin/screen -d -m " + cmd + " && sleep 1")

if __name__ == '__main__':
    print(sys.argv)
    if len(sys.argv) < 4:
        print('python fabfile.py target dycode Host')
        exit()
    # getLiveUrl('gsl')

    env.host_string = 'root@'+ sys.argv[3]
    print(env)
    streaming(sys.argv[1], sys.argv[2])


