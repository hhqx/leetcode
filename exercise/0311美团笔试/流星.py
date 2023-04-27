from collections import deque
from math import inf
from typing import *


def max_val(start, end):
    pair = []
    for s, e in zip(start, end):
        pair.append((s, 1))
        pair.append((e, -1))
    pair.sort()

    maxNum = -inf
    maxCnt = 0
    num = 0
    for i, (t, flag) in enumerate(pair):
        choice_cnt = pair[i + 1][0] - t + 1 if i+1 < len(pair) else 0

        num += flag
        if num > maxNum:
            maxCnt = choice_cnt
            maxNum = num
        elif num == maxNum:
            maxCnt += choice_cnt

    return maxNum, maxCnt


n = int(input())
start = list(map(int, input().split(' ')))
end = list(map(int, input().split(' ')))
x, y = max_val(start, end)
print(x, y)
