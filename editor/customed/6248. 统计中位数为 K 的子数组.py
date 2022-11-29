question_content = """
6248. 统计中位数为 K 的子数组 显示英文描述 
通过的用户数369
尝试过的用户数671
用户总通过次数396
用户总提交次数958
题目难度Hard


给你一个长度为 n 的数组 nums ，该数组由从 1 到 n 的 不同 整数组成。另给你一个正整数 k 。

统计并返回 num 中的 中位数 等于 k 的非空子数组的数目。

注意：

数组的中位数是按 递增 顺序排列后位于 中间 的那个元素，如果数组长度为偶数，则中位数是位于中间靠 左 的那个元素。
例如，[2,3,1,4] 的中位数是 2 ，[8,4,3,5,1] 的中位数是 4 。
子数组是数组中的一个连续部分。
 

示例 1：
Input: [2,5,1,4,3,6], 1
Output: 3

输入：nums = [3,2,1,4,5], k = 4
输出：3
解释：中位数等于 4 的子数组有：[4]、[4,5] 和 [1,4,5] 。
示例 2：

输入：nums = [2,3,1], k = 3
输出：1
解释：[3] 是唯一一个中位数等于 3 的子数组。
 

提示：

n == nums.length
1 <= n <= 105
1 <= nums[i], k <= n
nums 中的整数互不相同

"""


from typing import *
from PythonLeetcodeRunner import *

# @lc code=start
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        """ 中心扩展 + 哈希表, 时间: o(n), 空间: o(n) """
        n = len(nums)
        ans = 0

        for i in range(n):
            if nums[i] == k:
                # 往左扩展, 记录所有的 (左大-左小) 的频次
                dl = defaultdict(int)
                large, less = 0, 0
                for left in range(i, -1, -1):
                    if nums[left] > k:
                        large += 1
                    elif nums[left] < k:
                        less += 1
                    dl[large-less] += 1

                # 往右扩展, 中位数等于k的充要条件是: 左小+右小=左大+右大 => 左大-左小=右小-右大 + (0/1)
                large, less = 0, 0
                for right in range(i, n):
                    if nums[right] > k:
                        large += 1
                    elif nums[right] < k:
                        less += 1
                    ans += dl[(less-large)] + dl[(less-large+1)]
                break
        return ans


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        """ 转化为: 求子数组和大于零的
        求子数组[l,r]中位数大于等于k等价于: Q+E-L > 0, 其中Q,E,L分别是大于,等于和小于k的个数
        """
        def count(k):
            """ 统计nums子数组中中位数大于等于k的 个数  """
            arr = [1 if ni >= k else -1 for ni in nums]
            ret = 0
            curSum, prefix = 0, SortedList([0])
            for i in range(len(arr)):
                curSum += arr[i]
                # idx 为和大于零的子数组个数
                idx = prefix.bisect_left(curSum)
                ret += idx
                prefix.add(curSum)
            return ret

        return count(k) - count(k+1)
# leetcode submit region end(Prohibit modification and deletion)
# @lc code=end

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
