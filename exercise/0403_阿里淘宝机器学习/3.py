from acm_tools import *

question_str = """
小红拿到了一张无向连通图 (可能有重边和自环)，共有n个节点和m条边，她想额外再连一条边，使得连边后1号点到n号点的最短路变成K。
小红想知道，有多少种连边方式?
注:连的新边也可以是自环或者是重边，但<x, y>和<y, x>视为同一种连边方式

输入描述
第一行输入三个正整数n,m,k。
接下来的m行，每行输入两个正整数x和y，代表x和y有一条边连接。
1 <= k <= n <10**3
1 <= m <= 10**5
1 < x,y <= n
输出描述
一个整数，代表连边方案数。
示例1
输入:
4 3 2
1 2
2 3
3 4
输出:
2

"""
load_test_str(question_str)

#### START ###
from heapq import heappop, heappush
from math import inf


def func(edge, n, k):
    """ 复杂度 o(n*n+m) """
    g = [[] for _ in range(n)]
    for u, v in edge:
        if u == v:
            continue
        g[u - 1].append(v - 1)
        g[v - 1].append(u - 1)

    def min_dis(start, n):
        """ 堆优化的dijstra算法"""
        h = [(0, start)]
        mdis = [inf] * n
        while h:
            dis, u = heappop(h)
            if dis < mdis[u]:
                mdis[u] = dis
            else:
                continue
            for v in g[u]:
                heappush(h, (dis + 1, v))
        return mdis

    mdis0 = min_dis(0, n)
    # 若最短距离小于k, 返回0
    if mdis0[n - 1] < k:
        return 0
    mdis1 = min_dis(n - 1, n)
    # print_std('dis0', mdis0)
    # print_std('dis1', mdis1)
    ans = 0
    for i in range(n):
        for j in range(i, n):
            if i == j:
                # 自环
                if mdis0[i] + mdis1[j] == k:
                    ans += 1
            else:
                # 重边或新边
                if mdis0[i] + mdis1[j] + 1 == k:
                    ans += 1

    return ans


def main():
    n, m, k = list(map(int, input().split()))
    edge = []
    for _ in range(m):
        row = list(map(int, input().split()))
        edge.append(row)
    ret = func(edge, n, k)
    print(ret)


main()

#### END ###
