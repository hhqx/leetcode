question_content = """
输入：
num = 41,
plate = ["E...W..WW",".E...O...","...WO...W","..OWW.O..",".W.WO.W.E","O..O.W...",".OO...W..","..EW.WEE."]
输出：[[0,2],[0,3],[0,5],[0,6],[1,0],[1,8],[3,0],[3,8],[4,0],[6,0],[7,1],[7,4]]



输入：
num = 4, plate = ["..E.",".EOW","..W."]
输出：[[2,1]]


输入：
num = 5,
plate = [".....","..E..",".WO..","....."]
输出：[[0,1],[1,0],[2,4],[3,2]]


输入：
num = 3,
plate = [".....","....O","....O","....."]
输出：[]







"""

from typing import *
from PythonLeetcodeRunner import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def ballGame(self, num: int, plate: List[str]) -> List[List[int]]:
        dir_table = [[-1, 0], [0, 1], [1, 0], [0, -1], ]
        dir = 0

        def rotate_dir(i):
            i += 1
            if i == len(dir_table):
                i = 0
            return i

        def rotate_dir_reverse(i):
            i -= 1
            if i == -1:
                i = len(dir_table) - 1
            return i

        m, n = len(plate), len(plate[0])

        def dfs(i, j):
            nonlocal dir, step
            # print(i, j, plate[i][j])

            # if step == 0:
            #     pass
            if plate[i][j] == 'O':
                return True
            elif plate[i][j] == 'E':
                dir = rotate_dir(dir)
            elif plate[i][j] == 'W':
                dir = rotate_dir_reverse(dir)

            step += 1

            if step > num:
                return False

            # next step
            D = dir_table[dir]
            ii, jj = i + D[0], j + D[1]
            if ii >= m or ii < 0 or jj >= n or jj < 0:
                return False
            if dfs(ii, jj):
                return True

            return False

        # get all start points and directions
        point = []
        dir_start = []
        # left
        for i in range(m - 2):
            p = [i + 1, 0]
            point.append(p)
            dir_start.append(1)
        # right
        for i in range(m - 2):
            p = [i + 1, n - 1]
            point.append(p)
            dir_start.append(3)
        # up
        for i in range(n - 2):
            p = [0, i + 1]
            point.append(p)
            dir_start.append(2)
        # down
        for i in range(n - 2):
            p = [m-1, i + 1]
            point.append(p)
            dir_start.append(0)

        # play the game
        ans = []
        # point = [[2,1]]
        # dir_start = [0]

        # point = [[4,8]]
        # dir_start = [3]
        for d, (i, j) in zip(dir_start, point):
            # if [i,j] in [[4,8], [7,3], [7,2]]:
            #     import numpy as np
            #     mat = [[c for c in s] for s in plate]
            #     mat = np.array(mat)
            #     print('p')
            #     continue
            if plate[i][j] != '.':
                continue
            dir = d
            step = 0
            # print('Start .. ')
            status = dfs(i, j)
            if status:
                ans.append([i, j])
            # print(f'status:{status}')

        # ans.sort(key=lambda x: (x[0],x[1]))
        return ans




class Solution1:
    def ballGame(self, num: int, plate: List[str]) -> List[List[int]]:
        dir_table = [[-1, 0], [0, 1], [1, 0], [0, -1], ]
        dir = 0

        def rotate_dir(i):
            i += 1
            if i == len(dir_table):
                i = 0
            return i

        def rotate_dir_reverse(i):
            i -= 1
            if i == -1:
                i = len(dir_table) - 1
            return i

        m, n = len(plate), len(plate[0])

        def dfs(i, j):
            nonlocal dir, step
            # print(i, j, plate[i][j])

            if plate[i][j] == 'O':
                return True
            elif plate[i][j] == 'E':
                dir = rotate_dir(dir)
            elif plate[i][j] == 'W':
                dir = rotate_dir_reverse(dir)

            step += 1

            if step > num:
                return False

            # next step
            D = dir_table[dir]
            ii, jj = i + D[0], j + D[1]
            if ii >= m or ii < 0 or jj >= n or jj < 0:
                return False
            if dfs(ii, jj):
                return True

            return False

        # get all start points and directions
        point = []
        dir_start = []
        # left
        for i in range(m - 2):
            p = [i + 1, 0]
            point.append(p)
            dir_start.append(1)
        # right
        for i in range(m - 2):
            p = [i + 1, n - 1]
            point.append(p)
            dir_start.append(3)
        # up
        for i in range(n - 2):
            p = [0, i + 1]
            point.append(p)
            dir_start.append(2)
        # down
        for i in range(n - 2):
            p = [m-1, i + 1]
            point.append(p)
            dir_start.append(0)

        # play the game
        ans = []
        # point = [[2,1]]
        # dir_start = [0]
        for d, (i, j) in zip(dir_start, point):
            if plate[i][j] != 'O':
                continue
            dir = d
            step = 0
            # print('Start .. ')
            status = dfs(i, j)
            if status:
                ans.append([i, j])
            # print(f'status:{status}')

        return ans

# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
