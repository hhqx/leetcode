question_content = """
There is a safe protected by a password. The password is a sequence of n digits 
where each digit can be in the range [0, k - 1]. 

 The safe has a peculiar way of checking the password. When you enter in a 
sequence, it checks the most recent n digits that were entered each time you type a 
digit. 

 
 For example, the correct password is "345" and you enter in "012345": 
 

 
 After typing 0, the most recent 3 digits is "0", which is incorrect. 
 After typing 1, the most recent 3 digits is "01", which is incorrect. 
 After typing 2, the most recent 3 digits is "012", which is incorrect. 
 After typing 3, the most recent 3 digits is "123", which is incorrect. 
 After typing 4, the most recent 3 digits is "234", which is incorrect. 
 After typing 5, the most recent 3 digits is "345", which is correct and the 
safe unlocks. 
 
 


 Return any string of minimum length that will unlock the safe at some point of 
entering it. 

 
 Example 1: 

 
Input: n = 1, k = 2
Output: "10"
Explanation: The password is a single digit, so enter each digit. "01" would 
also unlock the safe.
 

 Example 2: 

 
Input: n = 2, k = 2
Output: "01100"
Explanation: For each possible password:
- "00" is typed in starting from the 4ᵗʰ digit.
- "01" is typed in starting from the 1ˢᵗ digit.
- "10" is typed in starting from the 3ʳᵈ digit.
- "11" is typed in starting from the 2ⁿᵈ digit.
Thus "01100" will unlock the safe. "10011", and "11001" would also unlock the 
safe.
 

 
 Constraints: 

 
 1 <= n <= 4 
 1 <= k <= 10 
 1 <= kⁿ <= 4096 
 

 Related Topics 深度优先搜索 图 欧拉回路 👍 233 👎 0

"""

from typing import *
from PythonLeetcodeRunner import *


# @lc code=start
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        """
        要生成一个最短的k进制的字符串, 使得其子串包含n位数的k进制串的所有情况

        把前n-1个k进制数(an-1,...,a2,a1)视作节点, 每个节点有k条边, 边ki指向节点(an-2,...,a2,a1, ki)
        边的id组合(node, ki)正好组成一个长度为n的k进制串

        遍历这个有向连通图, 找出欧拉回路(遍历所有边仅一次的路径), 即是最终结果
        """
        mask = 10 ** (n - 1)
        # def get_next(u, ki):
        #     return (u % mask) * 10 + ki

        vis = set()
        result = []

        def dfs(u):
            """ 后序遍历, vis保存的是已经遍历过的边: (node, edge) """
            for edge in range(k):  # 每个节点的边的编号: 0,1,...k-1
                edge_id = u * 10 + edge
                if edge_id in vis:
                    continue
                vis.add(edge_id)
                dfs(edge_id % mask)  # 边的id的后n-1位 -> 下一个节点id
                result.append(str(edge))

        dfs(0)  # dfs 最后遍历到的节点一定是0
        ans = "".join(result)
        return ans + "0" * (n - 1)


# leetcode submit region end(Prohibit modification and deletion)
# @lc code=end

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
