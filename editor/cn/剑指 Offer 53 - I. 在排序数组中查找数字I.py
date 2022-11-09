
question_content = """
统计一个数字在排序数组中出现的次数。 

 

 示例 1: 

 
输入: nums = [5,7,7,8,8,10], target = 8
输出: 2 

 示例 2: 

 
输入: nums = [5,7,7,8,8,10], target = 6
输出: 0 

 

 提示： 

 
 0 <= nums.length <= 10⁵ 
 -10⁹ <= nums[i] <= 10⁹ 
 nums 是一个非递减数组 
 -10⁹ <= target <= 10⁹ 
 

 

 注意：本题与主站 34 题相同（仅返回值不同）：https://leetcode-cn.com/problems/find-first-and-last-
position-of-element-in-sorted-array/ 

 Related Topics 数组 二分查找 👍 371 👎 0

"""

from typing import *
from PythonLeetcodeRunner import *

# @lc code=start
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bisect_larger(arr, tar, includeEqual=True):
            """
            Find the first arr[i] which is larger than tar.
            return the index.

            """

            # 这个模板中返回 right, right 初始值是 len(arr)
            # 找的是第一个大于(等于)某个数的
            # 闭区间的情况下, left 始终需要 + 1, 更新左边的条件始终是 <(=) , 区间左边所有情况会全部满足

            left, right = 0, len(arr)
            if includeEqual:
                while right > left:
                    mid = left + right >> 1  # 要么 (a+b)//2, 要么 a+b>>1, 写错成 a+b>>2, 偶买噶.
                    if arr[mid] < tar:
                        # 丢弃左边区间
                        left = mid + 1
                    else:
                        right = mid
            else:
                while right > left:
                    mid = left + right >> 1
                    if arr[mid] <= tar:
                        # 丢弃左边区间
                        left = mid + 1
                    else:
                        right = mid

            return right

        left = bisect_larger(nums, target, includeEqual=True)
        right = bisect_larger(nums, target, includeEqual=False)

        return right - left
    # leetcode submit region end(Prohibit modification and deletion)
# @lc code=end

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
