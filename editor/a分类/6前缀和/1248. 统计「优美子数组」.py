import bisect
import itertools

question_content = """
给你一个整数数组 nums 和一个整数 k。如果某个连续子数组中恰好有 k 个奇数数字，我们就认为这个子数组是「优美子数组」。 

 请返回这个数组中 「优美子数组」 的数目。 

 

 示例 1： 

 
输入：nums = [1,1,2,1,1], k = 3
输出：2
解释：包含 3 个奇数的子数组是 [1,1,2,1] 和 [1,2,1,1] 。
 

 示例 2： 

 
输入：nums = [2,4,6], k = 1
输出：0
解释：数列中不包含任何奇数，所以不存在优美子数组。
 

 示例 3： 

 
输入：nums = [2,2,2,1,2,2,1,2,2,2], k = 2
输出：16
 

 

 提示： 

 
 1 <= nums.length <= 50000 
 1 <= nums[i] <= 10^5 
 1 <= k <= nums.length 
 

 Related Topics 数组 哈希表 数学 滑动窗口 👍 258 👎 0

"""

from typing import *
from PythonLeetcodeRunner import *


# @lc code=start
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        p = list(itertools.accumulate((num % 2 for num in nums), initial=0))
        ans = 0
        for i in range(1, n + 1):
            l = bisect.bisect_left(p, p[i] - k, hi=i)
            r = bisect.bisect_right(p, p[i] - k, hi=i)
            ans += r - l
        return ans

    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        """ 有点类似滑动窗口, 求出包含k个奇数的区间的左右边界 """
        n = len(nums)
        d = {0: -1}
        cnt = 0
        for i, num in enumerate(nums):
            if num % 2 == 1:
                cnt += 1
                d[cnt] = i
        else:
            d[cnt + 1] = n
        ans = 0
        for i in range(0, cnt+1):
            if i >= k:
                l = d[i - k]
                dl = d[i - k + 1] - l
                r = d[i + 1]
                dr = r - d[i]
                ans += dl * dr
        return ans

    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        """ 哈希表+前缀和 """
        n = len(nums)
        d = defaultdict(int)
        d[0] = 1
        s = 0
        ans = 0
        for i in range(n):
            s += nums[i] % 2 == 1
            ans += d[s - k]
            d[s] += 1
        return ans


# leetcode submit region end(Prohibit modification and deletion)
# @lc code=end

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
