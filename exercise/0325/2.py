
"""


"""



"""


"""



















def maxVal(arr):
    """ 打家劫舍 """
    n = len(arr)
    if n <= 3:
        return max(arr)

    dp = [0] * n
    dp[0] = arr[0]
    dp[1] = max(arr[:2])
    dp[2] = max(arr[:3])
    for i in range(3, n):
        dp[i] = max([dp[i-3] + arr[i], dp[i-1], dp[i-2]])

    # print(dp)
    return dp[-1]


def maxVal1(arr):
    """ 打家劫舍 """
    n = len(arr)
    if n <= 3:
        return max(arr)

    dp = [[0] * 2 for _ in range(n)]
    dp[0][1] = arr[0]
    dp[1][1] = max(arr[:2])
    dp[1][0] = arr[0]

    dp[2][1] = max(arr[:3])
    dp[2][0] = max(dp[1][1], dp[1][0])
    for i in range(3, n):
        dp[i][0] = max([dp[i - 1][0], dp[i - 1][1], dp[i - 2][0], dp[i - 2][1]])
        dp[i][1] = dp[i - 3][1] + arr[i]

    # print(dp)
    return max([dp[-1][0], dp[-1][1]])


n = int(input())
arr = list(map(int, input().split(' ')))
ret = maxVal(arr)
print(ret)  # 14


