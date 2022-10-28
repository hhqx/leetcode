question_content = """
We are given hours, a list of the number of hours worked per day for a given 
employee. 

 A day is considered to be a tiring day if and only if the number of hours 
worked is (strictly) greater than 8. 

 A well-performing interval is an interval of days for which the number of 
tiring days is strictly larger than the number of non-tiring days. 

 Return the length of the longest well-performing interval. 

 
 Example 1: 

 
Input: hours = [9,9,6,0,6,6,9]
Output: 3
Explanation: The longest well-performing interval is [9,9,6].
 

 Example 2: 

 
Input: hours = [6,6,9]
Output: 1
 
 
Input: hours = [6,6,6]
Output: 0
 

 
 Constraints: 

 
 1 <= hours.length <= 10⁴ 
 0 <= hours[i] <= 16 
 

 Related Topics 栈 数组 哈希表 前缀和 单调栈 👍 227 👎 0

"""

from typing import *
from PythonLeetcodeRunner import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        f = lambda x: 1 if x > 8 else -1
        # prefix = [f(hours[0])]
        prefix = [0]
        for i in range(0, len(hours)):
            prefix.append(prefix[-1] + f(hours[i]))
        # print(prefix)

        nums = prefix
        st = []
        for i in range(len(nums)):
            if not st or nums[i] < nums[st[-1]]:
                st.append(i)

        ans = 0
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] > 0:
                ans = max(ans, i - 1)
            while st and nums[i] > nums[st[-1]]:
                v = st.pop()
                ans = max(ans, i - v)

        return ans


class Solution1:
    def longestWPI(self, hours: List[int]) -> int:
        arr = []
        for val in hours:
            if val > 8:
                arr.append(1)
            else:
                arr.append(-1)

        prefixSum = []  # 前缀和数组
        cur_sum = 0
        for val in arr:
            prefixSum.append(cur_sum)
            cur_sum += val
        prefixSum.append(cur_sum)

        stk = []
        for i in range(len(prefixSum)):
            if len(stk) == 0 or prefixSum[stk[-1]] > prefixSum[i]:
                stk.append(i)  # 因为最终需要的答案是最长距离,需要下标来计算,所以这里存储下标

        res = 0
        # 逆向遍历prefixSum
        for j in range(len(prefixSum) - 1, -1, -1):
            # 成立的话, (stk[-1], j)是一个候选项
            while len(stk) != 0 and prefixSum[j] > prefixSum[stk[-1]]:
                res = max(res, j - stk[-1])
                stk.pop()

        return res

    # 作者：jian - xi - mo - fa - shi - 2
    # 链接：https: // leetcode.cn / problems / longest - well - performing - interval / solution / can - kao - liao - ji - ge - da - shen - de - ti - jie - zhi - hou - zong - /
    # 来源：力扣（LeetCode）
    # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
