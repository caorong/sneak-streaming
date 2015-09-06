#!/usr/bin/env python2
# coding=utf-8

import json
import socket, datetime, os, requests, urllib2, sys
from fabric.api import env, roles, with_settings, sudo, lcd, cd, run, parallel, local, hosts
from fabric.contrib.files import exists
from livestreamer import Livestreamer
import urllib

"""
watchlist = ['sc2rain', 'egjd', 'krfantasy', 'naniwasc2', 'forgg']

fab streaming:target='xxx',dycode='xxx'

"""

roomNameDict = {
        'bostossmc':'神族总统MC',
        'sc2rain':'大雨神',
        'egjd':'菜东',
        'krfantasy':'范太子',
        'naniwasc2':'naniwa',
        'forgg':'forgg',
        'sc2creator':'sc2creator',
        'Journey92':'SAMSUNG Journey',
        }

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

def _get_rtmpurl():
    # close and start live
    local('./close_dy_live.sh')
    local('./open_dy_live.sh')
    j = local('./req_dy_rtmp.sh', capture=True)
    print(j)
    return json.loads(j.strip())['rtmp_send']['rtmp_val']

def streaming(target, dycode=''):
    url = _getLiveUrl(target)

    if not dycode:
        dycode = _get_rtmpurl()
    # change room name
    local('./change_dy_roomname.sh {}'.format(urllib.quote(roomNameDict[target] + '第一视角')))

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
    if len(sys.argv) < 3:
        print('python fabfile.py target Host dycode')
        exit()
    # getLiveUrl('gsl')

    env.host_string = 'root@'+ sys.argv[2]
    print(env)

    if len(sys.argv) == 4:
        streaming(sys.argv[1], sys.argv[3])
    else:
        streaming(sys.argv[1])



