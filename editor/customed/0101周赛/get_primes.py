
def get(right=int(1e6)):
    primes = [2]
    for num in range(2, right + 1):
        tmp = num
        for i in primes:
            if tmp % i == 0:
                tmp //= i
                break
        else:
            primes.append(num)
    print(primes)
    return primes

# def get(right=int(1e5)):
#     primes = []
#     for num in range(2, right + 1):
#         tmp = num
#         for i in range(2, num):
#             if tmp % i == 0:
#                 tmp //= i
#                 break
#         else:
#             primes.append(num)
#     print(primes)
#     return primes

# primes = get(right=100)
primes = get()
