
from typing import *

def combination(n, k):
    def backTracking(n, k):
        if n <= k:
            pass


# def backTracking(n, startIndex):
#
#     if n <= k:
#         pass
#
#     for i in range(startIndex, n):

def combine(n: int, k: int) -> List[List[int]]:
    result = []
    path = []

    def backtracking(n, k, startIndex):
        if k == len(path):
            result.append(path[:])
            return
        for i in range(startIndex, n - (k - len(path)) + 2):
            path.append(i)
            backtracking(n, k, i + 1)
            path.pop()

    backtracking(n, k, 1)
    return result

res = combine(4, 2)
print(res)


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        path = []

        def backtracking(n: int, k: int, startIndex: int):
            if len(path) >= k:
                result.append(path.copy())
                return
            for i in range(startIndex, n - k + 1 + len(path)):
                path.append(i)
                backtracking(n, k, i + 1)
                path.pop()

        backtracking(n, k, 0)
        return result

res = Solution().combine(3, 2)
print(res)
