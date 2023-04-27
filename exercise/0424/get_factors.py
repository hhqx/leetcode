import math
from collections import Counter, defaultdict


def get_primes(n=100):
    """ 埃氏筛求[0,n]内所有数字的质因子, 时间复杂度: n*log(n) """
    primes = [[] for _ in range(n + 1)]
    for x in range(2, n + 1):
        if primes[x]:
            continue
        for j in range(x, n + 1, x):
            primes[j].append(x)
    return primes


def get_factors(n=100):
    """ 求[0,n]内所有元素的质因数分解, 时间复杂度: n*log(n) """
    primes = get_primes(n)
    factors = [dict() for _ in range(n + 1)]
    for x, prime in enumerate(primes):
        counter = factors[x]
        for factor in prime:
            cnt = 0
            while x and x % factor == 0:
                cnt += 1
                x //= factor
            counter[factor] = cnt
        # factors[x] = counter
    return factors


n = 10 ** 5
ret = get_factors(n)
# print(n, sum(sum(cnt.values()) for cnt in ret) / n)
print('{}以内的所有数平均有{}个质因子'.format(n, sum(sum(cnt.values()) for cnt in ret) / n))


# print(ret)


def t4():
    """ 给一个n, 求有多少对(a,b,c), 0<a<b<c<=n, 使得ab,bc,ac均为完全平方数, n最大为10**5 """

    def cal1(n=100):
        """
        有结论: "ab,bc,ac均为完全平方数" <=> "a,b,c 的奇数次质因子完全一致"

        证明:
            首先, 对于整数x, x为完全平方数的充要条件是x的质因子指数全为偶数, 也就是说 ab, bc, ac 的质因子指数全为偶数
            - 证明 "a,b,c 的奇数次质因子集合完全相等"  =>  "ab, bc, ac 的质因子指数全为偶数"
                考虑 a,b,c 的奇数次质因子集合分别Oa, Ob, Oc,
                如果存在某个因子x属于Oa但是不属于Ob, 即质因子x在a中的指数为奇数, x在b中的指数为偶数,
                则 x 在ab中的指数为奇数, => ab 不是完全平方数

            - 证明 "ab, bc, ac 的质因子指数全为偶数"  =>  "a,b,c 的奇数次质因子集合完全相等"
                1. 假设 xi 在 a的指数为奇数, 则 xi 在b的指数为奇数(因为在ab中的指数为偶数), xi在c中的指数为奇数
                2. 假设 xi 在 a的指数为偶数,  则 xi 在b的指数为偶数(因为在ab中的指数为偶数), xi在c中的指数为偶数
            也就是说xi在a,b,c中的指数必然是同奇或同偶的, 因此, a,b,c的质因子集合应完全相等

        算法思路:
            枚举所有的数奇数次指数的质因子集合, 用组合数计算.
        """
        factors = get_factors(n)
        d = Counter()
        for x, counter in enumerate(factors):
            if not x:
                continue
            odd_cnt_factor = tuple(factor for factor, cnt in counter.items() if cnt % 2 == 1)
            d[odd_cnt_factor] += 1

        # 对于拥有奇数指数质因子的数构成的集合, 任选三个数构成(a,b,c)均可满足题意
        ans = sum(math.comb(v, 3) for v in d.values() if v >= 3)
        return ans

    def cal2(n=100):
        """
        线性筛选法: 时间复杂度o(n), 空间复杂度o(n).
                                --- from ky
        1 4 9 16（k=1）
        2 8 18 32（k=2）
        3 12 27  48（k=3）

        4 16, 36, 64 (k=4), 和k=1重复, 被包含在k=1的序列中
        5, 20, 45, ... (k=5)
        6, 24, 54, ... (k=6)
        ...
        6, 24, 54, ... (k=8), 和k=2序列重复, 被包含在k=2的序列中
        ...
        12, 48, 108,... (k=12), 和k=3序列重复, 被包含在k=3的序列中
        实际上会重复的k一定会整个都重复, 若k'和k重复, 则必然有 k'=k * a^2, 也就是说, k'为k乘一个完全平方数(也就是说k和k'的奇数次质因子元素相同)
        这样操作下来, 整个的时间复杂度是o(n), 空间复杂度也是o(n)
        """
        S = [i * i for i in range(1, n + 1)]
        vis = set()
        ans = 0
        for k in range(1, n + 1):
            if k in vis:
                # 如果k已经使用过了, 则说明kS这个序列是重复的
                continue
            cnt = 0
            for x in S:
                if x * k > n:
                    break
                vis.add(x * k)
                cnt += 1
            ans += math.comb(cnt, 3) if cnt >= 3 else 0

        return ans

    for n in (20, 10 ** 5):
        out1 = cal1(n)
        out2 = cal2(n)
        print("n={}, out1={}, out2={}.".format(n, out1, out2))


t4()
