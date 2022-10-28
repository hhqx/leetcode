#
# @lc app=leetcode.cn id=1856 lang=python3
#
# [1856] 子数组最小乘积的最大值
#
# https://leetcode.cn/problems/maximum-subarray-min-product/description/
#
# algorithms
# Medium (36.97%)
# Likes:    91
# Dislikes: 0
# Total Accepted:    7.6K
# Total Submissions: 20.7K
# Testcase Example:  '[1,2,3,2]'
#

question_content="""一个数组的 最小乘积 定义为这个数组中 最小值 乘以 数组的 和 。


比方说，数组 [3,2,5] （最小值是 2）的最小乘积为 2 * (3+2+5) = 2 * 10 = 20 。


给你一个正整数数组 nums ，请你返回 nums 任意 非空子数组 的最小乘积 的 最大值 。由于答案可能很大，请你返回答案对  10^9 + 7 取余
的结果。

请注意，最小乘积的最大值考虑的是取余操作 之前 的结果。题目保证最小乘积的最大值在 不取余 的情况下可以用 64 位有符号整数 保存。

子数组 定义为一个数组的 连续 部分。



示例 1：


输入：nums = [49,11,35,50,34,1,39,21,32,2,8,24,20,16,4,16,37,6,6,47,32,5,49,35,50,9,9,43,31,36,11,17,34,39,28,14,35,49,47,45,13,46,20,26,43,42,24,29,34,29,8,16,15,5,22,2,38,36,15,38,15,1,5,46,41,4,15,5,3,22,5,33,16,18,43,32,14,35,9,47,37,37,31,16,31,27,13,7,7,43,28,23,28,27,30,47,4,44,42,42]

输出：8085
解释：最小乘积的最大值由子数组 [2,3,2] （最小值是 2）得到。
2 * (2+3+2) = 2 * 7 = 14 。


# 输入：nums = [1,2,3,2]
# 输出：14
# 解释：最小乘积的最大值由子数组 [2,3,2] （最小值是 2）得到。
# 2 * (2+3+2) = 2 * 7 = 14 。


# 示例 2：
# # 输入：nums = [2,4,4,3,1,2]
# # 输出：18
# # 解释：最小乘积的最大值由子数组 [3,3] （最小值是 3）得到。
# # 3 * (3+3) = 3 * 6 = 18 。


输入：nums = [2,3,3,1,2]
输出：18
解释：最小乘积的最大值由子数组 [3,3] （最小值是 3）得到。
3 * (3+3) = 3 * 6 = 18 。


# 示例 3：


# 输入：nums = [3,1,5,6,4,2]
# 输出：60
# 解释：最小乘积的最大值由子数组 [5,6,4] （最小值是 4）得到。
# 4 * (5+6+4) = 4 * 15 = 60 。




提示：


1 
1 


"""

import itertools
from typing import *
from PythonLeetcodeRunner import *

# @lc code=start
class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        MOD = 10**9 + 7

        # 前缀统计
        import itertools, operator
        prefix = [0] + [n for n in itertools.accumulate(nums, operator.add)]

        st = []
        start = [i for i in range(len(nums))]
        end = [len(nums)] * len(nums)
        for i in range(len(nums)):
            idx = i
            while st and nums[i] <= st[-1][0]:  # 把小于当前值得挤掉, 并继承它的值
                _, ii, idx = st.pop()  # ii 为被挤掉点的坐标
                end[ii] = i  # 出现连续相同值时, 前面的不会被后面的终结, 不过此题不影响
            start[i] = idx  # idx 为连续大于等于当前值的起始点
            st.append((nums[i], i, idx))
        
        # while st:
        #     _, idx = st.pop()
        #     end[idx] = len(nums)
        
        func = lambda i: (prefix[end[i]] - prefix[start[i]]) * nums[i]
        ans = max(range(len(nums)), key=func)
        # print()
        print(func(ans), start[ans], end[ans], nums[start[ans]], nums[end[ans]-1])
        print(nums[start[ans]:end[ans]])
        
        
        # print(start)
        # print(end)
        print(prefix, start, end)
        
        # return ans

        return func(ans)

class Solution1:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        mod = 10**9 + 7

        n = len(nums)
        # 数组 left 初始化为 0，数组 right 初始化为 n-1
        # 设置为元素不存在时的特殊值
        left, right = [0] * n, [n - 1] * n
        # 单调栈
        s = list()
        for i, num in enumerate(nums):
            while s and nums[s[-1]] >= num:
                # 这里的 right 是非严格定义的，right[i] 是右侧最近的小于等于 nums[i] 的元素下标
                right[s[-1]] = i - 1
                s.pop()
            if s:
                # 这里的 left 是严格定义的，left[i] 是左侧最近的严格小于 nums[i] 的元素下标
                left[i] = s[-1] + 1
            s.append(i)
        
        # 前缀和
        pre = [0]
        for i, num in enumerate(nums):
            pre.append(pre[-1] + num)
        
        func = lambda i: (pre[right[i] + 1] - pre[left[i]]) * nums[i]
        best = max(range(len(nums)), key=func)
        
        i = best
        print(best, left[i], right[i], nums[left[i]], nums[right[i]])
        print(nums[left[i]:right[i]+1])
        return func(best) % mod

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/maximum-subarray-min-product/solution/zi-shu-zu-zui-xiao-cheng-ji-de-zui-da-zh-rq8r/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
import operator
class Solution:
    MOD = 10**9 + 7
    def maxSumMinProduct(self, nums: List[int]) -> int:
        
        n = len(nums)

        # 前缀和
        prefix = [0] + list(itertools.accumulate(nums, operator.add))
        
        # 单调栈求出每个点的最小值终止点(向左右延伸至碰到更小值)
        start = [0] * n  # 闭区间
        end = [n] * n  # 开区间
        st = []
        for i in range(n):
            while st and nums[i] <= nums[st[-1]]:
                end[st[-1]] = i  # 栈顶大于等于当前元素, 所以当前元素是栈顶的终点(连续相同元素的话,只有最后一个的结束点是正确的)
                st.pop()
            if st: # 退出循环后大于栈顶, 所以栈顶是当前元素起始点
                start[i] = st[-1] + 1  # 此处取闭区间
            st.append(i)
        
        # 枚举计算每个元素作为最小值的最小乘积结果
        func = lambda i: (prefix[end[i]] - prefix[start[i]]) * nums[i]
        ans = max(range(n), key=func)
        
        return func(ans)


# @lc code=end


if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()

