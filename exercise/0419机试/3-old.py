import bisect
import itertools

from acm_tools import *

test_case = """
输入:
1 5 3 3 5 5 1
输出:
6 10

输入:
1 6 5 4 6 3 6 7 7 2 4 3
输出:
9 4 15 1

输入:
1 5 3 4 6 5 1
输出:
4 14




"""
load_test_str(test_case)

## start


from math import inf
from itertools import accumulate
from collections import deque, defaultdict

# def dprint(*args):
#     return
# def sprint(*args):
#     return

def func():
    arr = list(map(int, input().strip().split()))
    i = 0
    while i+1 < len(arr) and arr[i+1] <= arr[i]:
        i += 1
    j = len(arr)-1
    while j-1 >= 0 and arr[j-1] <= arr[j]:
        j -= 1
    arr = arr[i:j+1]
    dprint('arr', arr)

    # 找底边
    bottom = []
    for i in range(1, len(arr)-1):
        if arr[i-1] < arr[i] and arr[i] >= arr[i+1]:
            bottom.append(i)

    # 统计水流
    water = defaultdict(list)
    for i in range(1, len(arr) - 1):
        idxr = bisect.bisect_right(bottom, i)
        # r = arr[bottom[idxr]]
        idxl = bisect.bisect_left(bottom, i)-1
        # l = arr[bottom[idxl]]

        if not (arr[i-1] >= arr[i]) and not (arr[i] < arr[i + 1]):
            bottom_idx = i
        elif (arr[i-1] >= arr[i]) and (arr[i] < arr[i + 1]):
            l, r = bottom[idxl], bottom[idxr]
            if arr[l] > arr[r]:
                bottom_idx = l
            else:
                bottom_idx = r
        elif arr[i-1] >= arr[i]:
            bottom_idx = bottom[idxl]
        else:  #  arr[i] < arr[i + 1]:
            bottom_idx = bottom[idxr]
        # else:  # arr[i-1] >= arr[i]:

        water[bottom_idx].append(arr[i])
    sprint(water)

    mn_idx = min(range(1, len(arr)-1), key=lambda idx: arr[idx])
    ans = []
    for i, k in enumerate(sorted(water)):
        v = water[k]
        if arr[mn_idx] < arr[0] or arr[mn_idx] < arr[-1]:
            if k < mn_idx:
                bias = max(arr[0], arr[mn_idx])
            else:
                bias = max(arr[-1], arr[mn_idx])
        else:
            bias = max(arr[0], arr[-1])
        val = sum(x - bias for x in v)
        ans.append(str(val))
    return " ".join(ans)


def main():
    ret = func()
    print(ret)


if __name__ == "__main__":
    main()

## end
while True:
    try:
        main()
    except:
        break
