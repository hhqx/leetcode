from collections import deque
from typing import *


def fair_path(n: int, edge: List[int]):
    ans = 0
    g = [[] for _ in range(n)]
    for u, v in edge:
        g[u-1].append(v)
        g[v-1].append(u-1)

    roots = [i for i in range(n) if len(g[i]) >= 3]
    for root in roots:
        start = [(idx, node) for idx, node in enumerate(root)]
        q = deque(start)
        vis = set(node for _, node in start)
        depth = 0
        while q:
            for _ in range(len(q)):
                idx, u = q.popleft()

                for v in g[u]:
                    if v not in vis:
                        vis.add(v)
                        q.append([idx, v])

            depth += 1


    return ans




n = int(input())
edge = [[i+2, nodeid] for i, nodeid in enumerate(map(int, input().split(' ')))]
ret = fair_path(n, edge)
print(ret)
