from acm_tools import *

test_case = """
输入:
9
输出:
1




"""
load_test_str(test_case)

from math import inf
from math import sqrt

"""
考虑每个质因子的组成
2, 3, 5

对于2, a,b,c要么全奇数, 要么全偶数

先考虑偶数
0, 2, 4

因子2
0, 0, 0
2, 2, 2
4, 4, 4

因子3

因子5

"""

def func():


    def issquare(x):
        s = int(sqrt(x)) ** 2 == x
        return s

    def get_square():
        ret = set(i*i for i in range(n+1))
        return ret

    def count(n):
        val = sum(
            1 for c in range(1, n + 1) for b in range(1, c) for a in range(1, b)
            if (a*b) in S and (b * c) in S and a*c in S
        )

        return val

    #     for c in range(1, n+1):
    #         for b in range(1, c):
    #             for a in range(1, b):
    #                 if int(sqrt(x)) **  2 == x

    n = int(input())

    S = get_square()
    # dprint(get_square())

    ret = count(n)

    # print(ret)
    return ret


def main():
    ret = func()
    print(ret)


main()
### end ###
while True:
    try:
        main()
    except:
        break
