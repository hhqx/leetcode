question_content = """
Given an m x n board of characters and a list of strings words, return all 
words on the board. 

 Each word must be constructed from letters of sequentially adjacent cells, 
where adjacent cells are horizontally or vertically neighboring. The same letter 
cell may not be used more than once in a word. 

 
 Example 1: 
测试用例:[["a","a"]]
    ["aaa"]
测试结果:["aaa"]
期望结果:[]

测试用例:[["a"]]
        ["a"]
测试结果:[]
期望结果:["a"]

 
Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f",
"l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
 

 Example 2: 
 
 
Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []
 

 
 Constraints: 

 
 m == board.length 
 n == board[i].length 
 1 <= m, n <= 12 
 board[i][j] is a lowercase English letter. 
 1 <= words.length <= 3 * 10⁴ 
 1 <= words[i].length <= 10 
 words[i] consists of lowercase English letters. 
 All the strings of words are unique. 
 

 Related Topics 字典树 数组 字符串 回溯 矩阵 👍 720 👎 0

"""

from typing import *
from PythonLeetcodeRunner import *


# @lc code=start
# leetcode submit region begin(Prohibit modification and deletion)
class Trie:
    def __init__(self):
        self.children = defaultdict(Trie)
        self.word = ""

    def insert(self, word):
        """ Insert word to trie, append the word at the last node """
        cur = self
        for c in word:
            cur = cur.children[c]
        cur.word = word


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # 建立 trie
        trie = Trie()
        for word in words:
            trie.insert(word)

        # dfs 搜索所有可能路径, 并利用 trie 剪枝
        ans = set()
        m, n = len(board), len(board[0])

        def dfs(x, y, cur):
            """ 深度优先遍历 """
            nonlocal ans
            # 打上访问标记
            c = board[x][y]
            board[x][y] = '.'

            # 能到当前点代表当前路径是 trie 的一个前缀
            if len(cur.word):  # trie 的字符结束点会挂载上该字符串
                ans.add(cur.word)

            # 判断是否存在相应的 trie 子节点
            if c not in cur.children:
                board[x][y] = c
                return

            # 若存在该子节点,
            cur_next = cur.children[c]
            if len(cur_next.word):
                ans.add(cur_next.word)

            # dfs
            for i, j in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1),):
                if 0 <= i < m and 0 <= j < n and board[i][j] != '.':
                    dfs(i, j, cur_next)

            # 移除访问标记
            board[x][y] = c

        # 尝试 dfs 遍历所有起点构成的路径
        for i in range(m):
            for j in range(n):
                dfs(i, j, trie)

        return list(ans)


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def dfs(row, col, cur):
            if row < 0 or row >= m or col < 0 or col >= n or board[row][col] == '.' or board[row][
                col] not in cur.children:
                return
            c = board[row][col]
            cur = cur.children[c]
            if cur.word != '':
                ans.add(cur.word)
            board[row][col] = '.'
            dfs(row + 1, col, cur)
            dfs(row - 1, col, cur)
            dfs(row, col + 1, cur)
            dfs(row, col - 1, cur)
            board[row][col] = c

        m, n = len(board), len(board[0])
        ans = set()
        trie = Trie()
        words = set(words)
        for word in words:
            trie.insert(word)
        for i in range(m):
            for j in range(n):
                dfs(i, j, trie)
        return list(ans)


# leetcode submit region end(Prohibit modification and deletion)
# @lc code=end

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
