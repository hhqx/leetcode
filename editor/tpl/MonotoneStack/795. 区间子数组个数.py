
question_content = """
给你一个整数数组 nums 和两个整数：left 及 right 。找出 nums 中连续、非空且其中最大元素在范围 [left, right] 内的子数组，并
返回满足条件的子数组的个数。 

 生成的测试用例保证结果符合 32-bit 整数范围。 

 

 示例 1： 

 
# 输入：nums = [2,1,4,3], left = 2, right = 3
# 输出：3
# 解释：满足条件的三个子数组：[2], [2, 1], [3]
 

 示例 2： 

 
输入：nums = [2,9,2,5,6], left = 2, right = 8
输出：7
 

 

 提示： 

 
 1 <= nums.length <= 10⁵ 
 0 <= nums[i] <= 10⁹ 
 0 <= left <= right <= 10⁹ 
 

 Related Topics 数组 双指针 👍 287 👎 0

"""

from typing import *
from PythonLeetcodeRunner import *

# @lc code=start
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:

        """
        单调栈做法, 单调栈枚举所有子区间最值为nums[i]的子区间

        统计所有最大值范围在 [a, b] 之间的子数组个数，可等价为统计每一个范围落在 [a, b] 之间的 nums[i] 作为最大值时子数组的个数。

        """
        n = len(nums)

        # 取[lower_i, upper_i]
        upper = [n] * n
        lower = [-1] * n

        # 单调栈统计每个元素为最大值的最大区间长度
        st = []
        for i, num in enumerate(nums):
            while st and num >= nums[st[-1]]:
                upper[st[-1]] = i
                st.pop()
            # //** 此处统计左侧第一个大于nums[i]的元素  **//
            lower[i] = st[-1] if st else -1
            st.append(i)

        # 枚举最大值为 nums[i] 的所有区间
        ans = 0
        for i in range(n):
            if left <= nums[i] <= right:
                ans += (upper[i] - i) * (i - lower[i])

        return ans


class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        """
        使用单调栈, 统计左侧第一个大于当前元素, 和右侧第一个大于等于当前元素

        单调栈统计左侧第一个大于当前元素: while循环退出后的栈顶即是左侧第一个大于当前元素的位置
            统计右侧第一个大于当前元素可以在while循环内部出栈的时候, 当前元素的位置 是 出栈元素右侧第一个大于的位置

        或者采用倒序遍历的思路, 此时while循环退出时的栈顶元素即是 当前元素右侧第一个大于的位置
        """
        n = len(nums)

        l = [-1] * n
        r = [n] * n

        st = []
        for i in range(n):
            while st and nums[i] >= nums[st[-1]]:
                # r[st[-1]] = i
                st.pop()
            # nums[l[i]] > nums[i]
            l[i] = st[-1] if st else -1
            st.append(i)

        st = []
        for i in range(n-1, -1, -1):
            while st and nums[i] > nums[st[-1]]:
                st.pop()
            # nums[r[i]] >= nums[i]
            r[i] = st[-1] if st else n
            st.append(i)

        ans = 0
        for i in range(n):
            if left <= nums[i] <= right:
                ans += (i - l[i]) * (r[i] - i)

        return ans

# leetcode submit region end(Prohibit modification and deletion)
# @lc code=end

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
