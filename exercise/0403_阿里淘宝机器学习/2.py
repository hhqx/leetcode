from acm_tools import *

question_str = """
给定一个正整数n，你需要求出有多少四元组(A,B,C,D)满足(A+B)x(C+D)=n。
A,B,C,D必须都是正整数。

输入描述
一个正整数n。
2 <= n <= 10**12
输出描述
四元组的数量。

示例1
Input:
6
Output:
4
说明
共有以下4个四元组满足要求:
(1,1,1,2),(1,1,2,1),(1,2,1,1),(2,1,1,1)
"""
load_test_str(question_str)

#### START ###
from math import sqrt


def get_pairs(x):
    """ 复杂度 sqrt(n) """
    ans = [(i, x // i) for i in range(2, int(sqrt(x)) + 1) if x % i == 0]
    return ans


ans = 0
for a, b in get_pairs(int(input())):
    if a == b:
        ans += (a - 1) * (b - 1)
    else:
        ans += 2 * (a - 1) * (b - 1)
print(ans)
#### END ###
