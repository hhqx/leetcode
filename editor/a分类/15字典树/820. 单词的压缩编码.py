question_content = """
单词数组 words 的 有效编码 由任意助记字符串 s 和下标数组 indices 组成，且满足： 

 
 words.length == indices.length 
 助记字符串 s 以 '#' 字符结尾 
 对于每个下标 indices[i] ，s 的一个从 indices[i] 开始、到下一个 '#' 字符结束（但不包括 '#'）的 子字符串 恰好与 
words[i] 相等 
 

 给你一个单词数组 words ，返回成功对 words 进行编码的最小助记字符串 s 的长度 。 

 

 示例 1： 

 
输入：words = ["time", "me", "bell"]
输出：10
解释：一组有效编码为 s = "time#bell#" 和 indices = [0, 2, 5] 。
words[0] = "time" ，s 开始于 indices[0] = 0 到下一个 '#' 结束的子字符串，如加粗部分所示 "time#bell#"
words[1] = "me" ，s 开始于 indices[1] = 2 到下一个 '#' 结束的子字符串，如加粗部分所示 "time#bell#"
words[2] = "bell" ，s 开始于 indices[2] = 5 到下一个 '#' 结束的子字符串，如加粗部分所示 "time#bell#"
 

 示例 2： 

 
输入：words = ["t"]
输出：2
解释：一组有效编码为 s = "t#" 和 indices = [0] 。
 

 

 提示： 

 
 1 <= words.length <= 2000 
 1 <= words[i].length <= 7 
 words[i] 仅由小写字母组成 
 

 Related Topics 字典树 数组 哈希表 字符串 👍 306 👎 0

"""

from typing import *
from PythonLeetcodeRunner import *


# @lc code=start
# leetcode submit region begin(Prohibit modification and deletion)
class Trie:
    def __init__(self):
        self.child = defaultdict(Trie)
        self.word = ""

    def insert(self, word):
        cur = self
        for c in word:
            cur = cur.child[c]
        # cur.word = word


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        """ 字典树建树, 累加根节点到叶子节点的路径长度 """

        def dfs(root: Trie, depth):
            nonlocal ans
            if not root.child:
                ans += depth + 1
            for c, v in root.child.items():
                dfs(v, depth + 1)

        obj = Trie()
        for word in words:
            obj.insert(reversed(word))
        ans = 0
        dfs(obj, 0)

        return ans


# leetcode submit region end(Prohibit modification and deletion)
# @lc code=end

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
