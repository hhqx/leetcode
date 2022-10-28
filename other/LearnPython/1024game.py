import itertools

NUMS = [30, 1024, 3, 2, 2, 2, 25, 24]
OP = ['*', '|', '//', '|', ]


def permute(arr, k):
    """ dfs枚举数组arr中选取k个全排的所有情况 """
    arr.sort()

    path = []
    result = []
    isUsed = [False] * len(arr)

    def dfs(i):
        if len(path) == k:
            result.append(tuple(path[:]))

        for j in range(i, len(arr)):
            if isUsed[j]:
                continue
            if j > i and arr[j] == arr[j - 1]:
                continue
            path.append(arr[j])
            isUsed[j] = True
            dfs(j + 1)
            isUsed[j] = False
            path.pop()

    dfs(0)
    return result


def main():
    # NUMS.sort()
    # OP.sort()

    nums = permute(NUMS, k=4)
    ops = permute(OP, k=3)

    print(f'{len(set(ops))}种运算符组合: {ops}')
    print(f'{len(set(nums))}种操作数符组合: {nums}')

    ret = []
    for num, op in itertools.product(nums, ops):
        ans = num[0]
        for ni, opi in zip(num[1:], op):
            ans = eval(f'ans {opi} {ni}')

        # print(ans)
        if ans == 1024:
            ret.append((num, op))

    print(f'枚举了{len(nums) + len(ops)}个方案, 找到{len(ret)}个结果为1024的')
    for i, (num, op) in enumerate(ret):
        print(f'方案{i + 1}', num, op)


if __name__ == '__main__':
    main()

"""
程序输出示例:
    3种运算符组合: [('*', '//', '|'), ('*', '|', '|'), ('//', '|', '|')]
    30种操作数符组合: [(2, 2, 2, 3), ..., (24, 25, 30, 1024)]
    枚举了33个方案, 找到6个结果为1024的
    方案1 (2, 2, 24, 1024) ('*', '//', '|')
    方案2 (2, 2, 25, 1024) ('*', '//', '|')
    方案3 (2, 2, 30, 1024) ('*', '//', '|')
    方案4 (2, 3, 24, 1024) ('*', '//', '|')
    方案5 (2, 3, 25, 1024) ('*', '//', '|')
    方案6 (2, 3, 30, 1024) ('*', '//', '|')

"""
