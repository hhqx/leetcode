from bisect import bisect_left

question_content = """
You are given a 2D array of axis-aligned rectangles. Each rectangle[i] = [xi1, 
yi1, xi2, yi2] denotes the iᵗʰ rectangle where (xi1, yi1) are the coordinates of 
the bottom-left corner, and (xi2, yi2) are the coordinates of the top-right 
corner. 

 Calculate the total area covered by all rectangles in the plane. Any area 
covered by two or more rectangles should only be counted once. 

 Return the total area. Since the answer may be too large, return it modulo 10⁹ 
+ 7. 

 
 Example 1: 
 
 
Input: rectangles = [[0,0,2,2],[1,0,2,3],[1,0,3,1]]
Output: 6
Explanation: A total area of 6 is covered by all three rectangles, as 
illustrated in the picture.
From (1,1) to (2,2), the green and red rectangles overlap.
From (1,0) to (2,3), all three rectangles overlap.
 

 Example 2: 

 
Input: rectangles = [[0,0,1000000000,1000000000]]
Output: 49
Explanation: The answer is 10¹⁸ modulo (10⁹ + 7), which is 49.
 

 
 Constraints: 

 
 1 <= rectangles.length <= 200 
 rectanges[i].length == 4 
 0 <= xi1, yi1, xi2, yi2 <= 10⁹ 
 

 Related Topics 线段树 数组 有序集合 扫描线 👍 174 👎 0

"""

from typing import *
from PythonLeetcodeRunner import *

# leetcode submit region begin(Prohibit modification and deletion)
class Segtree:
    def __init__(self):
        self.cover = 0
        self.length = 0
        self.max_length = 0


class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        hbound = set()
        for rect in rectangles:
            # 下边界
            hbound.add(rect[1])
            # 上边界
            hbound.add(rect[3])

        hbound = sorted(hbound)
        m = len(hbound)
        # 线段树有 m-1 个叶子节点，对应着 m-1 个会被完整覆盖的线段，需要开辟 ~4m 大小的空间
        tree = [Segtree() for _ in range(m * 4 + 1)]

        def init(idx: int, l: int, r: int) -> None:
            tree[idx].cover = tree[idx].length = 0
            if l == r:
                tree[idx].max_length = hbound[l] - hbound[l - 1]
            else:
                mid = (l + r) // 2
                init(idx * 2, l, mid)
                init(idx * 2 + 1, mid + 1, r)
                tree[idx].max_length = tree[idx * 2].max_length + tree[idx * 2 + 1].max_length

        def update(idx: int, l: int, r: int, ul: int, ur: int, diff: int) -> None:
            if l > ur or r < ul:
                return
            if ul <= l and r <= ur:
                tree[idx].cover += diff
                pushup(idx, l, r)
            else:
                mid = (l + r) // 2
                update(idx * 2, l, mid, ul, ur, diff)
                update(idx * 2 + 1, mid + 1, r, ul, ur, diff)
                pushup(idx, l, r)

        def pushup(idx: int, l: int, r: int) -> None:
            if tree[idx].cover > 0:
                tree[idx].length = tree[idx].max_length
            elif l == r:
                tree[idx].length = 0
            else:
                tree[idx].length = tree[idx * 2].length + tree[idx * 2 + 1].length

        init(1, 1, m - 1)

        sweep = list()
        for i, rect in enumerate(rectangles):
            # 左边界
            sweep.append((rect[0], i, 1))
            # 右边界
            sweep.append((rect[2], i, -1))
        sweep.sort()

        ans = i = 0
        while i < len(sweep):
            j = i
            while j + 1 < len(sweep) and sweep[i][0] == sweep[j + 1][0]:
                j += 1
            if j + 1 == len(sweep):
                break

            # 一次性地处理掉一批横坐标相同的左右边界
            for k in range(i, j + 1):
                _, idx, diff = sweep[k]
                # 使用二分查找得到完整覆盖的线段的编号范围
                left = bisect_left(hbound, rectangles[idx][1]) + 1
                right = bisect_left(hbound, rectangles[idx][3])
                update(1, 1, m - 1, left, right, diff)

            ans += tree[1].length * (sweep[j + 1][0] - sweep[j][0])
            i = j + 1

        return ans % (10 ** 9 + 7)


class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:

        ybound = []
        xbound = set()
        for i, (x1, y1, x2, y2) in enumerate(rectangles):
            ybound.append((y1, 1, i))
            ybound.append((y2, -1, i))
            xbound.add(x1)
            xbound.add(x2)
        ybound.sort()
        xbound = sorted(list(xbound))
        # rectangles.sort(key=lambda x: )

        # 维护切割线长度
        segLen = [xbound[i + 1] - xbound[i] for i in range(len(xbound) - 1)]
        line = [0] * (len(xbound) - 1)
        lineWidth = 0

        def add_line(x1, x2):
            nonlocal lineWidth
            id1, id2 = bisect_left(xbound, x1), bisect_left(xbound, x2)
            for i in range(id1, id2):
                if line[i] == 0:
                    lineWidth += segLen[i]
                line[i] += 1

        def remove_line(x1, x2):
            nonlocal lineWidth
            id1, id2 = bisect_left(xbound, x1), bisect_left(xbound, x2)
            for i in range(id1, id2):
                if line[i] == 1:
                    lineWidth -= segLen[i]
                line[i] -= 1

        # 沿着y轴从下往上动态扫描
        area = 0
        last_bound = ybound[0][0]
        for bound, flag, i in ybound:
            area += (bound - last_bound) * lineWidth
            area = area % (10 ** 9 + 7)
            last_bound = bound
            if flag == 1:
                add_line(rectangles[i][0], rectangles[i][2])
            else:
                remove_line(rectangles[i][0], rectangles[i][2])

        return area


class Solution:

    def rectangleArea(self, rectangles: List[List[int]]) -> int:

        ybound = []
        xbound = set()
        for i, (x1, y1, x2, y2) in enumerate(rectangles):
            ybound.append((y1, 1, i))
            ybound.append((y2, -1, i))
            xbound.add(x1)
            xbound.add(x2)
        ybound.sort()
        xbound = sorted(list(xbound))
        # rectangles.sort(key=lambda x: )

        # 维护切割线长度
        lineWidth = 0

        hbound = xbound
        m = len(hbound)
        # 线段树有 m-1 个叶子节点，对应着 m-1 个会被完整覆盖的线段，需要开辟 ~4m 大小的空间
        tree = [Segtree() for _ in range(m * 4 + 1)]

        def init(idx: int, l: int, r: int) -> None:
            tree[idx].cover = tree[idx].length = 0
            if l == r:
                tree[idx].max_length = hbound[l] - hbound[l - 1]
            else:
                mid = (l + r) // 2
                init(idx * 2, l, mid)
                init(idx * 2 + 1, mid + 1, r)
                tree[idx].max_length = tree[idx * 2].max_length + tree[idx * 2 + 1].max_length

        def update(idx: int, l: int, r: int, ul: int, ur: int, diff: int) -> None:
            if l > ur or r < ul:
                return
            if ul <= l and r <= ur:
                tree[idx].cover += diff
                pushup(idx, l, r)
            else:
                mid = (l + r) // 2
                update(idx * 2, l, mid, ul, ur, diff)
                update(idx * 2 + 1, mid + 1, r, ul, ur, diff)
                pushup(idx, l, r)

        def pushup(idx: int, l: int, r: int) -> None:
            if tree[idx].cover > 0:
                tree[idx].length = tree[idx].max_length
            elif l == r:
                tree[idx].length = 0
            else:
                tree[idx].length = tree[idx * 2].length + tree[idx * 2 + 1].length

        init(1, 1, m - 1)
        def add_line(x1, x2, diff=1):
            nonlocal lineWidth
            left, right = bisect_left(xbound, x1), bisect_left(xbound, x2)
            update(1, 1, m - 1, left+1, right, diff)  # 线段树id编号从1开始
            lineWidth = tree[1].length

        def remove_line(x1, x2, diff=-1):
            nonlocal lineWidth
            left, right = bisect_left(xbound, x1), bisect_left(xbound, x2)
            update(1, 1, m - 1, left+1, right, diff)  # 线段树id编号从1开始
            lineWidth = tree[1].length

        # 沿着y轴从下往上动态扫描
        area = 0
        last_bound = ybound[0][0]
        for bound, flag, i in ybound:
            area += (bound - last_bound) * lineWidth
            area = area % (10 ** 9 + 7)
            last_bound = bound
            if flag == 1:
                add_line(rectangles[i][0], rectangles[i][2])
            else:
                remove_line(rectangles[i][0], rectangles[i][2])

        return area

# leetcode submit region end(Prohibit modification and deletion)
 


if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
