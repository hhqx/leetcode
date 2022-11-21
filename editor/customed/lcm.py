import math


def lcm(*args):
    """ 计算数组arr所有元素的最小公倍数 """
    arr = args
    gcd = arr[0]
    for a in arr[1:]:
        gcd = math.gcd(gcd, a)

    ans = 1
    for a in arr:
        ans *= a // gcd

    return ans


def lcm(*a):
    """
    function to calculate LCM。
    :param a:
    :return: LCM of array: a
    """
    _lcm = a[0]
    for i in range(1, len(a)):
        _lcm = _lcm * a[i] // math.gcd(_lcm, a[i])
    return _lcm


print(lcm(2, 6, 5))

