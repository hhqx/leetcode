"""
时间限制:3000MS内存限制:589824KB
顾目描述:给出一个数组。你需要求出按顺序对其进行一系列区同撞作后最络所得的数组换作有三种:
1. 将下标在L到R之间的元察全部或上X
2. 将下标在L到R之间的元素全部与上X
3. 将下标在L到R之间的元素全部设为X


输入猫述
第一行有一个正整数N(1<=N<=100000)，代表数组的长度
第二行有N个非负整数，范围在0到220-1之间，代表数组中的元素
第三行有一个正整数M(1<=M<=100000)，代表操作次数。
第四行有M个正整数，代表M次操作中的区间左端点L。
第五行有M个正整数，代表M次操作中的区间右端点R
第六行是一个长度为M的字符串，下代表操作1，&代表操作2，=代表操作3.
第七行有M个正整数，代表M次操作中的参数X。

输出描述
在一行中输出N个数，代表所有操作按顺序完成后最终所得的数组。

样例输出:
8 2 2 0
"""
from functools import cache


def operation(arr, left, right, ops, num):
    """ 用位操作写, 测试不通过 """
    n = len(arr)
    m = len(ops)
    NBITS = 30

    # bit = [[arr[j] & (1 << i) for j in range(n)] for i in range(NBITS)]
    # bit[k][i]
    @cache
    def get_mask(l, r):
        mask = 2 ** (r - l + 1) - 1
        mask <<= l
        return mask

    def set(x, l, r, val):
        if val == 0:
            y = x & (C ^ get_mask(l, r))
        else:
            y = x | get_mask(l, r)

        return y

    C = 2 ** (n+1)-1

    bit = []
    for i in range(NBITS):
        tmp = 0
        # for j in range(n-1, -1, -1):
        for j in range(n):
            tmp = (tmp << 1) + (arr[j] & 1)
            arr[j] >>= 1
        bit.append(tmp)

    for op, x, l, r in zip(ops, num, left, right):
        for i in range(NBITS):
            if op == '&':
                if (x >> i) & 1 == 0:
                    bit[i] = set(bit[i], l, r, 0)
            elif op == '|':
                if (x >> i) & 1 == 1:
                    bit[i] = set(bit[i], l, r, 1)
            else:
                bit[i] = set(bit[i], l, r, (x >> i) & 1)

    ans = [0] * n
    for i in range(n):
        for j in range(NBITS-1, -1, -1):
            ans[i] = (ans[i] << 1) + ((bit[j] >> i) & 1)
            # ans[i] = (ans[i] << 1) + (bit[j] & 1)
            # bit[j] >>= 1

    return ans


N = int(input())
arr = list(map(int, input().split(' ')))
M = int(input())
left = list(map(int, input().split(' ')))
right = list(map(int, input().split(' ')))
ops = list(input())
num = list(map(int, input().split(' ')))

# ret = operation(arr, left, right, ops, num)
ret = operation(arr, left[:1], right[:1], ops[:1], num[:1])
print(*ret)
