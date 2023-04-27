from collections import deque, defaultdict
from math import inf


def maxLen(colors, k):
    n = len(colors)
    ans = -inf

    # 双指针统计[i, j]区间内的颜色总数
    color_cnt = 0
    d = defaultdict(int)
    i = 0
    for j in range(n):
        d[colors[j]] += 1
        if d[colors[j]] == 1:
            color_cnt += 1
        while color_cnt > k and i < j:
            d[colors[i]] -= 1
            if d[colors[i]] == 0:
                color_cnt -= 1
            i += 1
        ans = max(ans, j - i + 1)

    return ans

n, k = list(map(int, input().split(' ')))
colors = list(map(int, input().split(' ')))
ret = maxLen(colors, k)
print(ret)
