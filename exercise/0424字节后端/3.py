from acm_tools import *

test_case = """
输入:
8
3 7 2 1 6 5 4 8
输出:
7 3 6 5 2 1 8 4



"""
load_test_str(test_case)

from math import inf

from heapq import *


def func():
    n = int(input())
    arr = list(map(int, input().split()))

    left = [2] * (n + 1)

    for i in range(n):
        mx = max(arr[i:i + 3])
        if mx == arr[i]:
            continue
        if i + 1 < n and mx == arr[i + 1]:
            if left[arr[i]] > 0 and left[arr[i + 1]] > 0:
                left[arr[i]] -= 1
                left[arr[i + 1]] -= 1
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        elif i + 2 < n and mx == arr[i + 2]:
            if left[arr[i]] > 0 and left[arr[i + 1]] > 0 and left[arr[i + 2]] > 1:
                left[arr[i]] -= 1
                left[arr[i + 2]] -= 2
                left[arr[i + 1]] -= 1
                arr[i], arr[i + 1], arr[i + 2] = arr[i + 2], arr[i], arr[i + 1]
            elif left[arr[i]] > 0 and left[arr[i + 1]] > 0:
                left[arr[i]] -= 1
                left[arr[i + 1]] -= 1
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr


ret = func()
print(*ret)

### end ###
# while True:
#     try:
#         main()
#     except:
#         break
