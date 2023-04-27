"""


"""
import heapq
from collections import defaultdict


def func(arr, k):
    """ 计算顺子子数组 """
    n, ans = len(arr), 0

    d, double_cnt = defaultdict(int), 0

    q1, q2 = [], []
    for i, num in enumerate(arr):
        heapq.heappush(q1, (-num, num, i))
        heapq.heappush(q2, (num, num, i))

        # 得到区间最大最小值
        mx, mn = q1[0][1], q2[0][1]
        # print(double_cnt, mx, mn)

        # 确保区间无重复元素
        d[num] += 1
        if d[num] == 2:
            double_cnt += 1
        if i - 0 + 1 >= k:
            if double_cnt == 0 and mx - mn + 1 == k:
                ans += 1

            j = i - k + 1
            d[arr[j]] -= 1
            if d[arr[j]] == 1:
                double_cnt -= 1

        while q1 and i - q1[0][-1] + 1 >= k:
            heapq.heappop(q1)
        while q2 and i - q2[0][-1] + 1 >= k:
            heapq.heappop(q2)

    return ans


arr = [1, 2, 2, 3, 4]
# 1, 2, 3, 4
k = 2

ret = func(arr, k)
print(ret)
