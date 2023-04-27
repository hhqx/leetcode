from collections import deque, defaultdict
from math import inf
from typing import *


def minString(s):
    s, n = [c for c in s], len(s)

    # 统计不相同的字符对数量
    cnt = sum(s[i] != s[n - 1 - i] for i in range(n // 2))
    if cnt == 0:
        changed = 0
        for i in range(n // 2 + 1):
            if s[i] != 'a':
                s[i] = 'a'
                s[n - 1 - i] = 'a'
                changed += 2
            if changed >= 2:
                break
    elif cnt == 1:
        for i in range(n // 2):
            if s[i] != s[n - 1 - i]:
                if s[i] != 'a' and s[n - 1 - i] != 'a':
                    # 若全不为'a', 两个全置'a'
                    s[i] = 'a'
                    s[n - 1 - i] = 'a'
                    break
                else:
                    # 若有任意一个为'a', 则只需该其中一个, 另外把奇数情况下最中间的字符置'a'
                    s[i] = 'a'
                    s[n - 1 - i] = 'a'
                    if n % 2 == 1:
                        s[n // 2] = 'a'
                    break
    elif cnt == 2:
        # 把不相等的两对置成相同的
        for i in range(n // 2):
            if s[i] != s[n - 1 - i]:
                if s[i] > s[n - 1 - i]:
                    s[i] = s[n - 1 - i]
                else:
                    s[n - 1 - i] = s[i]

    return ''.join(s)


string = input()
ret = minString(string)
print(ret)
