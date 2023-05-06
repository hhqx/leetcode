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
    if x.bit_count() == N: return "0"

    MASK = 2 ** N - 1
    def right_shift(x, delta):
        if delta >= 0:
            return x >> delta
        else:
            return (x << -delta) & MASK

    result = [None, None]
    for idx, dir in enumerate([1, -1]):
        tmp = x
        for i in range(N):
            if (tmp | x).bit_count() == N:
                result[idx] = i * dir
                break
            tmp = right_shift(tmp, dir)

    if all([not row for row in result]): return "0"
    ans = []
    for bias in result:
        if bias is None:
            continue
        mask = right_shift(~x, -bias) & x & ((1 << N + bias) - 1)
        ans += ["{:+d}\n{}".format(bias, bin(mask)[2:].rjust(N, '0'))]

    return ans if ans else "0"

def main():
    ret = func()
    print("\n".join(ret))


main()
#### END ###
while True:
    try:
        main()
    except:
        break
