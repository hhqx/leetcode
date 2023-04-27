from acm_tools import *

test_case = """
输入:
3 3 1 1
10 2 0
-2 2 1
2 1 2
输出:
1 1

输入:
3 3 2 2
1 2 0
-2 2 1
2 1 2
输出:
2 2



"""
load_test_str(test_case)

from math import inf


def func():
    m, n, x0, y0 = map(int, input().split())
    mat = []
    for i in range(m):
        row = list(map(int, input().split()))
        mat.append(row)

    # 滑动窗口
    pair = []
    for i in range(m):
        #
        tmp = []
        row_cnt = 0
        row_val = 1
        for j in range(n):
            if not mat[i][j]:
                row_cnt += 1
            else:
                row_val *= mat[i][j]

            if j - y0 >= 0:
                if not mat[i][j - y0]:
                    row_cnt -= 1
                else:
                    row_val //= mat[i][j - y0]
            if j >= y0 - 1:
                tmp.append((row_val, row_cnt))
        pair.append(tmp)

    # dprint(pair)

    #
    maxval = -inf
    ans = [-1, -1]
    #
    val = [1] * n
    zero_cnt = [0] * n
    for i in range(m):
        item = pair[i]
        for j in range(len(item)):
            v, cnt = item[j]
            zero_cnt[j] += cnt
            val[j] *= v

        if i - x0 >= 0:
            item = pair[i - x0]
            for j in range(len(item)):
                v, cnt = item[j]
                zero_cnt[j] -= cnt
                val[j] //= v

        if i >= x0 -1:
            for j in range(len(item)):
                total = val[j] if not zero_cnt[j] else 0
                if total > maxval:
                    # dprint(maxval, total, i)
                    maxval = total
                    ans = [i-x0 +1, j]

    # ans = []
    return [ans[0]+1, ans[1] + 1]


def main():
    ret = func()
    print(*ret)


main()
### end ###
while True:
    try:
        main()
    except:
        break
