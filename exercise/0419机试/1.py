import itertools

from acm_tools import *
test_case="""
输入:
2
2 5
8 9
输出:
20

输入:
3
4 8
1 6
2 9
输出:
34
"""
load_test_str(test_case)

## start



from math import inf
from itertools import accumulate
def func():
    """ 1, 3, 4 """
    n = int(input())
    data = []
    # for i in range(n):
    #     row = list(map(int, input().strip().split()))
    #     data.append(row)
    # n = len(data)
    a = [0] * (int(10 ** 6) + 2)
    # a = defaultdict(int)
    maxT = -inf
    minT = inf
    # for s, e in data:
    for _ in range(n):
        s, e = list(map(int, input().strip().split()))
        if s < minT:
            minT = s
        if e > maxT:
            maxT = e
        a[s] += 1
        a[e + 1] -= 1

    # p = a
    # for i in range(minT+1, maxT+1):
    #     p[i] = p[i-1] + p[i]
    p = list(accumulate(a))

    # ans = 0
    # for t in range(minT, maxT+1):
    #     if p[t] == 0:
    #         ans += 1
    #     elif p[t] == 1:
    #         ans += 3
    #     else:
    #         ans += 4
    ans = 0
    ans += sum(1 if pp == 0 else (3 if pp == 1 else 4) for pp in p[minT: maxT+1])

    return ans

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
