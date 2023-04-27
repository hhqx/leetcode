def divmod_(a, b):
    """
    思路, 仿照十进制除法列竖式的思路, 对a,b的二进制表示列竖式然后依次相除
    时间复杂度: o(log(a)-log(b))
    """
    if a < b:
        return 0, a
    la, lb = a.bit_length(), b.bit_length()

    # d 是 a,b 的位长度差, 总共需要迭代 d+1 次
    div, d = 0, la - lb
    for i in range(d + 1):
        bi = b << (d - i)
        if a - bi >= 0:
            div += 1 << d - i
            a -= bi

    return div, a


def valid():
    import random
    random.seed(0)
    case_number = 100000
    for _ in range(case_number):
        a, b = random.randint(0, case_number), random.randint(1, case_number // 10)
        expect = divmod(a, b)
        output = divmod_(a, b)

        assert output == expect, f'Output not equal to Expect: a={a}, b={b}, expect={expect}, output={output}'
    else:
        print('All cases has accepted.')


valid()
assert 0, ""
