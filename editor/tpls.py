# 字典树
from collections import defaultdict
class Trie:
    def __init__(self):
        self.children = defaultdict(Trie)
        self.word = ""

    def insert(self, word):
        cur = self
        for c in word:
            cur = cur.children[c]
        cur.word = word


# 最右边位置零: x&(x-1)
# 取最右边bit1: x&(-x)
# 树状数组
def low_bit(x):
    return x & (-x)


class BitTree:
    def __init__(self, M, N):
        self.sz = N - M + 1
        self.M = M
        self.N = N
        self.arr = [0] * (self.sz + 1)

    def add(self, x, val):
        idx = x - self.M + 1
        while idx < self.sz:
            self.arr[idx] += val
            idx += low_bit(idx)

    def query(self, x):
        idx = x - self.M + 1
        ans = 0
        while idx > 0:
            ans += self.arr[idx]
            idx -= low_bit(idx)
        return ans

    def update(self, x, val):
        prev_val = self.query(x) - self.query(x - 1)
        delta = val - prev_val
        self.add(x, delta)


# 并查集
class UnionSet:
    def __init__(self, M):
        self.parent = {}
        self.cnt = 0
        for i in range(M):
            self.parent[i] = i
            self.cnt += 1

    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
            x = self.parent[x]
        return self.parent[x]

    def union(self, p, q):
        x, y = self.find(p), self.find(q)
        if x != y:
            self.parent[x] = y
            self.cnt -= 1


# 扩展转相除法
def gcd(a, b):
    if b == 0:
        return 1, 0, a
    x, y, g = gcd(b, a % b)
    x, y = y, x - a // b * y
    return x, y, g

# 前缀和哈希
# 字符串哈希
def hash(s, n):
    P = 131313
    MOD = int(2**64)
    h = [0] * (n + 1)
    p = [1] * (n + 1)
    for i in range(len(s)):
        h[i + 1] = (h[i] * P + ord(s[i])) % MOD
        p[i + 1] = (p[i] * P) % MOD

# 最小表示法(跳过)

# 二分法函数
# def bisect_left(arr, x, key=lambda x: x):
#     left, right = 0, len(arr)
#     while left < right:
#         mid = left + right >> 1
#         if

# 单调栈枚举最值区间

# 区间极值(队列, 堆, 分块, 线段树)

# 二分图, 最短路, 树形dp
