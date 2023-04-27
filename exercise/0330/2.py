








def func(edges, n):
    g = [[] for _ in range(n)]
    for u, v, w in edges:
        g[u - 1].append((v - 1, w))
        g[v - 1].append((u - 1, w))

    vis = set()
    ans = 0

    def dfs(u):
        nonlocal ans
        pass
        cnt = 0
        for v, w in g[u]:
            if v in vis:
                continue
            vis.add(v)
            r = dfs(v)
            cnt += w == 0
            if r == 0 and w == 0:
                ans += 1
        return cnt

    vis.add(0)
    dfs(0)
    return ans

    ans = 0
    vis.add(0)
    dfs(0)
    return ans


n = int(input())
edges = [list(map(int, input().split(' '))) for _ in range(n - 1)]
ret = func(edges, n)
print(ret)
