"""
米小游拿到了一个仅由小写字母组成的字符串，她准备进行恰好一次操作: 交换两个相邻字母，在操作结束后使得字符串的字典序尽可能大。请你输出最终生成的字符串。

输入描述:
一个仅由小写字母组成的字符串，长度不小于2, 不超过200000。

输出描述:
操作后的字符串。

"""
from collections import defaultdict


def max_swap(s):
    """ 交换相邻ascii码的字符一次 """
    n = len(s)
    first, last = defaultdict(int), defaultdict(int)
    for i in range(n):
        if s[i] not in first:
            first[s[i]] = i

    for i in range(n - 1, -1, -1):
        if s[i] not in last:
            last[s[i]] = i

    # 针对交换后变大的情况
    for i in range(n):
        c = s[i]
        next_c = chr(ord(c) + 1)
        if next_c in last and last[next_c] > i:
            # swap
            j = last[next_c]
            return s[:i] + s[j] + s[i + 1:j] + s[i] + s[j + 1:]

    # 针对交换后变小的情况
    pair = None
    for i in range(n):
        c = s[i]
        next_c = chr(ord(c) - 1)
        if next_c in first and first[next_c] > i:
            # store swap pair
            pair = [i, next_c]

    if pair:
        i, j = pair
        return s[:i] + s[j] + s[i + 1:j] + s[i] + s[j + 1:]

    # 若无法交换, 返回原串
    return s


def max_swap(s):
    """ 交换相邻位置的字符一次 """
    for i in range(len(s)):
        if i == len(s) - 1 or s[i] < s[i + 1]:
            j = i + 1
            return s[:i] + s[j] + s[i + 1:j] + s[i] + s[j + 1:]
    return None


s = input()
ret = max_swap(s)
print(ret)
