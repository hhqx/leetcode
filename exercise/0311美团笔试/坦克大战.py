from collections import deque
from math import inf
from typing import *


def game(cmdD, cmdW):
    m, n = 16, 16
    d = (0, 0, 'R')
    w = (15, 15, 'L')
    mark = {(0, 0): 'd', (15, 15): 'w'}
    def is_shooted(a, b):
        """ a 是否被 b 打中 """
        ax, ay, adir = a
        bx, by, bdir = b
        if bdir == 'U' and ay==by and ax > bx:
            return True
        if bdir == 'D' and ay==by and ax < bx:
            return True
        if bdir == 'L' and ax==bx and ay < by:
            return True
        if bdir == 'R' and ax==bx and ay > by:
            return True

    get_dir = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1), }

    d_dead = -1
    w_dead = -1
    for t, (dcmd, wcmd) in enumerate(zip(cmdD, cmdW)):
        if dcmd == 'F':
            if is_shooted(w, d):
                w_dead = t
        else:
            # d next
            dx, dy = get_dir[dcmd]
            nxt_dir = d[2]
            dnxt = [d[0] + dx, d[1] + dy, d]

        if wcmd == 'F':
            if is_shooted(d, w):
                d_dead = t




        if d_dead != -1 or w_dead != -1:
            if d_dead != -1 and w_dead != -1:
                return t+1, 'P'
            if d_dead != -1:
                return t+1, 'W'
            if w_dead != -1:
                return t+1, 'D'

    # 统计占领区域判断赢家
    dcnt = sum(v == 'd' for v in mark.values())
    wcnt = sum(v == 'w' for v in mark.values())
    if dcnt == wcnt:
        return 256, 'P'
    elif dcnt > wcnt:
        return 256, 'D'
    else:
        return 256, 'W'


cmdD = input()
cmdW = input()
round, winner = game(cmdD, cmdW)
print(round)
print(winner)
