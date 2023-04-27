from collections import deque
from typing import *


def Min_Change(s: str):
    n = len(s)
    start = -1
    ans = 0
    for i, c in enumerate(s):
        if i == n-1 or s[i] != s[i+1]:
            cnt = i - start
            start = i
            ans += cnt - 1

    return ans




# s = int(input())
s = "111222333444"  # 结果为8
ret = Min_Change(s)
print(ret)
