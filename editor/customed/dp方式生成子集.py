# arr = [1, 2, 2, 4]
arr = [1, 3, 5, 6]


def get_subset(arr):
    n = len(arr)
    ret = []
    dp = [[] for _ in range(n + 1)]
    dp[0] = [[]]

    for i in range(len(arr)):
        num = arr[i]

        dmax = min(i + 1, n)
        # for d in range(1, n+1):
        for d in range(dmax + 1 - 1, 1 - 1, -1):
            # dp[d] = dp[d-1] + [num]

            dp[d].extend(item + [num] for item in dp[d - 1])

        # ret.extend(dp)

    print(dp)
    return sum(dp, [])


def get_subset(arr, delta=2):
    n = len(arr)
    ret = []
    dp = [[] for _ in range(n + 1)]

    for i in range(len(arr)):
        num = arr[i]

        dmax = min(i + 1, n)
        # for d in range(1, n+1):
        for d in range(dmax + 1 - 1, 2 - 1, -1):
            for item in dp[d - 1]:
                if not len(item):
                    if num + 1 >= delta:
                        dp[d].append(item + [num])
                else:
                    if num - delta >= item[-1]:
                        dp[d].append(item + [num])

        dp[1].append([num])


def get_subset(arr, delta=2):
    n = len(arr)
    ret = []
    dp = [[] for _ in range(n + 1)]

    for i in range(len(arr)):
        num = arr[i]

        dmax = min(i + 1, n)
        # for d in range(1, n+1):
        for d in range(dmax + 1 - 1, 2 - 1, -1):
            for item in dp[d - 1]:
                if not len(item):
                    if num + 1 >= delta:
                        dp[d].append(item + [num])
                else:
                    if num - delta >= item[-1]:
                        dp[d].append(item + [num])

        dp[1].append([num])

    print(dp)
    print(sum(len(row) for row in dp))
    return dp


def get_subset(arr, delta=2):
    n = len(arr)
    ret = []
    # dp = [[] for _ in range(n + 1)]
    dp = [dict() for _ in range(n + 1)]
    dp[0][-float('inf')] = 1

    for i in range(len(arr)):
        num = arr[i]

        dmax = min(i + 1, n)
        # for d in range(1, n+1):
        for d in range(dmax + 1 - 1, 1 - 1, -1):
            for x in dp[d - 1]:
                if num - x >= delta:
                    dp[d][num] = dp[d - 1][x] + dp[d].get(num, 0)

        # dp[1] = dp

    print(dp)
    print(sum(sum(row.values()) for row in dp[1:]))
    # print(sum(dp[]))
    return dp


subset = get_subset(arr)
print(subset)



