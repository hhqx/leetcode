import bisect

question_content = """


# 输入：
# [[0,0],[1,0],[2,0],
#  [0,2]
# ]
# 4
# 
# 输出：1
# 
# 输入：
# [[0,0],[1,0],[2,0],[3,0],[4,0]]
# 5

输出：2


"""

from typing import *
from PythonLeetcodeRunner import *


def add_cases():
    def add_pair(in_, out):
        global question_content
        s = "Input:\n"
        s += "\n".join(map(str, in_))
        s += f"\nOutput:\n{out}\n"
        question_content += s

    from random import randint, seed
    seed(0)
    for _ in range(5):
        n = 20
        MAXX = 10 ** 1

        points = [[randint(1, MAXX), randint(1, MAXX)] for _ in range(n)]
        m = randint(1, n + 1)
        add_pair((points, m), 0)

    return


add_cases()


def brute_force(points, m):
    # cnt = defaultdict(list)
    cnt = Counter()
    q = deque((0, i, p) for i, p in enumerate(points))
    vis = set((i, p[0], p[1]) for i, p in enumerate(points))
    ans = 0

    xmax = max(x for x, y in points)
    ymax = max(y for x, y in points)

    xmax, ymax = 1000, 1000
    while q:
        for _ in range(len(q)):
            dis, id, (x, y) = q.popleft()
            cnt[(x, y)] += 1
            if cnt[(x, y)] == m:
                return dis
            # ans = max(ans, dis)

            from itertools import product
            for dx, dy in product([-1, 0, 1], [-1, 0, 1]):
                i, j = x + dx, y + dy
                if (id, i, j) in vis:
                    continue
                if i < 0 or i > xmax or j < 0 or j > ymax:
                    continue
                vis.add((i, j))
                q.append((dis + 1, id, (i, j)))

    maxval = max(cnt.values())
    print('maxval', maxval)
    return 0


# @lc code=start
# leetcode submit region begin(Prohibit modification and deletion)
def fieldOfGreatestBlessing(forceField: List[List[int]]) -> int:
    """ 离散形式的二维差分数组 """
    diff = []
    xcoord, ycoord = set([-inf]), set([-inf])
    for x, y, side in forceField:
        x, y, side = 2 * x, 2 * y, 2 * side
        x1, x2, y1, y2 = x - side // 2, x + side // 2 + 1, y - side // 2, y + side // 2 + 1,
        tmp = [[x1, y1, 1], [x1, y2, -1], [x2, y1, -1], [x2, y2, 1], ]
        diff.extend(tmp)
        xcoord = xcoord.union([x1, x2])
        ycoord = ycoord.union([y1, y2])

    xcoord = list(sorted(xcoord))
    ycoord = list(sorted(ycoord))
    # print(xcoord, ycoord)

    # 给差分二维数组赋初始值
    ans = -inf
    d = defaultdict(int)
    for x, y, val in diff:
        d[(x, y)] += val

    # 对二维数组进行累加积分
    for i in range(1, len(xcoord)):
        for j in range(1, len(ycoord)):
            x1, x2, y1, y2 = xcoord[i - 1], xcoord[i], ycoord[j - 1], ycoord[j],
            d[(x2, y2)] += d[(x1, y2)] + d[(x2, y1)] - d[(x1, y1)]
            ans = max(ans, d[(x2, y2)])

    return ans


class Solution:
    def minDay(self, points, m):
        def bisect_left(arr, tar, key=lambda x: x):
            """ 二分法查找 """
            left, right = -1, len(arr)
            while right - left > 1:
                mid = (right + left) // 2
                if key(arr[mid]) < tar:
                    left = mid
                else:
                    right = mid
            return right

        def isValid(k):
            """ 判断长度为k时, 是否有一个点长了至少m种草 """
            rects = [[x, y, 2 * k] for x, y in points]
            cnt = fieldOfGreatestBlessing(rects)
            return cnt >= m

        # print(isValid(1))

        # 二分查找长度
        UPPER = 10 ** 9 + 1
        idx = bisect_left(range(1, UPPER), True, key=lambda x: isValid(x)) + 1

        ans = idx if idx < UPPER else 0

        return brute_force(points, m)
        return ans


# leetcode submit region end(Prohibit modification and deletion)
# @lc code=end

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()

