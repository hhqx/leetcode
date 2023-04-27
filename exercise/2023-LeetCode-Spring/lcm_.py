"""
Tarjan 算法离线求lcm, 利用并查集
link: https://segmentfault.com/a/1190000015145319
"""

# 定义节点类
class Node:
    def __init__(self, val):
        self.val = val
        self.children = []


# Tarjan 算法
def tarjan_lca(root, pairs):
    # 初始化并查集
    p = [i for i in range(n)]

    def find(x):
        if p[x] != x:
            p[x] = find(p[x])
        return p[x]

    def union(x, y):
        p[find(x)] = find(y)

    # 初始化答案字典和访问数组
    ans = {}
    vis = [False] * n

    # Tarjan 算法主体
    def dfs(u):
        vis[u] = True
        for v in tree[u].children:
            dfs(v)
            # union(u, v)
            union(v, u)
        for v in query[u]:
            if vis[v]:
                ans[(u, v)] = find(v)
                ans[(v, u)] = find(v)

    # 预处理查询对
    query = [[] for _ in range(n)]
    for u, v in pairs:
        query[u].append(v)
        query[v].append(u)

    # 运行 Tarjan 算法
    dfs(root)
    return ans


# 示例树结构
n = 7
tree = [Node(i) for i in range(n)]
tree[0].children = [1, 2]
tree[1].children = [3, 4]
tree[2].children = [5, 6]
#    0
#   1 2
# 3 4 5 6

# 示例查询对
pairs = [(3, 4), (5, 6), (1, 5)]

# 运行算法并打印结果
ans = tarjan_lca(0, pairs)
for pair in pairs:
    print(f'LCA of {pair}: {ans[pair]}')
