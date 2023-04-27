"""
现在存在m个房间，有n个人需要入住，需要列出所有房间入住可以安排的情况假设每个房间可以入住的人数限制为5人。
限制条件，为了公平起见，不能存在个房间的人数比别的房间的人数多2个。输出的组合中房间敏感的，即1.1.2组合和2.1.1组合是不同的组合，都需要输出，1,1,2组合代表第一个房间住1个人，第二个房间住1个人，第三个房间住2个人，而2,1,1组合代表第一个房间住2个人，第二房间住1个人，第三个房间住1个人

输入描述
输入房间数和入住人数，中间用逗号分隔
输出描述
第一行输土剩余没有安排人员的数巨第二行输出有几种安排情况参数异常输出invelld

输入:
3 20
输出:
5
5,5,5
输入:
6 11
输出:
0
1,2,2,2,2,2
2,1,2,2,2,2
2,2,1,2,2,2
2,2,2,1,2,2
2,2,2,2,1,2
2,2,2,2,2,1
"""

import itertools


def func(m=6, n=11):
    """ n个人, m个房间 """
    if m == 0:
        print("invalid")
        return

    small = n // m
    if n % m == 0:
        large = small
    else:
        large = small + 1
    small_cnt = large * m - n
    if small > 5:
        small = 5
        left = n - m * small
        print(left)
        print(",".join(map(str, [small] * m)))
        return

    print(0)
    for selected in itertools.combinations(range(m), small_cnt):
        tmp = [large] * m
        for i in selected:
            tmp[i] = small
        print(",".join(map(str, tmp)))
        assert sum(tmp) == n, ""


for m, n in ((3, 20), (6, 11), (6, 10), (2, 3), (1, 3), (1, 6), (0, 3)):
    print("m={}, n={}, 的结果为: ".format(m, n))
    func(m, n)
