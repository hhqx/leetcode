"""


"""
import heapq
from collections import defaultdict


def arear_cnt(m, n, lines):
    def f(line, x):
        x1, y1, x2, y2 = line
        k = (y1 - y2) // (x1 - x2)
        y = (x - x1) * (y1 - y2) // (x1 - x2) + y1
        return y, k

    grid = [[1] * (3 * n) for _ in range(3 * m)]
    POINTS = [
        [],
        [[0, 0], [1, 1], [2, 2], ],  # k=1
        [[0, 2], [1, 1], [2, 0], ],  # k=-1
        [[0, 0], [1, 1], [2, 2], [0, 2], [2, 0], ],  # k=1 or k=-1
    ]
    flag = [[0] * n for _ in range(m)]
    for line in lines:
        for j in range(n):
            i, k = f(line, j)
            if 0 <= i < m:
                flag[i][j] |= 1 if k == 1 else 2

    for i in range(m):
        for j in range(n):
            for di, dj in POINTS[flag[i][j]]:
                grid[3 * i + di][3 * j + dj] = 0

    for row in grid:
        print(*row)

    # dfs 求grid的连通域
    def dfs(x, y):
        for i, j in ((x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y),):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and (i, j) not in vis and grid[i][j] == 1:
                vis.add((i, j))
                dfs(i, j)

    vis = set()
    cnt = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i, j) in vis or grid[i][j] == 0:
                continue
            cnt += 1
            vis.add((i, j))
            dfs(i, j)

    return cnt


h, w = list(map(int, input().split(' ')))
lines = []
for _ in range(int(input())):
    x1, y1, x2, y2 = list(map(int, input().split(' ')))
    lines.append([x1, y1, x2, y2])
ret = arear_cnt(h + 1, w + 1, lines)
print(ret)
