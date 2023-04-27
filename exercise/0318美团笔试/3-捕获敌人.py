from acm_tools import *

question_str = """
题目：捕获敌人
题目描述
小美在玩一项游戏。该游戏的目标是尽可能抓获敌人。

敌人的位置将被一个二维坐标 (x,y)(x,y)(x,y) 所描述。

小美有一个全屏技能，该技能能一次性将若干敌人一次性捕获。捕获的敌人之间的横坐标的最大差值不能大于 AAA，纵坐标的最大差值不能大于 BBB 。

现在给出所有敌人的坐标，你的任务是计算小美一次性最多能使用技能捕获多少敌人。

输入描述
第一行三个整数 N,A,B，表示共有 N 个敌人，小美的全屏技能的参数 A 和参数 B。

接下来 N 行，每行两个数字 x,y，描述一个敌人所在的坐标。

1 ⩽ N ≤ 500 ， 1 ⩽ A , B ⩽ 1000 ， 1 ⩽ x , y ⩽ 1000 1⩽N≤500，1⩽A,B⩽1000，1⩽x,y⩽1000 1⩽N≤500，1⩽A,B⩽1000，1⩽x,y⩽1000

输出描述
一行，一个整数表示小美使用技能单次所可以捕获的最多数量。

样例1
输入:
3 1 1
1 1
1 2
1 3
输出:
2
说明：最多可以同时捕获两名敌人，可以是 (1,1) 和 )(1,2) 处的敌人，也可以是 (1,2) 和 (1,3) 处的敌人，但不可以同时捕获三名敌人，因为三名敌人时，纵坐标的最大差值是 2，超过了参数 B 的值 1。

样例2
输入:
5 1 2
1 1
2 2
3 3
1 3
1 4
输出:
3
说明：最多同时捕获三名敌人。其中一种方案如下: 捕获 (1,1)，(1,3)，(2,2) 处的三个敌人。
"""
load_test_str(question_str)

#### START ###
from math import inf


def func_0(Points, A, B):
    """ 理解错题目意思 """
    n = len(Points)

    # o(N*N) 遍历建图
    graph = [[] for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            x, y = Points[i], Points[j]
            if abs(x[0] - y[0]) <= A and abs(x[1] - y[1]) <= B:
                graph[i].append(j)
                graph[j].append(i)

    # dfs求最大连通域
    visisted = set()
    maxN = -inf

    def dfs(u, cnt):
        nonlocal maxN
        cnt += 1
        maxN = max(maxN, cnt)
        for v in graph[u]:
            if v not in visisted:
                visisted.add(v)
                dfs(v, cnt)

    # dfs
    for i in range(n):
        if i in visisted:
            continue
        visisted.add(i)
        dfs(i, 0)

    return maxN


def func_1(Points, A, B):
    """ 二维前缀和遍历所有大小为A*B的矩形区域 """
    n, m = max(x for x, y in Points) + 1, max(y for x, y in Points) + 1
    a = dict()
    for x, y in Points:
        a[(y, x)] = a.get((y, x), 0) + 1
    ans = 0

    # 求二维前缀和
    grid = [[0] * n for _ in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            grid[i][j] = grid[i - 1][j] + grid[i][j - 1] + a.get((i, j), 0) - grid[i - 1][j - 1]

    # for row in grid:
    #     sprint(row)
    # 遍历
    A, B = min(A + 1, n - 1), min(B + 1, m - 1)
    for i in range(B, m):
        for j in range(A, n):
            val = grid[i][j] + grid[i - B][j - A] - grid[i - B][j] - grid[i][j - A]
            ans = max(ans, val)

    return ans


# func = func_0
func = func_1


def main():
    N, A, B = list(map(int, input().split(' ')))
    Point = []
    for _ in range(N):
        row = list(map(int, input().split(' ')))
        Point.append(row)
    ret = func(Point, A, B)
    print(ret)


main()
#### END ###
while True:
    try:
        main()
    except:
        break
