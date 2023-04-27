

def get_prime(x):
    flag = [True] * (x+1)
    for i in range(2, x+1):
        if flag[i] is False:
            return
