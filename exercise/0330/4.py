import re

from acm_tools import *

"""
5
3
3 3 2
4
1 3 1 3
5 4 1 5 3 2
4
2 4 1 2

1
2
4
3

"""
from collections import deque

STD_IN = """
4
3
3 3 2
4
1 3 1 3
6
5 4 1 5 3 2
4
2 4 1 2
"""
STD_OUT = """
1
2
4
3
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
1


"""
load_test_str(test_str)


# load_test_case(STD_IN, STD_OUT)

def exec_pyfile(file=__file__):
    # 提取需要执行的代码行
    extracted_lines = []
    with open(file, 'r', encoding='utf-8') as f:
        start = False
        for line in f:
            start |= line.strip().startswith('#### START')
            if not start:
                extracted_lines.append("\n")
                continue
            extracted_lines.append(line)
            if line.strip().startswith('#### END'):
                break
    extracted_code = ''.join(extracted_lines)

    # 将代码行放在函数内
    exec(extracted_code)
    exit(0)
exec_pyfile()

#### START 代码从这里开始 ###

def func(arr):
    # assert 0, "test error"
    return 0


for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    ret = func(arr)
    print(ret)

#### END 代码在这里结束 ###
