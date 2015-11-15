#!/usr/bin/env python2
# coding=utf-8

import json
import socket, datetime, os, requests, urllib2, sys
from fabric.api import env, roles, with_settings, sudo, lcd, cd, run, parallel, local, hosts, settings
from fabric.contrib.files import exists
from livestreamer import Livestreamer
import urllib
from common import roomNameDict

"""
watchlist = ['sc2rain', 'egjd', 'krfantasy', 'naniwasc2', 'forgg']

fab streaming:target='xxx',dycode='xxx'

"""

CURR_DIR = os.path.dirname(os.path.realpath(__file__))


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
    local('/bin/bash {}/close_dy_live.sh'.format(CURR_DIR))
    local('/bin/bash {}/open_dy_live.sh'.format(CURR_DIR))
    j = local('/bin/bash {}/req_dy_rtmp.sh'.format(CURR_DIR), capture=True)
    print(j)
    return json.loads(j.strip())['rtmp_send']['rtmp_val']


def streaming(target, dycode=''):
    url = _getLiveUrl(target)
    print(url)

    if not dycode:
        dycode = _get_rtmpurl()
    # change room name
    local('/bin/bash {}/change_dy_roomname.sh {}'.format(CURR_DIR, urllib.quote(roomNameDict[target])))
#  + '第一视角'
    cmd = "/root/FFmpeg/ffmpeg -re -i '{}' -c:v libx264 -b:v 1000k -c:a libfdk_aac -profile:a aac_he -ac 2 -ar 44100 -ab 64k -f flv 'rtmp://send3.douyutv.com/live/{}'".format(url, dycode)
    print
    print(cmd)
    # kill old
    #  pid = run("ps -ef|grep SCREEN|grep -v grep |awk '{print $2}'")
    #  if pid:
        #  run('kill -9 {}'.format(pid))
    with settings(warn_only=True):
        #  run('killall -9 /root/FFmpeg/ffmpeg')
        run('killall -9 ffmpeg')
    run("/usr/bin/screen -d -m " + cmd + " && sleep 1")

if __name__ == '__main__':
    print(sys.argv)
    if len(sys.argv) < 3:
        print('python fabfile.py target Host sshkey-filename')
        exit()
    # getLiveUrl('gsl')
    print(sys.argv)
    env.host_string = 'root@' + sys.argv[2]
    print(env)

    if len(sys.argv) == 4:
        env.key_filename = [sys.argv[3]]
        streaming(sys.argv[1])
    else:
        streaming(sys.argv[1])
