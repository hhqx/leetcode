from acm_tools import *

question_str = """
输入:
14
0xE77F
输出:
+2
01100010000000
-2
00000110001000
输入:
18
0x677F OxFFFF
输出:
-2
001001100010000000
"""
load_test_str(question_str)


#### START ###
def func():
    N = int(input())
    word = input().strip().split()

    # get bit array of size N
    nums = list(map(lambda s: int(s[2:], base=16), word))
    x = 0
    for num in nums:
        x = (x << 16) + num
    x >>= (-N) % 16

    if x.bit_count() == N:
        print("0")
        return

    right, tmp = [], x
    for i in range(N):
        if (tmp | x).bit_count() == N:
            right.append(i)
            break
        tmp >>= 1

    left, tmp = [], x
    MASK = 2 ** N - 1
    for i in range(N):
        if (tmp | x).bit_count() == N:
            left.append(i)
            break
        tmp = (tmp << 1) & MASK

    if right:
        bias = right[0]
        mask = (~x << bias) & x
        print("+{}\n{}".format(bias, bin(mask)[2:].rjust(N, '0')))
    if left:
        bias = left[0]
        mask = (~x >> bias) & x & ((1 << N - bias) - 1)
        out = "-{}\n{}".format(bias, bin(mask)[2:].rjust(N, '0'))
        print(out)
    if not left and not right:
        print("0")


func()
#### END ###
while True:
    try:
        func()
    except:
        break
