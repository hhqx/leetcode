question_content = """
5. 魔法棋盘
通过的用户数72
尝试过的用户数169
用户总通过次数76
用户总提交次数451
题目难度Hard
在大小为 n * m 的棋盘中，有两种不同的棋子：黑色，红色。当两颗颜色不同的棋子同时满足以下两种情况时，将会产生魔法共鸣：

两颗异色棋子在同一行或者同一列
两颗异色棋子之间恰好只有一颗棋子
由于棋盘上被施加了魔法禁制，棋盘上的部分格子变成问号。chessboard[i][j] 表示棋盘第 i 行 j 列的状态：

若为 . ，表示当前格子确定为空
若为 B ，表示当前格子确定为 黑棋
若为 R ，表示当前格子确定为 红棋
若为 ? ，表示当前格子待定
现在，探险家小扣的任务是确定所有问号位置的状态（留空/放黑棋/放红棋），使最终的棋盘上，任意两颗棋子间都 无法 产生共鸣。请返回可以满足上述条件的放置方案数量。

示例1：

输入：
2
1
["B","R"]

输出：1


输入：n = 3, m = 3, chessboard = ["..R","..B","?R?"]

输出：5

解释：给定的棋盘如图：
image.png
所有符合题意的最终局面如图：
image.png

示例2：

输入：n = 3, m = 3, chessboard = ["?R?","B?B","?R?"]

输出：105

提示：

n == chessboard.length
m == chessboard[i].length
1 <= n*m <= 30
chessboard 中仅包含 "."、"B"、"R"、"?"

test cases:


"""
test_cases = [
    [3, 3, [['.', '.', 'R'], ['.', '.', 'B'], ['?', 'R', '?']], 5],
    [3, 3, [['?', 'R', '?'], ['B', '?', 'B'], ['?', 'R', '?']], 105], [3, 2, [['?', 'B', '?'], ['.', '?', 'R']], 21],
    [2, 2, [['?', '?'], ['B', '?']], 27], [2, 3, [['?', 'R'], ['.', '.'], ['.', 'R']], 3],
    [2, 2, [['?', 'B'], ['?', '?']], 27], [3, 2, [['?', '?', '?'], ['?', '?', 'R']], 161],
    [3, 2, [['?', '?', '?'], ['?', 'R', '.']], 69], [2, 3, [['.', '?'], ['?', '?'], ['?', '.']], 81],
    [2, 2, [['?', '?'], ['.', '?']], 27], [1, 2, [['B'], ['R']], 1], [3, 1, [['?', '?', '?']], 23],
    [1, 3, [['?'], ['?'], ['?']], 23], [3, 2, [['?', '.', '.'], ['B', '.', '?']], 9], [1, 2, [['?'], ['B']], 3],
    [3, 2, [['?', '?', '?'], ['R', '?', 'R']], 69], [3, 3, [['?', '?', '?'], ['?', '.', '?'], ['?', 'B', '?']], 1137],
    [3, 1, [['.', 'R', 'R']], 1], [3, 2, [['?', 'B', '?'], ['R', '?', 'B']], 7],
    [3, 3, [['?', '?', '?'], ['?', '.', '?'], ['?', 'B', '?']], 1137],
    [2, 3, [['?', '?'], ['?', '?'], ['?', '?']], 529], [3, 1, [['?', '?', 'R']], 7],
    [3, 2, [['?', '?', '?'], ['.', '?', 'B']], 69], [3, 2, [['?', '?', '?'], ['?', '.', '?']], 207],
    [1, 2, [['?'], ['.']], 3], [2, 3, [['.', 'R'], ['B', 'R'], ['.', '?']], 2],
    [4, 2, [['?', 'B', '?', 'B'], ['R', '?', '.', '?']], 42], [2, 2, [['?', 'B'], ['?', 'R']], 9],
    [4, 4, [['?', '?', '?', '?'], ['?', '?', '?', '.'], ['?', '?', '?', '?'], ['?', '?', 'R', '?']], 322765],
    [2, 4, [['.', 'R'], ['B', 'R'], ['B', '.'], ['.', 'R']], 1], [1, 3, [['?'], ['?'], ['?']], 23],
    [4, 4, [['B', '?', '?', '?'], ['?', '?', '?', '?'], ['?', 'B', '?', '?'], ['?', '?', '?', '?']], 169529],
    [4, 4, ["????", "????", "????", "???R"], 657325],
]
# test_cases.append([4, 4, ["?"*4 for _ in range(4)], 5])
# test_cases.append([6, 6, ["?"*6 for _ in range(6)], 5])
for m, n, mat, out in test_cases[-3:]:
    s = f"输入:{n}\n{m}\n{mat}\n\n输出:{out}\n\n"
    # question_content += s

from typing import *
from PythonLeetcodeRunner import *

# @lc code=start
# leetcode submit region begin(Prohibit modification and deletion)

cases = []
cnt = 0


class Solution:
    def getSchemeCount(self, n: int, m: int, chessboard: List[str]) -> int:
        """ 暴力回溯, 复杂度过高 """
        global cnt, cases
        cnt += 1
        print('case cnt', cnt)

        m, n = n, m
        chessboard = [list(row) for row in chessboard]
        # 保存所有棋子位置
        rows = [[] for _ in range(m)]
        cols = [[] for _ in range(n)]
        row2idx = dict()
        col2idx = dict()
        for i in range(m):
            for j in range(n):
                if chessboard[i][j] != '.':
                    row2idx[(i, j)] = len(rows[i])
                    col2idx[(i, j)] = len(cols[j])
                    rows[i].append(j)
                    cols[j].append(i)

        def get_neighbor(i_, j_):
            """
            原本以为是只可以取"BR", 但是题目可以取'.'留空, 所以记录棋子的固定位置行不通.
            不过可以尝试用m+n个栈, 这样查找行列前三个元素时无需一直往前搜索.
            """
            i0, j0 = row2idx[(i_, j_)], col2idx[(i_, j_)],
            posi = [[i_, rows[i_][i]] for i in range(i0 - 2, i0 + 2 + 1) if 0 <= i < len(rows[i_])]
            posj = [[cols[j_][j], j_] for j in range(j0 - 2, j0 + 2 + 1) if 0 <= j < len(cols[j_])]

            neri = ["".join(chessboard[i][j] for i, j in posi[k:k + 3]) for k in range(len(posi) - 2)]
            nerj = ["".join(chessboard[i][j] for i, j in posj[k:k + 3]) for k in range(len(posj) - 2)]
            return neri, nerj

        def get_neighbor(i_, j_):
            out_i1, out_j1 = [], []
            for i in range(i_, -1, -1):
                if (c := chessboard[i][j_]) != '.':
                    out_i1.append(c)
                    if len(out_i1) >= 3:
                        break
            for j in range(j_, -1, -1):
                if (c := chessboard[i_][j]) != '.':
                    out_j1.append(c)
                    if len(out_j1) >= 3:
                        break

            neri = ["".join(out_i1[k:k + 3]) for k in range(len(out_i1) - 2)]
            nerj = ["".join(out_j1[k:k + 3]) for k in range(len(out_j1) - 2)]
            return neri, nerj

        def is_valid(pos):
            if any(s in {"RRB", "RBB", "BBR", "BRR"} for s in pos):
                return False
            return True

        # dfs
        def dfs(i, j):
            i, j = i + j // n, j % n
            choice = "BR."

            # if i == m - 1 or (j == n - 1 and n >= 3):
            #     if chessboard[i][j] != '?':
            #         choice = chessboard[i][j]
            #     pass
            # else:
            #     pass
            #     while i < m and chessboard[i][j] != '?':
            #         j += 1
            #         i, j = i + j // n, j % n

            if i >= m:
                # for row in chessboard:
                #     print(*row)
                # print('')
                return 1
            choice = "BR." if chessboard[i][j] == '?' else chessboard[i][j]

            # assert chessboard[i][j] == '?', ""
            chess = chessboard[i][j]

            r = 0
            for c in choice:
                chessboard[i][j] = c
                neri, nerj = get_neighbor(i, j)
                if is_valid(neri) and is_valid(nerj):
                    r += dfs(i, j + 1)
                chessboard[i][j] = chess

            return r

        ans = dfs(0, 0)
        cases.append([n, m, chessboard, ans])

        return ans


class Solution:
    def getSchemeCount(self, n: int, m: int, chessboard: List[str]) -> int:
        """ 暴力回溯, 复杂度过高 """
        global cnt, cases
        cnt += 1
        print('case cnt', cnt)

        m, n = n, m
        chessboard = [list(row) for row in chessboard]
        row = [[] for _ in range(m)]
        col = [[] for _ in range(n)]

        def is_valid(s):
            return s not in {"RRB", "RBB", "BBR", "BRR"}

        def get_hash(row, col):
            hashid = tuple(tuple(item[-min(len(item), 3):]) for item in row + col)
            return hashid

        # dfs
        @cache
        def dfs(i, j, hid):
            i, j = i + j // n, j % n
            if i >= m:
                # for row in chessboard:
                #     print(*row)
                # print('')
                return 1
            choice = "BR." if chessboard[i][j] == '?' else chessboard[i][j]

            # assert chessboard[i][j] == '?', ""
            chess = chessboard[i][j]

            r = 0
            for c in choice:
                chessboard[i][j] = c
                if c != '.':
                    row[i].append(c)
                    col[j].append(c)

                neri, nerj = "".join(row[i][-min(3, len(row[i])):]), "".join(col[j][-min(3, len(col[j])):])
                if is_valid(neri) and is_valid(nerj):
                    r += dfs(i, j + 1, get_hash(row, col))
                chessboard[i][j] = chess

                if c != '.':
                    row[i].pop()
                    col[j].pop()

            return r

        ans = dfs(0, 0, get_hash(row, col))
        cases.append([n, m, chessboard, ans])

        return ans


class Solution:
    def getSchemeCount(self, n: int, m: int, chessboard: List[str]) -> int:
        @cache
        def get_next(pre, a):
            if a == '.':
                return pre
            return pre[1] + a if pre[0] in ['.', a] else ''

        @cache
        def dfs(i, j, row, cols):
            if i == n:
                return 1
            ans = 0
            for a in ('.RB' if chessboard[i][j] == '?' else chessboard[i][j]):
                if (nrow := get_next(row, a)) and (ncol := get_next(cols[j], a)):
                    ni, nj, nrow = (i, j + 1, nrow) if j < m - 1 else (i + 1, 0, '..')
                    ans += dfs(ni, nj, nrow, cols[:j] + (ncol,) + cols[j + 1:])
            return ans

        return dfs(0, 0, '..', ('..',) * m)


TRANS = (
    # (当前序列末尾添加 B 之后的状态，当前序列末尾添加 R 之后的状态)
    (1, 2),  # 0: 空
    (3, 6),  # 1: 一个 B
    (5, 4),  # 2: 一个 R
    (3, -1),  # 3: 连续多个 B
    (-1, 4),  # 4: 连续多个 R
    (-1, 6),  # 5: BR 交替，且以 B 结尾
    (5, -1),  # 6: BR 交替，且以 R 结尾
)


class Solution1:
    def getSchemeCount(self, n: int, m: int, chessboard: List[str]) -> int:
        a = chessboard
        if n < m:  # 保证 n >= m
            a = [list(col) for col in zip(*a)]
            n, m = m, n

        def DFS(r: int, mask: int) -> int:
            if r == n:
                return 1

            # 写一个爆搜，生成出所有的合法状态
            @cache
            def dfs(c: int, row_mask: int, col_mask: int) -> int:
                if c == m:
                    return DFS(r + 1, col_mask)  # 枚举下一行

                def nxt(color: int) -> int:
                    rm = TRANS[row_mask][color]  # 新的 rowMask
                    if rm < 0: return 0  # 非法
                    c3 = c * 3
                    cm = TRANS[(col_mask >> c3) & 7][color]  # 新的 colMask 的第 c 列
                    if cm < 0: return 0  # 非法
                    cm = col_mask & ~(7 << c3) | (cm << c3)  # 修改 colMask 的第 c 列
                    return dfs(c + 1, rm, cm)

                b = a[r][c]
                if b == 'B':
                    return nxt(0)
                if b == 'R':
                    return nxt(1)
                if b == '.':
                    return dfs(c + 1, row_mask, col_mask)
                return dfs(c + 1, row_mask, col_mask) + nxt(0) + nxt(1)

            return dfs(0, 0, mask)

        return DFS(0, 0)


# leetcode submit region end(Prohibit modification and deletion)
# @lc code=end

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
