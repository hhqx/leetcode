def count(arr):
    if not arr:
        ans = 0
    elif not arr[0]:
        ans = count(arr[1:]) + 1
    else:
        ans = count([arr[0] - 1] + arr[1:] + arr[0] * [arr[0] - 1]) + 1
    # print('arr', arr, 'ans', ans)
    return ans


for i in range(5):
    arr = [i]
    ret = count(arr)
    print('arr', arr)
    print('ret', ret)

count([1, 2])

edge = [[0, 1], [1, 2]]
g = [[] for _ in range(4)]
for u, v in edge:
    g[u].append(v)
    g[v].append(u)
g[0].append(-1)


def dfs(u, parent):
    for v in g[u]:
        if v == parent:
            continue
            dfs(v, u)

            if len(g[u]) == 1:
                print(f'{u} 是叶子')


dfs(0, -1)
