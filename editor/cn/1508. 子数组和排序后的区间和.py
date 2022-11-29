
question_content = """
给你一个数组 nums ，它包含 n 个正整数。你需要计算所有非空连续子数组的和，并将它们按升序排序，得到一个新的包含 n * (n + 1) / 2 个数字的
数组。 

 请你返回在新数组中下标为 left 到 right （下标从 1 开始）的所有数字和（包括左右端点）。由于答案可能很大，请你将它对 10^9 + 7 取模后返
回。 

 
输入：nums = [1,2,3,4], n = 4, left = 1, right = 10
输出：50
 
 示例 1： 

 
输入：nums = [1,2,3,4], n = 3, left = 1, right = 2
输出：3 
解释：所有的子数组和为 1, 3, 6, 10, 2, 5, 9, 3, 7, 4 。将它们升序排序后，我们得到新的数组 [1, 2, 3, 3, 4, 5, 
6, 7, 9, 10] 。下标从 le = 1 到 ri = 5 的和为 1 + 2 + 3 + 3 + 4 = 13 。
 

 示例 2： 

 
输入：nums = [1,2,3,4], n = 4, left = 3, right = 4
输出：6
解释：给定数组与示例 1 一样，所以新数组为 [1, 2, 3, 3, 4, 5, 6, 7, 9, 10] 。下标从 le = 3 到 ri = 4 的和为 
3 + 3 = 6 。
 

 示例 3： 

 
输入：nums = [1,2,3,4], n = 4, left = 1, right = 10
输出：50
 

 

 提示： 

 
 1 <= nums.length <= 10^3 
 nums.length == n 
 1 <= nums[i] <= 100 
 1 <= left <= right <= n * (n + 1) / 2 
 

 Related Topics 数组 双指针 二分查找 排序 👍 62 👎 0

"""

from typing import *
from PythonLeetcodeRunner import *

# @lc code=start
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        """ 状压dp, 原始版(第一次调通) """
        total = sum(nums)
        dp = [[0] * (total + 1) for _ in range(len(nums))]
        # dp[0] = 1
        # dp[i][s] 表示以i为区间右端点,和为 s 的子数组个数
        dp[0][nums[0]] = 1
        for i in range(len(nums)):
            dp[i][0] = 1

        d = [0] * (total + 1)
        d[nums[0]] = 1
        for i in range(1, len(nums)):
            num = nums[i]
            for s in range(0, total + 1 - num):
                dp[i][s + num] += dp[i-1][s]
                d[s + num] += dp[i][s + num]

        tmp = right - left + 1
        ans = 0
        cnt = 0
        # p = [0]
        print(dp)

        dp = d
        for s in range(1, len(dp)):
            freq = dp[s]
            cnt += freq
            # val 为这次可以拿几个
            if cnt >= left:
                val = min(freq, cnt - left + 1)

                if tmp >= val:
                    ans += val * s
                    print(val, s, val * s)
                    tmp -= val
                else:
                    ans += tmp * s
                    tmp -= tmp
                    print(tmp * s)
                    break

        return ans

class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        """ 状压dp统计所有子数组和的次数, 时间复杂度: n*S, 空间复杂度: n+S """
        total = sum(nums)
        dp = [defaultdict(int) for _ in range(len(nums)+1)]
        # dp[i][s] 表示以i为区间右端点(开区间),和为 s 的子数组个数
        for i in range(len(nums)+1):
            dp[i][0] = 1

        CounterSum = [0] * (total + 1)
        for i in range(0, len(nums)):
            num = nums[i]
            for s in dp[i-1]:
                dp[i][s + num] += dp[i-1][s]
                CounterSum[s + num] += dp[i][s + num]

        ans = 0

        # 下面从一个排好序的子数组和中取 number = right - left + 1个, 把他们累加起来
        number = right - left + 1

        # CounterSum 是一个数组形式的哈希表, CounterSum[i]存在和为 i 的子区间个数
        # pcnt 记录当前小于等于 i 的子数组和有多少个
        pcnt = 0
        for s in range(1, len(CounterSum)):
            freq = CounterSum[s]
            pcnt += freq
            if pcnt >= left:  # pcnt >= left 时才开始取
                # val 为本次最多可以取几个
                val = min(freq, pcnt - left + 1)
                if number >= val:  # 如果剩余数量大于当前可取最大值, 取val个
                    ans += val * s  # 取val个和为s的子区间
                    number -= val
                else:
                    # 取完剩下的容量, 退出
                    ans += number * s
                    number -= number
                    break

        return ans
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        """ 状压dp统计所有子数组和的次数 + 滚动数组, 时间复杂度: n*S, 空间复杂度: n+S """
        mod = int(1e9+7)
        total = sum(nums)
        dp = [defaultdict(int) for _ in range(len(nums)+1)]
        # dp[i][s] 表示以i为区间右端点(开区间),和为 s 的子数组个数
        # for i in range(len(nums)+1):
        #     dp[i][0] = 1
        dpi = defaultdict(int)
        dpi[0] = 1

        CounterSum = [0] * (total + 1)
        for i in range(0, len(nums)):
            num = nums[i]
            dpi1 = defaultdict(int)
            dpi1[0] = 1
            for s in dpi:
                dpi1[s + num] += dpi[s]
                CounterSum[s + num] += dpi1[s + num]
            dpi = dpi1

        ans = 0

        # 下面从一个排好序的子数组和中取 number = right - left + 1个, 把他们累加起来
        number = right - left + 1

        # CounterSum 是一个数组形式的哈希表, CounterSum[i]存在和为 i 的子区间个数
        # pcnt 记录当前小于等于 i 的子数组和有多少个
        pcnt = 0
        for s in range(1, len(CounterSum)):
            freq = CounterSum[s]
            pcnt += freq
            if pcnt >= left:  # pcnt >= left 时才开始取
                # val 为本次最多可以取几个
                val = min(freq, pcnt - left + 1)
                if number >= val:  # 如果剩余数量大于当前可取最大值, 取val个
                    ans += val * s  # 取val个和为s的子区间
                    number -= val
                else:
                    # 取完剩下的容量, 退出
                    ans += number * s
                    number -= number
                    break
                ans %= mod

        return ans % mod

# leetcode submit region end(Prohibit modification and deletion)
# @lc code=end

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
