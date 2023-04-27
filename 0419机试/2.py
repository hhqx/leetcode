import itertools

from acm_tools import *

test_case = """

输入:
4
3
0 1
0 2
0 3
1
2
输出:
0->1

输入:
2
1
0 1
1
1
输出:
NULL

输入:
4
3
0 1
0 2
0 3
2
2
3
输出:
0->1

输入:
7
6
0 1
0 3
1 2
3 4
1 5
5 6
1
4
输出:
0->1->2

"""
load_test_str(test_case)

## start


from math import inf
from itertools import accumulate
from collections import deque


def func():
    ans = ""
    n = int(input())
    m = int(input())
    g = [[] for _ in range(n)]
    for _ in range(m):
        u, v = list(map(int, input().strip().split()))
        g[u].append(v)
        g[v].append(u)
    block = set()
    for _ in range(int(input())):
        val = int(input())
        block.add(val)

    if 0 in block:
        return "NULL"
    if n == 1:
        return "0"

    # bfs
    ret = []
    q = deque([[0, [0]]])
    vis = set([0])
    while q:
        for _ in range(len(q)):
            u, path = q.popleft()
            if len(g[u]) == 1 and u != 0:
                ret = map(str, path)
                return "->".join(ret)

            for v in g[u]:
                if v in vis:
                    continue
                vis.add(v)
                if v in block:
                    continue
                q.append([v, path + [v]])

    return "NULL"


def main():
    ret = func()
    print(ret)


if __name__ == "__main__":
    main()

## end
while True:
    try:
        main()
    except:
        break
