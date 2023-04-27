"""
6 2
b 1
m 1 100
m 1 2000
m 1 100
b 2
m 2 10

2010

6 2
b 1
b 2
m 2 20
b 2
m 1 40
m 2 10

40

6 2
b 1
b 2
m 2 20
b 2
m 1 30
m 2 20

40

5 2
b 1
b 2
m 1 10
m 2 20
m 2 30

30
"""
from collections import defaultdict
from math import inf


def func(data):
    n = len(data)
    s = dict()
    # dp[i] 表示 arr[:i] 中所能获得的最大分数
    dp = [0] * (n + 1)
    for i in range(n):
        d = data[i]
        row = [d[0]] + list(map(int, d[1:]))
        if row[0] == 'b':
            x = row[1]
            s[x] = i
            dp[i + 1] = dp[i]
        else:
            x, y = row[1:]
            if x in s:
                # dp[i + 1] = dp[s[x] + 1] + y
                dp[i + 1] = max(dp[s[x] + 1] + y, dp[i])
            else:
                dp[i + 1] = dp[i]

    return max(dp)


def func1(data):
    n = len(data)
    start = defaultdict(list)
    end = defaultdict(list)
    for i in range(n):
        d = data[i]
        row = [d[0]] + list(map(int, d[1:]))
        if row[0] == 'b':
            x = row[1]
            start[x].append(i)
        else:
            x, y = row[1:]
            end[x].append([i, y])

    # 列出所有可能的交易
    intervals = []
    for stone in end:
        if stone not in start:
            continue
        segs = [[l, r, w] for r, w in end[stone] for l in start[stone] if l < r]
        intervals.extend(segs)

    # 找最大不重合区间的分数值
    intervals.sort(key=lambda x: x[1])
    dp = defaultdict(int)
    mx = -inf
    for l, r, w in intervals:
        dp[r] = max(dp[l - 1] + w, mx)
        mx = max(dp[r], mx)

    return max(dp.values())


while True:
    try:
        n, m = map(int, input().split(' '))
        data = []
        for _ in range(n):
            row = list(map(str, input().split(' ')))
            data.append(row)
        ret = func(data)
        print(ret)
    except:
        break
