from acm_tools import *

question_str = """
输入:
5
4 9 5 2 2 1 3 5 1 4
输出:
2
"""
load_test_str(question_str)


def func():
    n = int(input())
    arr = list(map(int, input().split()))
    item = [[arr[2 * i], arr[2 * i + 1]] for i in range(n)]

    item.sort(key=lambda x: tuple(x))
    dprint(arr)

    cnt = 0
    while item:
        st = []
        left = []
        for i, (x, y) in enumerate(item):
            if not st or x >= st[-1][0] and y >= st[-1][1]:
                st.append((x, y))
            else:
                left.append((x, y))

        item = left
        cnt += 1

    print(cnt)
    return cnt


func()

#### START ###


#### END ###
