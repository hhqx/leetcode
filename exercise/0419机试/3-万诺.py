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

"""
l >= cur and r >= cur
比较左bottom和右bottom, 取大值, 若一样取左

# 向更深处引流, 取大于等于当前点的第一个bottom
l >= cur and r < cur
l < cur and r >= cur

l < cur and r < cur
"""


def func_wangnuo():
    nums = [int(c) for c in input().split(" ")]

    yinlius = []

    for i in range(1, len(nums) - 1):
        if nums[i] > nums[i - 1] and nums[i] >= nums[i + 1]: yinlius.append(i)

    ans = [0 for _ in range(len(yinlius))]

    for i in range(len(yinlius) - 1):
        for j in range(yinlius[i] + 1, yinlius[i + 1]):
            if nums[yinlius[i]] > nums[yinlius[i + 1]]:
                ans[i] += nums[j] - 1
            elif nums[yinlius[i]] < nums[yinlius[i + 1]]:
                ans[i + 1] += nums[j] - 1
            else:
                if nums[j] >= nums[j - 1]:
                    ans[i + 1] += nums[j] - 1
                else:
                    ans[i] += nums[j] - 1

    for j in range(yinlius[0]):
        ans[0] += nums[j] - 1

    for j in range(yinlius[-1] + 1, len(nums)):
        ans[-1] += nums[j] - 1

    for i in range(len(ans)):
        ans[i] += nums[yinlius[i]] - 1

    print(str(ans)[1:-1].replace(",", ""))


def func():
    arr = list(map(int, input().strip().split()))
    i = 0
    while i + 1 < len(arr) and arr[i + 1] <= arr[i]:
        i += 1
    j = len(arr) - 1
    while j - 1 >= 0 and arr[j - 1] <= arr[j]:
        j -= 1
    arr = arr[i:j + 1]
    dprint('arr', arr)

    # 找底边
    bottom = []
    flat_bottom = {}
    flat_up = {}
    flat_down = {}
    lastb = -1
    for i in range(1, len(arr) - 1):
        if arr[i - 1] < arr[i] and arr[i] >= arr[i + 1]:
            bottom.append(i)
            lastb = i
        elif arr[i - 1] == arr[i] and lastb == i - 1:
            flat_bottom[i] = bottom[-1]
            lastb = i

    # 统计水流
    water = defaultdict(list)
    for i in range(1, len(arr) - 1):
        if i in flat_bottom:
            water[flat_bottom[i]].append(arr[i])
            continue

        idxr = bisect.bisect_left(bottom, i)
        # r = arr[bottom[idxr]]
        idxl = bisect.bisect_right(bottom, i) - 1
        # l = arr[bottom[idxl]]

        cur, l, r = arr[i], arr[i - 1], arr[i + 1]
        if l > cur >= r or i in flat_up:
            lidx = bottom[idxl]
            bottom_idx = lidx
        elif l <= cur < r or i in flat_down:
            ridx = bottom[idxr]
            bottom_idx = ridx
        elif l >= cur and r >= cur:  # 在取鞍点且取等号时有问题
            lidx = bottom[idxl]
            ridx = bottom[idxr]
            if arr[lidx] >= arr[ridx]:
                bottom_idx = lidx
            else:
                bottom_idx = ridx

        else:  # l < cur and r < cur
            assert i in bottom, "error"
            bottom_idx = i

        water[bottom_idx].append(arr[i])
    sprint(water)

    # 计算水平线深度
    depth = [0] * len(arr)
    mn = inf
    for i, num in enumerate(arr):
        mn = min(mn, num)
        depth[i] = mn
    mn = inf
    for i in range(len(arr) - 1, -1, -1):
        mn = min(mn, arr[i])
        depth[i] = max(depth[i], mn)

    # 计算每部分区域的引水量
    ans = []
    for i, k in enumerate(water):
        v = water[k]
        val = sum(x - depth[k] for x in v)
        ans.append(str(val))
    print(" ".join(ans))
    return


func = func_wangnuo
# func = func


def main():
    ret = func()
    # print(ret)


if __name__ == "__main__":
    main()

## end
while True:
    try:
        main()
    except:
        break
