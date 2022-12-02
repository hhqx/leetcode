
question_content = """
给你一个整数数组 nums ，返回 nums 中所有 等差子序列 的数目。 

 如果一个序列中 至少有三个元素 ，并且任意两个相邻元素之差相同，则称该序列为等差序列。 

 
 例如，[1, 3, 5, 7, 9]、[7, 7, 7, 7] 和 [3, -1, -5, -9] 都是等差序列。 
 再例如，[1, 1, 2, 5, 7] 不是等差序列。 
 

 数组中的子序列是从数组中删除一些元素（也可能不删除）得到的一个序列。 

 
 例如，[2,5,10] 是 [1,2,1,2,4,1,5,10] 的一个子序列。 
 

 题目数据保证答案是一个 32-bit 整数。 

 
 
输入：nums = [7,7,7,7,7]
输出：16
解释：数组中的任意子序列都是等差子序列。

 示例 1： 

 
输入：nums = [2,4,6,8,10]
输出：7
解释：所有的等差子序列为：
[2,4,6]
[4,6,8]
[6,8,10]
[2,4,6,8]
[4,6,8,10]
[2,4,6,8,10]
[2,6,10]
 

 示例 2： 


 

 

 提示： 

 
 1 <= nums.length <= 1000 
 -2³¹ <= nums[i] <= 2³¹ - 1 
 

 Related Topics 数组 动态规划 👍 266 👎 0

"""

from typing import *
from PythonLeetcodeRunner import *

# @lc code=start
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        """ 状态压缩, 动态规划 """
        n = len(nums)

        # dp[d][x][m] 表示nums[:i+1]的子序列中, 长度为d,最后一个元素为x, 公差为m的子序列个数
        dp = [defaultdict(dict) for _ in range(n + 1)]

        for i in range(n):
            num = nums[i]

            # 滚动数组(优化数组i维度)的情况下, 需要逆序更新
            # for d in range(n, 3 - 1, -1):
            for d in range(min(i+1, n), 3 - 1, -1):
                # 遍历dp[d-1]的每一个结尾元素 x
                for x in dp[d - 1]:
                    # x + m == num
                    m = num - x
                    # 如果长度为d-1的, 公差为m的 子序列存在
                    if m in dp[d - 1][x]:
                        # 说明加上num, 长度为d, 公差为m的子序列, 相比之前多了cnt个, 累加上cnt
                        cnt = dp[d - 1][num - m][m]
                        dp[d][num][m] = cnt + dp[d][num].get(m, 0)
            # d=2, 长度为2的子序列的dp初始化
            for j in range(i):
                m = num - nums[j]
                dp[2][num][m] = 1 + dp[2][num].get(m, 0)

        # print(dp)
        ans = 0
        for d in range(3, n + 1):
            for x in dp[d]:
                ans += sum(dp[d][x].values())

        return ans


# leetcode submit region end(Prohibit modification and deletion)
# @lc code=end

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
