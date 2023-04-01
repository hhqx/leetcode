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
import bisect

"""


"""

import itertools


def k_sort(arr, k):
    n = len(arr)
    sorted_arr = sorted(arr)  # 对原数列进行排序得到有序数列

    operations = []
    for i in range(n):
        j = bisect.bisect_left(sorted_arr, arr[i])  # 从有序数列中找到第一个大于等于arr[i]的数的位置j
        if i != j:
            operations.append(i)  # 如果i != j，则记录下位置i

    num_operations = 0
    for i in operations:
        num_operations += (i - num_operations) // k  # 计算需要进行的K排序操作次数
        temp = arr.pop(i)
        arr.insert(n - k * (num_operations + 1), temp)  # 将该位置的数移到第j个位置

    return num_operations


def k_sort(arr, k):
    n = len(arr)
    posi = {num: i for i, num in enumerate(arr)}

    seperator = [posi[num] for num in range(1, arr[-1] + 1)]
    issorted = set(seperator)
    ans = 0
    for x in range(arr[-1] + 1, n + 1):
        if x in issorted:
            continue
        else:
            ans += 1

        # 以当前点为起点向左右扩展集合, 扩展集合的条件是: 左右的元素值 = 集合中的最大值+1
        # 扩展后的集合大小最大为k
        l, r = posi[x], posi[x]
        mx = x
        while mx - x + 1 <= k:
            if l - 1 >= 0 and arr[l - 1] == mx + 1:
                mx = mx + 1
                issorted.add(mx)
                l -= 1
            elif r + 1 < n and arr[r + 1] == mx + 1:
                mx = mx + 1
                issorted.add(mx)
                r += 1
            else:
                break
    return ans


# data = []
# for _ in range(int(input())):
#     n, k = list(map(int, input().split(' ')))
#     row = list(map(int, input().split(' ')))
#     data.append([row, k])
data = [
    [[1, 2, 3, 4, 5], 1],
    [[1, 3, 5, 4, 2], 2],
]

for arr, k in data:
    ret = k_sort(arr, k)
    print(ret)  # 0  1
