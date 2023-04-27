"""


"""
from functools import cache

"""


"""

"""


"""

from functools import cache


def answer(arr, queries):
    """ 背包 """
    n = len(arr)
    arr = [x * x for x in arr]

    @cache
    def dp(x, n):
        if n <= 0 or x <= 0:
            return 0

        return max(dp(x - arr[n - 1], n - 1) + 1, dp(x, n - 1))

    ans = [dp(q, n) for q in queries]
    dp.cache_clear()
    return ans


n, m = list(map(int, input().split(' ')))
arr = list(map(int, input().split(' ')))
queries = list(map(int, input().split(' ')))
ret = answer(arr, queries)
print(*ret)  # 1 1 2 3 3
