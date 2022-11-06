question_content = """
Given an integer array nums, find the subarray which has the largest sum and 
return its sum. 

 
 Example 1: 

 
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
 

 Example 2: 

 
Input: nums = [1]
Output: 1
 

 Example 3: 

 
Input: nums = [5,4,-1,7,8]
Output: 23
 

 
 Constraints: 

 
 1 <= nums.length <= 10⁵ 
 -10⁴ <= nums[i] <= 10⁴ 
 

 
 Follow up: If you have figured out the O(n) solution, try coding another 
solution using the divide and conquer approach, which is more subtle. 

 Related Topics 数组 分治 动态规划 👍 5422 👎 0

"""

from typing import *
from PythonLeetcodeRunner import *


# @lc code=start
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        分治法, 时间复杂度: o(n*log(n)), 空间复杂度: o(log(n))

        分治 一分二, 二分四, 当数组规模为 1 时, 最大连续子数组即为本身

        1. 子问题融合时仅有子数组的最大和是不够的, 一种方法是:
            每个子数组 arr[i:j+1] 求解出:
                (1) 以 arr[i] 为起点的最大子数组和
                (2) 以 arr[j] 为结束点的最大子数组和
                (3) arr[i:j+1] 内的最大子数组和

        2. 融合条件:
            arr[i:m+1] 和 arr[m+1:j+1] 的结果融合成 arr[i:j+1] 的结果:
            (1) 最大子数组和
            arr[i:j+1] 的最大子数组和 = max(
                arr[i:m+1] 的最大子数组和,
                arr[m+1:j+1] 的最大子数组和,
                arr[i:m+1] 以 arr[m] 为结束点的最大子数组和 +
                    arr[m+1:j+1] 以 arr[m+1] 为起点的最大子数组和
            )
            (2) 左侧 arr[i] 为起点的最大子数组和
            arr[i:j+1] 最左侧起始的最大子数组和 = max(
                arr[i:m+1] 左侧起始的最大子数组和,
                arr[i:m+1] 的总和 + arr[m+1:j] 左侧起始的最大子数组和
            )
            (3) 右侧 arr[j] 为终点的最大子数组和
            arr[i:j+1] 最右侧终止的最大子数组和 = max(
                arr[m+1:j+1] 左侧起始的最大子数组和,
                arr[m+1:j+1] 的总和 + arr[i:m+1] 最右侧终止的最大子数组和
            )

        3. 终止条件
            当 子数组长度 <= 2 时, 直接求解上述三个量返回即可


        """
        n = len(nums)
        prefix = [0]
        for num in nums:  # 沃日, 之前这里for循环变量写成了n, 覆盖了数组长度n. 偶买噶!, 枯死.
            prefix.append(prefix[-1] + num)

        def dfs(i, j):
            # 分治 dfs 递归到小问题, 直接求解
            if j - i <= 2:
                total = prefix[j] - prefix[i]
                return max(total, nums[i]), max(total, nums[i], nums[j - 1]), max(total, nums[j - 1])

            # 下面将大问题划分成两个子问题求解
            mid = (i + j) // 2

            # ml, m, mr 分别代表子数组的三种最大连续和
            # lml 为: 左半部分子数组以左边第一个元素为起点的最大子数组和
            # lm 为: 左半部分子数组的最大子数组和
            # lmr 为: 左半部分子数组以右边最后一个元素为终点的最大子数组和
            lml, lm, lmr = dfs(i, mid)
            rml, rm, rmr = dfs(mid, j)

            # 融合子问题的计算结果到本问题
            res = (
                max([lml, prefix[mid] - prefix[i] + rml]),
                max([lm, rm, lmr + rml]),
                max([rmr, prefix[j] - prefix[mid] + lmr])
            )

            return res

        lmx, mx, rmx = dfs(0, n)
        return mx

# leetcode submit region end(Prohibit modification and deletion)
# @lc code=end

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
