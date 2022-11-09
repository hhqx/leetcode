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

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def findWord(word, m, n, board, d) -> bool:
            if word[:4] == word[0] * 4:
                word = ''.join([c for c in reversed(word)])
            starts = []
            stack = []
            visited = set()
            for i in range(m):
                for j in range(n):
                    if board[i][j] == word[0]:
                        if len(word) == 1:
                            return True
                        starts.append((i, j))
            for start in starts:
                stack.append(start)
                visited.add((start,))
                l = 1
                while stack != [] and l < len(word):
                    x, y = stack[-1]
                    for dxy in d:
                        nx, ny = x + dxy[0], y + dxy[1]
                        if 0 <= nx < m and 0 <= ny < n:
                            if board[nx][ny] == word[l]:
                                if (nx, ny) not in stack and tuple(stack) + ((nx, ny),) not in visited:
                                    stack.append((nx, ny))
                                    visited.add(tuple(stack))
                                    l += 1
                                    if l == len(word):
                                        return True
                                    break
                    else:
                        stack.pop()
                        l -= 1
            else:
                return False

        m = len(board)
        n = len(board[0])
        res = []

        d = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        ref = set()
        for i in range(m):
            for j in range(n - 1):
                ref.add(board[i][j] + board[i][j + 1])
        for j in range(n):
            for i in range(m - 1):
                ref.add(board[i][j] + board[i + 1][j])

        skip_cnt = 0
        for word in words:
            f = True
            for i in range(len(word) - 1):
                if word[i:i + 2] not in ref and word[i + 1] + word[i] not in ref:
                    f = False
                    break
            if not f:
                skip_cnt += 1
                continue
            if findWord(word, m, n, board, d):
                res.append(word)

        print(f'left words: {len(words) - skip_cnt}, skipped: {skip_cnt}')
        return res


# leetcode submit region end(Prohibit modification and deletion)
# @lc code=end

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
