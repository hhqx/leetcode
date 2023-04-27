from acm_tools import *

"""

"""

test_str = """
Input:
4
3
3 3 2
4
1 3 1 3
6
5 4 1 5 3 2
4
2 4 1 2
Output:
1
2
4
3
Input:
1
1
1
Output:
0


"""
load_test_str(test_str)


#### START 代码从这里开始 ###

def func(arr):
    # assert 0, "test error"
    dprint(arr)
    return 0


def main():
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int, input().split()))
        ret = func(arr)
        print(ret)

while True:
    try:
        main()
    except:
        break

#### END 代码在这里结束 ###
