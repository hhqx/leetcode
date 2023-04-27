from collections import deque
from functools import cache
from typing import *


def best_plan(color, mat, k):
    """ 返回可获得最大金币个数,  """
    m, n = len(color), len(color[0])
    ans = 0

    @cache
    def dfs(i, j, coins):
        """ coins 是已收集到的金币数量 """
        nonlocal m, n, k, ans
        if i >= m or j >= n:
            return
        if coins < 0:
            return

        coins += mat[i][j]
        ans = max(ans, coins)

        for x, y in ((i+1, j), (i, j+1)):
            if x < m and y < n:
                nxt_coins = coins
                if color[i][j] != color[x][y]:
                    nxt_coins -= k

                dfs(x, y, nxt_coins)

        return

    dfs(0, 0, 0)
    return ans


"""
3 3 3
BBR
BRB
RBB
0 1 10
2 10 100
10 100 100
"""

m, n, k = list(map(int, input().split(' ')))
color = []
for _ in range(m):
    color.append(input())

mat = []
for _ in range(m):
    row = list(map(int, input().split(' ')))
    mat.append(row)

ret = best_plan(color, mat, k)
print(ret)