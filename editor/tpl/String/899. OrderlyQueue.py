
question_content = """
You are given a string s and an integer k. You can choose one of the first k 
letters of s and append it at the end of the string.. 

 Return the lexicographically smallest string you could have after applying the 
mentioned step any number of moves. 

 
 Example 1: 

 
Input: s = "cba", k = 1
Output: "acb"
Explanation: 
In the first move, we move the 1ˢᵗ character 'c' to the end, obtaining the 
string "bac".
In the second move, we move the 1ˢᵗ character 'b' to the end, obtaining the 
final result "acb".
 

 Example 2: 

 
Input: s = "baaca", k = 3
Output: "aaabc"
Explanation: 
In the first move, we move the 1ˢᵗ character 'b' to the end, obtaining the 
string "aacab".
In the second move, we move the 3ʳᵈ character 'c' to the end, obtaining the 
final result "aaabc".
 

 
 Constraints: 

 
 1 <= k <= s.length <= 1000 
 s consist of lowercase English letters. 
 

 Related Topics 数学 字符串 排序 👍 180 👎 0

"""

from typing import *
from PythonLeetcodeRunner import *

# @lc code=start
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        """

        k = 1, 最小表示法, 参考宫水三叶模板, o(n)
        k > 1, 排序
        时间复杂度: o(n*log(n))
        """
        if k >= 2:
            # python 字符串无法直接排序, 只能 sorted(s) 后再 join
            return ''.join(sorted(s))

        # 最小表示法
        # 此处的 k 表示 i,j 后面有多少个公共字符
        # 这里的 i,j 没有前后顺序关系, 虽然也可以设计成 i<j, 但代码会多几步且效益不高
        n = len(s)
        i, j, k = 0, 1, 0
        while i < n and j < n and k < n:
            a, b = s[(i + k) % n], s[(j + k) % n]  # 淦, 之前这句忘放进循环里了, 我是xx
            if a == b:
                k += 1
            else:
                # 判断 s[i:i+k+1], s[j:j+k+1] 哪个更大,
                # 保留更小的, 移动更大到第一个不相等的位置(因为这中间的相等位置一定也更大)
                if a < b:
                    j += k + 1
                else:
                    i += k + 1
                k = 0
                # 上述处理后i可能等于j, 需跳过这种情况
                if i == j:
                    i += 1
        i = min(i, j)
        return s[i:] + s[:i]
# leetcode submit region end(Prohibit modification and deletion)
# @lc code=end

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
