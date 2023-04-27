question_content = """
4. 传送卷轴
通过的用户数102
尝试过的用户数133
用户总通过次数102
用户总提交次数197
题目难度Hard
随着不断的深入，小扣来到了守护者之森寻找的魔法水晶。首先，他必须先通过守护者的考验。

考验的区域是一个正方形的迷宫，maze[i][j] 表示在迷宫 i 行 j 列的地形：

若为 . ，表示可以到达的空地；
若为 # ，表示不可到达的墙壁；
若为 S ，表示小扣的初始位置；
若为 T ，表示魔法水晶的位置。
小扣每次可以向 上、下、左、右 相邻的位置移动一格。而守护者拥有一份「传送魔法卷轴」，使用规则如下：

魔法需要在小扣位于 空地 时才能释放，发动后卷轴消失；；
发动后，小扣会被传送到水平或者竖直的镜像位置，且目标位置不得为墙壁(如下图所示)；
image.png
在使用卷轴后，小扣将被「附加负面效果」，因此小扣需要尽可能缩短传送后到达魔法水晶的距离。而守护者的目标是阻止小扣到达魔法水晶的位置；如果无法阻止，则尽可能 增加 小扣传送后到达魔法水晶的距离。
假设小扣和守护者都按最优策略行事，返回小扣需要在 「附加负面效果」的情况下 最少 移动多少次才能到达魔法水晶。如果无法到达，返回 -1。

注意：

守护者可以不使用卷轴；
传送后的镜像位置可能与原位置相同。
示例 1：

输入：
["..#...#..","##.....S.","#..#....#","....#.#.#","....#..#.",".##......","........#","#..#T..#.",".....#..#"]
输出：
8

输入：maze = [".....","##S..","...#.","T.#..","###.."]

输出：7

解释：如下图所示：
守护者释放魔法的两个最佳的位置为 [2,0] 或 [3,1]：
若小扣经过 [2,0]，守护者在该位置释放魔法，
小扣被传送至 [2,4] 处且加上负面效果，此时小扣还需要移动 7 次才能到达魔法水晶；
若小扣经过 [3,1]，守护者在该位置释放魔法，
小扣被传送至 [3,3] 处且加上负面效果，此时小扣还需要移动 9 次才能到达魔法水晶；
因此小扣负面效果下最少需要移动 7 次才能到达魔法水晶。
image.png

示例 2：

输入：maze = [".#..","..##",".#S.",".#.T"]

输出：-1

解释：如下图所示。
若小扣向下移动至 [3,2]，守护者使其传送至 [0,2]，小扣将无法到达魔法水晶；
若小扣向右移动至 [2,3]，守护者使其传送至 [2,0]，小扣将无法到达魔法水晶；
image.png

示例 3：

输入：maze = ["S###.","..###","#..##","##..#","###.T"]

输出：5

解释：如下图所示：
守护者需要小扣在空地才能释放，因此初始无法将其从 [0,0] 传送至 [0,4];
当小扣移动至 [2,1] 时，释放卷轴将其传送至水平方向的镜像位置 [2,1]（为原位置）
而后小扣需要移动 5 次到达魔法水晶
image.png

提示：

4 <= maze.length == maze[i].length <= 200
maze[i][j] 仅包含 "."、"#"、"S"、"T"

link：https://leetcode.cn/contest/season/2023-spring/problems/rdmXM7/
"""

from typing import *
from PythonLeetcodeRunner import *


# @lc code=start
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def challengeOfTheKeeper(self, maze: List[str]) -> int:
        """ 博弈目标是从起点到终点的总路径长度 """
        m, n = len(maze), len(maze[0])
        des, start = None, None
        for i in range(m):
            for j in range(n):
                if maze[i][j] == 'T':
                    des = (i, j)
                elif maze[i][j] == 'S':
                    start = (i, j)
        assert des is not None or start is None, ""

        # 传送后的到终点的最短距离, bfs
        mdis = [[inf] * n for _ in range(m)]
        q = deque([des])
        vis = {des}
        step = 0
        while q:
            for _ in range(len(q)):
                x, y = q.popleft()
                mdis[x][y] = step

                for i, j in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1),):
                    if i >= m or i < 0 or j >= n or j < 0:
                        continue
                    if (i, j) in vis or maze[i][j] == '#':
                        continue
                    vis.add((i, j))
                    q.append((i, j))
            step += 1
        # mmdis是传送后各点到终点的距离
        mmdis = [row.copy() for row in mdis]
        for i in range(m):
            for j in range(n):
                if maze[i][j] == 'S':
                    continue
                if maze[m - 1 - i][j] not in 'T#':
                    mmdis[i][j] = max(mmdis[i][j], mdis[m - 1 - i][j])
                if maze[i][n - 1 - j] not in 'T#':
                    mmdis[i][j] = max(mmdis[i][j], mdis[i][n - 1 - j])

        # print
        for row in maze:
            print(row)
        print('mdis:')
        for row in mdis:
            print(list(row))
        print('mmdis:')
        for row in mmdis:
            print(list(row))

        # 从起点开始用最短路径搜索, min( max(path[i][j])  for (i, j) in Si)
        i0, j0 = start
        h = [(mmdis[i0][j0], 0, i0, j0)]
        vis = {start}
        ans = inf
        while h:
            dis, step, x, y = heapq.heappop(h)

            for i, j in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1),):
                if i >= m or i < 0 or j >= n or j < 0:
                    continue
                if (i, j) in vis or maze[i][j] == '#':
                    continue
                vis.add((i, j))
                if (i, j) == des:
                    # return dis
                    ans = dis
                    h = []
                    break
                heapq.heappush(h, (max(mmdis[i][j] + step, dis), step + 1, i, j))

        return ans if ans != inf else -1

# %%
class Solution:
    cnt = 0
    def challengeOfTheKeeper(self, maze: List[str]) -> int:
        """ 博弈目标是使用卷轴后到终点的路径长度 """
        self.cnt += 1
        print('case cnt', self.cnt)
        m, n = len(maze), len(maze[0])
        des, start = None, None
        for i in range(m):
            for j in range(n):
                if maze[i][j] == 'T':
                    des = (i, j)
                elif maze[i][j] == 'S':
                    start = (i, j)
        assert des is not None or start is None, ""

        # 传送后的到终点的最短距离, bfs
        mdis = [[inf] * n for _ in range(m)]
        q = deque([des])
        vis = {des}
        step = 0
        while q:
            for _ in range(len(q)):
                x, y = q.popleft()
                mdis[x][y] = step

                for i, j in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1),):
                    if i >= m or i < 0 or j >= n or j < 0:
                        continue
                    if (i, j) in vis or maze[i][j] == '#':
                        continue
                    vis.add((i, j))
                    q.append((i, j))
            step += 1
        # mmdis是传送后各点到终点的距离
        mmdis = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if maze[i][j] == 'S':
                    continue
                if maze[m - 1 - i][j] not in 'T#':
                    mmdis[i][j] = max(mmdis[i][j], mdis[m - 1 - i][j])
                if maze[i][n - 1 - j] not in 'T#':
                    mmdis[i][j] = max(mmdis[i][j], mdis[i][n - 1 - j])

        #
        f = lambda x: f"\t{x}"
        # for row in maze:
        #     print(*list(map(f, row)))
        # print('mdis:')
        # for row in mdis:
        #     print(*list(map(f, row)))
        # print('mmdis:')
        # for row in mmdis:
        #     print(*list(map(f, row)))

        # 从起点开始用最短路径搜索, min( max(path[i][j])  for (i, j) in Si)
        i0, j0 = start
        h = [(mmdis[i0][j0], i0, j0)]
        vis = {start}
        ans = inf
        while h:
            dis, x, y = heapq.heappop(h)

            for i, j in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1),):
                if i >= m or i < 0 or j >= n or j < 0:
                    continue
                if (i, j) in vis or maze[i][j] == '#':
                    continue
                vis.add((i, j))
                if (i, j) == des:
                    ans = dis
                    h = []
                    break
                heapq.heappush(h, (max(mmdis[i][j], dis), i, j))

        return ans if ans != inf else -1


# leetcode submit region end(Prohibit modification and deletion)
# @lc code=end

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
