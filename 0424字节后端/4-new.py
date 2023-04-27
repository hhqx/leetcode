from collections import Counter, defaultdict
from math import comb, sqrt


def prime_factorization(n):
    """生成0-n内所有整数的质因数分解"""

    def get(x):
        d = Counter()
        for i in range(2, int(sqrt(x)) + 1):
            while x % i == 0:
                d[i] += 1
                x //= i
            if x < i:
                break
        if x != 1:
            d[x] += 1
        return list(d.items())

    factors = {1: []}
    for x in range(2, n + 1):
        r = get(x)
        factors[x] = r

    return factors


factors = prime_factorization(10 ** 4)
for i in range(1, 21):
    print(f"{i}: {factors[i]}")


def cal(n=200):
    show = defaultdict(list)
    d = Counter()
    factors = prime_factorization(n)
    for x in range(1, n + 1):

        if x == 1:
            factorsx = []
        else:
            factorsx = factors[x]
        odd_prime = []
        for prime, cnt in factorsx:
            if cnt % 2 == 1:
                odd_prime.append(prime)
        hid = tuple(odd_prime)
        d[hid] += 1

        show[hid].append(x)

    #
    ans = 0
    for hid in d:
        if d[hid] >= 3:
            ans += comb(d[hid], 3)

    return ans


def cal2(n=200):
    S = [i * i for i in range(1, n + 1)]
    vis = set()
    ans = 0
    for x in range(1, n + 1):
        if x in vis:
            continue

        cnt = 0
        for i, v in enumerate(S):
            if v * x > n:
                cnt = i
                break
            vis.add(v * x)

        if cnt >= 3:
            ans += comb(cnt, 3)
    return ans


def func(n=10**5):
    def count(n):
        S = set(i * i for i in range(n + 1))
        val = sum(
            1 for c in range(1, n + 1) for b in range(1, c) for a in range(1, b)
            if (a * b) in S and (b * c) in S and a * c in S
        )
        return val

    tar = 0
    # tar = count(n)
    tar = cal(n)
    # out = cal(n)
    out = cal2(n)
    print('n', n, 'tar', tar, 'out', out)


func()
