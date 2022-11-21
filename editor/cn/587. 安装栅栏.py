question_content = """
在一个二维的花园中，有一些用 (x, y) 坐标表示的树。由于安装费用十分昂贵，你的任务是先用最短的绳子围起所有的树。只有当所有的树都被绳子包围时，花园才能围好
栅栏。你需要找到正好位于栅栏边界上的树的坐标。 

测试用例:[[1,2],[2,2],[4,2],[5,2],[6,2],[7,2]]
测试结果:[[6,2],[1,2],[7,2],[6,2],[5,2],[4,2],[2,2]]
期望结果:[[4,2],[6,2],[2,2],[5,2],[1,2],[7,2]]

测试用例:[[3,0],[4,0],[5,0],[6,1],[7,2],[7,3],[7,4],[6,5],[5,5],[4,5],[3,5],[2,5],[1,4],[1,3],[1,2],[2,1],[4,2],[0,3]]
测试结果:[[3,0],[5,0],[6,1],[7,2],[7,3],[7,4],[6,5],[5,5],[4,5],[3,5],[2,5],[1,4],[0,3],[1,2],[2,1]]
期望结果:[[4,5],[2,5],[6,1],[3,5],[2,1],[1,4],[1,2],[7,4],[7,3],[7,2],[3,0],[0,3],[5,0],[5,5],[4,0],[6,5]]

 
# 测试用例:[[1,2],[2,2],[4,2],[5,2],[6,2],[7,2]]
# 测试结果:[[2,2],[4,2],[5,2],[6,2],[7,2],[1,2],[2,2],[4,2],[5,2],[6,2]]
# 期望结果:[[4,2],[6,2],[2,2],[5,2],[1,2],[7,2]]

 示例 1: 

输入: [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
输出: [[1,1],[2,0],[4,2],[3,3],[2,4]]
解释:

 

 示例 2: 

输入: [[1,2],[2,2],[4,2]]
输出: [[1,2],[2,2],[4,2]]
解释:

即使树都在一条直线上，你也需要先用绳子包围它们。
 

 

 注意: 

 
 所有的树应当被围在一起。你不能剪断绳子来包围树或者把树分成一组以上。 
 输入的整数在 0 到 100 之间。 
 花园至少有一棵树。 
 所有树的坐标都是不同的。 
 输入的点没有顺序。输出顺序也没有要求。 
 

 Related Topics 几何 数组 数学 👍 210 👎 0

"""

from typing import *
from PythonLeetcodeRunner import *


# @lc code=start
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        """ Jarvis 算法 """

        def cross(p: List[int], q: List[int], r: List[int]) -> int:
            return (q[0] - p[0]) * (r[1] - q[1]) - (q[1] - p[1]) * (r[0] - q[0])

        n = len(trees)
        if n < 4:
            return trees

        leftMost = 0
        for i, tree in enumerate(trees):
            if tree[0] < trees[leftMost][0] or (tree[0] == trees[leftMost][0] and tree[1] < trees[leftMost][1]):
                leftMost = i

        ans = []
        vis = [False] * n
        p = leftMost
        while True:
            q = (p + 1) % n
            for r, tree in enumerate(trees):
                # // 如果 r 在 pq 的右侧，则 q = r
                # 此处可以优化为, 若存在共线, 保存这些共线的点
                if cross(trees[p], trees[q], tree) < 0:
                    q = r
            # 是否存在点 i, 使得 p q i 在同一条直线上
            for i, b in enumerate(vis):
                if not b and i != p and i != q and cross(trees[p], trees[q], trees[i]) == 0:
                    ans.append(trees[i])
                    vis[i] = True

            # p作为本次迭代的向量起始点, q表示当前最靠外侧的点, 若有多个q点共线, 选取扫描到的第一个,
            # 最坏情况下在多个可能的q中, 每次都只扫描到线段上的第一个, 每次只前进一步,
            # 最好情况时刚好扫到最后一个, 一下把共线的点全部扫描完毕
            if not vis[q]:  # 如果有多个q共线, 刚好扫到最后一个时, q不用重走i点, 其余情况下q会重走i点, 故需要加上if判断
                ans.append(trees[q])
                vis[q] = True
            # else:
            #     print(q)
            p = q
            if p == leftMost:
                break
        return ans

    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        """ Jarvis 算法, 官解实现 + 小小优化, 2n*n -> n*n """

        def cross(p: List[int], q: List[int], r: List[int]) -> int:
            return (q[0] - p[0]) * (r[1] - q[1]) - (q[1] - p[1]) * (r[0] - q[0])

        n = len(trees)
        if n < 4:
            return trees

        leftMost = 0
        for i, tree in enumerate(trees):
            if tree[0] < trees[leftMost][0] or (tree[0] == trees[leftMost][0] and tree[1] < trees[leftMost][1]):
                leftMost = i

        ans = []
        vis = [False] * n
        p = leftMost
        while True:
            q = (p + 1) % n
            points_at_side = []
            for r, tree in enumerate(trees):
                # // 如果 r 在 pq 的右侧，则 q = r
                # 此处可以优化为, 若存在共线, 保存这些共线的点
                val = cross(trees[p], trees[q], tree)
                if val < 0:
                    points_at_side = [r]
                    q = r
                elif val == 0:
                    points_at_side.append(r)
                    # 保留距离p距离最大的点
                    q = max(q, r, key=lambda x: abs(trees[x][0] - trees[p][0]) + abs(trees[x][1] - trees[p][1]))
            # 是否存在点 i, 使得 p q i 在同一条直线上
            # for i, b in enumerate(vis):
            #     if not b and i != p and i != q and cross(trees[p], trees[q], trees[i]) == 0:
            #         ans.append(trees[i])
            #         vis[i] = True

            for i in points_at_side:
                if vis[i]:
                    continue
                ans.append(trees[i])
                vis[i] = True

            # p作为本次迭代的向量起始点, q表示当前最靠外侧的点, 若有多个q点共线, 选取扫描到的第一个,
            # 最坏情况下在多个可能的q中, 每次都只扫描到线段上的第一个, 每次只前进一步,
            # 最好情况时刚好扫到最后一个, 一下把共线的点全部扫描完毕
            # if not vis[q]:  # 如果有多个q共线, 刚好扫到最后一个时, q不用重走i点, 其余情况下q会重走i点, 故需要加上if判断
            #     ans.append(trees[q])
            #     vis[q] = True
            # else:
            #     print(q)
            p = q
            if p == leftMost:
                break
        return ans


class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        """ Graham 算法 """

        def cross(p: List[int], q: List[int], r: List[int]) -> int:
            return (q[0] - p[0]) * (r[1] - q[1]) - (q[1] - p[1]) * (r[0] - q[0])

        def distance(p: List[int], q: List[int]) -> int:
            return (p[0] - q[0]) * (p[0] - q[0]) + (p[1] - q[1]) * (p[1] - q[1])

        n = len(trees)
        if n < 4:
            return trees

        # 找到 y 最小的点 bottom
        bottom = 0
        for i, tree in enumerate(trees):
            if tree[1] < trees[bottom][1] or (tree[1] == trees[bottom][1] and tree[0] < trees[bottom][0]):
                bottom = i
        trees[bottom], trees[0] = trees[0], trees[bottom]

        # 以 bottom 原点，按照极坐标的角度大小进行排序, 角度一样则按幅值大小排序
        def cmp(a: List[int], b: List[int]) -> int:
            diff = - cross(trees[0], a, b)
            return diff if diff else (distance(trees[0], a) - distance(trees[0], b))

        trees[1:] = sorted(trees[1:], key=cmp_to_key(cmp))

        # 对于凸包最后且在同一条直线的元素按照距离从大到小进行排序, 交换 [l, n-1] 之间与[n-1, 0]共线的点
        # 目的是为了先扫描距离原点远的点, 在从原点出发时需要先扫描离原点近的点, 返回原点时则需要先扫描远的点
        # 本题的返回结果要求如果凸包边上有多点共线, 需要全部返回, 不能遗漏
        r = n - 1
        while r >= 0 and cross(trees[0], trees[n - 1], trees[r]) == 0:
            r -= 1
        l, h = r + 1, n - 1
        while l < h:
            trees[l], trees[h] = trees[h], trees[l]
            l += 1
            h -= 1

        # for debug, plot the coords
        # plot_text(trees, sz=5)

        stack = [0, 1]
        for i in range(2, n):

            # 如果当前元素与栈顶的两个元素构成的向量顺时针旋转，则弹出栈顶元素
            val = cross(trees[stack[-2]], trees[stack[-1]], trees[i])
            while len(stack) > 1 and val < 0:
                stack.pop()
                val = cross(trees[stack[-2]], trees[stack[-1]], trees[i])
            stack.append(i)

        ans = [trees[i] for i in stack]

        # for debug, plot the coords
        # plot_text(ans, sz=5)
        return ans

    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        def cross(p: List[int], q: List[int], r: List[int]) -> int:
            return (q[0] - p[0]) * (r[1] - q[1]) - (q[1] - p[1]) * (r[0] - q[0])

        def distance(p: List[int], q: List[int]) -> int:
            return (p[0] - q[0]) * (p[0] - q[0]) + (p[1] - q[1]) * (p[1] - q[1])

        n = len(trees)
        if n < 4:
            return trees

        # 找到 y 最小的点 bottom
        bottom = 0
        for i, tree in enumerate(trees):
            if tree[1] < trees[bottom][1] or -(tree[1] == trees[bottom][1] and tree[0] < trees[bottom][0]):
                bottom = i
        trees[bottom], trees[0] = trees[0], trees[bottom]

        # 以 bottom 原点，按照极坐标的角度大小进行排序, 角度相同的话先处理幅值大的点,
        # 这种方式可以顺利处理结束时多点共线的情况, 但需要对原点起始的共线情况进行处理
        def cmp(a: List[int], b: List[int]) -> int:
            diff = - cross(trees[0], a, b)
            return diff if diff else -(distance(trees[0], a) - distance(trees[0], b))

        trees[1:] = sorted(trees[1:], key=cmp_to_key(cmp))

        # for debug, plot the coords
        # plot_text(trees, sz=5)

        ans = []
        stack = [0, 1]
        for i in range(2, n):
            val = cross(trees[stack[-2]], trees[stack[-1]], trees[i])
            # 如果当前点和第一个线段共线, 直接添加改点, 不入栈
            if val == 0 and stack[-2] == 0:
                ans.append(trees[i])
                continue

            # 如果当前元素与栈顶的两个元素构成的向量顺时针旋转，则弹出栈顶元素
            while len(stack) > 1 and val < 0:
                stack.pop()
                val = cross(trees[stack[-2]], trees[stack[-1]], trees[i])
            stack.append(i)

        ans.extend([trees[i] for i in stack])

        # for debug, plot the coords
        # plot_text(ans, sz=5)
        return ans


class Solution:
    """ Andrew 算法 """

    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        def cross(p: List[int], q: List[int], r: List[int]) -> int:
            return (q[0] - p[0]) * (r[1] - q[1]) - (q[1] - p[1]) * (r[0] - q[0])

        n = len(trees)
        if n < 4:
            return trees

        # 按照 x 从小到大排序，如果 x 相同，则按照 y 从小到大排序
        trees.sort()

        hull = [0]  # hull[0] 需要入栈两次，不标记
        used = [False] * n
        # 求凸包的下半部分
        for i in range(1, n):
            while len(hull) > 1 and cross(trees[hull[-2]], trees[hull[-1]], trees[i]) < 0:
                used[hull.pop()] = False
            used[i] = True
            hull.append(i)
        # 求凸包的上半部分
        m = len(hull)
        for i in range(n - 2, -1, -1):
            if not used[i]:
                while len(hull) > m and cross(trees[hull[-2]], trees[hull[-1]], trees[i]) < 0:
                    used[hull.pop()] = False
                used[i] = True
                hull.append(i)
        # hull[0] 同时参与凸包的上半部分检测，因此需去掉重复的 hull[0]
        hull.pop()

        return [trees[i] for i in hull]


from cmath import phase, pi


def phase_by_ori(o: complex, q: complex, p: complex):
    return (phase(p - q) - phase(q - o) + pi) % (2 * pi) - pi


def AndrewHull(hull, r):
    hull.append(r)
    while len(hull) >= 3 and phase_by_ori(*hull[-3:]) < 0:
        hull.pop(-2)
    return hull


class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        trees = [complex(*t) for t in sorted(trees)]
        return [[int(t.real), int(t.imag)] for t in
                set(reduce(AndrewHull, trees, []) + reduce(AndrewHull, reversed(trees), []))]


from cmath import phase, pi


def phase_by_ori(o: complex, q: complex, p: complex):
    return (phase(p - q) - phase(q - o) + pi) % (2 * pi) - pi


def AndrewHull(hull, r):
    hull.append(r)
    while len(hull) >= 3 and phase_by_ori(*hull[-3:]) < 0:
        hull.pop(-2)
    return hull


class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        trees = [complex(*t) for t in sorted(trees)]

        # reduce(func, arr, a0), 和accumulate类似, 不同之处在于reduce返回的只是accumulate的最后一个结果
        ans = reduce(AndrewHull, trees, [])
        ans += reduce(AndrewHull, reversed(trees), [])

        return [[int(t.real), int(t.imag)] for t in set(ans)]


# leetcode submit region end(Prohibit modification and deletion)
# @lc code=end

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
