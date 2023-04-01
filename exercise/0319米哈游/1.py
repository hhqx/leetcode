"""
米小游拿到了一个无限长的字符串:1,2,3,4,5,6,7,8,9,10,11,12,13,14......
该字符串由数字字符和，以及组成，代表整个自然数集。每三个数由一个分号隔开，其它的数由逗号隔开
米小游想知道，该字符串的第1个字符到第r字符之间有多少个逗号和分号?

输入描述:
第一行输入一个正整数t，代表询问次数。接下来的t行，每行输入两个正整数l和r，代表一次询问。
1 <= t <= 10^4
1 <= l <= r <= 10^3

输出描述:
输出t行，每行输入两个整数，用空格隔开。分别代表','的数量和';'的数量

"""


# # 用python写算法题
#
# # 输入询问次数t
# t = int(input())
#
# # 创建一个空列表存储结果
# results = []
#
# # 循环t次
# for _ in range(t):
#     # 输入l和r
#     l, r = map(int, input().split())
#     # 初始化逗号和分号的数量为0
#     comma = 0
#     semicolon = 0
#     # 计算从第1个字符到第l-1个字符之间有多少个逗号和分号（因为索引从0开始）
#     for i in range(l-1):
#         # 如果是逗号，逗号数量加1
#         if i % 4 == 2:
#             comma += 1
#         # 如果是分号，分号数量加1
#         elif i % 4 == 3:
#             semicolon += 1
#     # 计算从第l个字符到第r个字符之间有多少个逗号和分号（包含两端）
#     for i in range(l-1, r):
#         # 如果是逗号，逗号数量加1
#         if i % 4 == 2:
#             comma += 1
#         # 如果是分号，分号数量加1
#         elif i % 4 == 3:
#             semicolon += 1
#     # 把当前询问的结果添加到列表中（用元组表示）
#     results.append((comma, semicolon))
#
# # 输出每次询问的结果（用空格隔开）
# for result in results:
#     print(result[0], result[1])


def get_queries(queries):
    def count_before_n(n):
        semicolon = n // 6
        comma = n // 2 - semicolon
        return comma, semicolon

    ans = []
    for l, r in queries:
        r1, r2 = count_before_n(r)
        l1, l2 = count_before_n(l)
        ans.append((r1 - l1, r2 - l2))

    return ans


# t = int(input())
# queries = []
# for _ in range(t):
#     row = list(map(int, input().split(' ')))
#     queries.append(row)
# ret = get_queries(queries)
# for comma, semicolon in queries:
#     print(comma, semicolon)

"""
[9*2, (100-10)*3, (1000-100)*4, ... ]
"""
cnt = [[10 - 1, 9 * 2]]
for N in range(2, 14 - 1):
    cnt.append([10 ** N - 1, (10 ** N - 10 ** (N - 1)) * (N + 1)])
print(cnt)


def count_separate(n):
    """ 计算长度为n自然数字符串有多少个分隔符 """
    separate = 0
    for i, (num_before, delta) in enumerate(cnt):
        if n > delta:
            n -= delta
            separate = num_before
        else:
            separate += n // (2 + i)
            break
    return separate


def get_queries(queries):
    def count_before_n(n):
        semicolon = count_separate(n) // 3
        comma = count_separate(n) - semicolon
        return comma, semicolon

    ans = []
    for l, r in queries:
        r1, r2 = count_before_n(r)
        l1, l2 = count_before_n(l)
        ans.append((r1 - l1, r2 - l2))

    return ans


# test function: count_separate()
test_str = ""
for i in range(1, 10 ** 3):
    test_str += str(i) + ','
    print(i, count_separate(len(test_str)), count_separate(len(test_str) - 1), count_separate(len(test_str) + 1))
