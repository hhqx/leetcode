"""
米小游希望你构造一个长度为n的数组，满足以下条件:
1.所有元素的绝对值不大于3
2.相邻两个元素的乘积小于0，且和不为0
3.所有元素之和等于0。
你能帮帮她吗?

输入描述:
一个正整数n。
2 <= n <= 10^5

输出描述:
如果无解，请输出一个字符串"No Answer”否则输出n个整数。有多解输出任意即可。

"""

"""
[-3, 3]
相邻元素符号相反, 绝对值不相等, 且无元素为零
元素和为零

-3: 2, 1
-2: 3, 1
-1: 3, 2

n==3
-1, 3, -2
1, -3, 2


n==4
-2, 3, -2, 1

n==5
-2, 3, -2, 3, -2

"""

import itertools


def get_all(n):
    choice = [-3, -2, -1, 1, 2, 3]
    itertools.permutations(choice, n)
    N = len(choice)
    ans = []
    for i in range(N ** n):
        tmp = []
        num = i
        for _ in range(n):
            num, digit = divmod(num, N)
            tmp.append(choice[digit])
            if len(tmp) >= 2 and (tmp[-1] * tmp[-2] > 0 or abs(tmp[-1]) == abs(tmp[-2])):
                break
        else:
            if sum(tmp) == 0:
                ans.append(tmp)

    return ans


for i in range(3, 5 + 1):
    ret = get_all(i)
    print(i, ret)

"""
[-1, 3, -2] [1, -3, 2]

[1, -2, 3, -2] [-1, 2, -3, 2]

[1, -3, 1, -2, 3] [-1, 3, -1, 2, -3]

n == 2时, No Answer.
n >= 3时
用 [-1, 3, -2] [1, -3, 2] 重复构造至剩余长度为4,或5
1. 若剩余为4, 根据最后一个数为-2或2分别追加 [1, -2, 3, -2] 和 [-1, 2, -3, 2]
2. 若剩余为5, 根据最后一个数为-2或2分别追加 [1, -3, 1, -2, 3] 和 [-1, 3, -1, 2, -3]

"""

n = int(input())
if n == 2:
    print("No Answer")
else:
    ans = []
    while n - len(ans) >= 6:
        if not ans or ans[-1] == -2:
            ans.extend([1, -3, 2])
        else:
            ans.extend([-1, 3, -2])

    if n - len(ans) == 3:
        if not ans or ans[-1] == -2:
            ans.extend([1, -3, 2])
        else:
            ans.extend([-1, 3, -2])
    elif n - len(ans) == 4:
        if not ans or ans[-1] == -2:
            ans.extend([1, -2, 3, -2])
        else:
            ans.extend([-1, 2, -3, 2])
    elif n-len(ans) == 5:
        if not ans or ans[-1] == -2:
            ans.extend([1, -3, 1, -2, 3])
        else:
            ans.extend([-1, 3, -1, 2, -3])

    print(*ans)

