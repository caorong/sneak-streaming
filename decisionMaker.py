#!/usr/bin/env python3
# coding=utf-8

import operator

import common

live_priority = {}

# list to map value 小的优先级更高
map(lambda (x,y): operator.setitem(live_priority, y, x), enumerate(common.watchlist))
watchlist = common.watchlist


def make_decision(watchlist_previous, watchlist_now):
    previous_top = now_top = 99
    if watchlist_now:
        if watchlist_previous:
            previous_top = min(map(lambda x:live_priority.get(x, 99), watchlist_previous))
            # print(previous_top)
        if watchlist_now:
            now_top = min(map(lambda x:live_priority.get(x, 99), watchlist_now))
            # print(now_top)
        print(previous_top, now_top)
        if now_top < previous_top:
            return now_top
    return None


if __name__ == '__main__':
    print(live_priority)
    print(make_decision(['sc2creator','egjd'], ['sc2rain', 'forgg']))
    print(make_decision([], ['sc2rain', 'forgg']))
    
