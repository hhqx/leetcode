import tqdm

def get_factors(n):
    factors = []
    N = int(n ** (0.5))
    for i in range(1, N):
        if n % i == 0:
            factors += [i, n // i]

    # print(factors)
    # print(len(factors))
    if n % N == 0:
        factors.append(N)
    return factors

def max_number_of_factors():
    """ 一百万以下因数最多: [720720, 240] """

    n = int(1e6)
    iters = range(1, n+1)
    # iters = [int(1e8)]
    # iters = [int(720720)]

    ans = []
    for i in tqdm.tqdm(iters):
        f = get_factors(i)
        ans.append([i, len(f)])

    print(max(ans, key=lambda x: x[1]))

max_number_of_factors()
