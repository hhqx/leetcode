


def main():

    a = input('a=')
    b = input('b=')
    a = int(a)
    b = int(b)
    result = a - b

    print('a - b = ', result)

main()

# 1 - 1/3 + 1/5

def cal_n(n=1):
    an = lambda n: (-1) ** (n - 1) / (2 * n - 1)
    for n in range(1, 6):
        print(f'n={n}, an={an(n)}')

    maxn = 1000*1000
    sum = 0
    for n in range(1, maxn+1):
        a = an(n)
        sum += a
        pi = sum * 4
        if n > maxn - 10:
            print(f'n={n}, an={an(n)}, sn={sum}, pi={pi}')

# cal_n()

