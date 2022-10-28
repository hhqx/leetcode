
question_content = """
You are given an integer array nums and an integer k. 

 Find the longest subsequence of nums that meets the following requirements: 

 
 The subsequence is strictly increasing and 
 The difference between adjacent elements in the subsequence is at most k. 
 

 Return the length of the longest subsequence that meets the requirements. 

 A subsequence is an array that can be derived from another array by deleting 
some or no elements without changing the order of the remaining elements. 

 
 Example 1: 

 
Input: nums = [4,2,1,4,3,4,5,8,15], k = 3
Output: 5
Explanation:
The longest subsequence that meets the requirements is [1,3,4,5,8].
The subsequence has a length of 5, so we return 5.
Note that the subsequence [1,3,4,5,8,15] does not meet the requirements because 
15 - 8 = 7 is larger than 3.
 

 Example 2: 

 
Input: nums = [7,4,5,1,8,12,4,7], k = 5
Output: 4
Explanation:
The longest subsequence that meets the requirements is [4,5,8,12].
The subsequence has a length of 4, so we return 4.
 

 Example 3: 

 
Input: nums = [1,5], k = 1
Output: 1
Explanation:
The longest subsequence that meets the requirements is [1].
The subsequence has a length of 1, so we return 1.
 

 
Input: nums = [1,100,500,100000,100000], k = 100000
Output: 4
Explanation:
The longest subsequence that meets the requirements is [1].
The subsequence has a length of 1, so we return 1.
 

 
 Constraints: 

 
 1 <= nums.length <= 10⁵ 
 1 <= nums[i], k <= 10⁵ 
 

 Related Topics 树状数组 线段树 队列 数组 分治 动态规划 单调队列 👍 42 👎 0

"""

from typing import *
from PythonLeetcodeRunner import *

# leetcode submit region begin(Prohibit modification and deletion)
from sortedcontainers import SortedDict
NUM_MIN, NUM_MAX = int(1), int(1e5)

class class_dp_dict:
    def __init__(self):
        self.dp = SortedDict()

    def find_dp_between_xy(self, L, R):
        """ [L,R]区间内dp数组的最大值 """
        ans = 0
        for k, v in self.dp.items():
            if L <= k <= R:
                ans = max(ans, v)
        return ans

    def update(self, k, v):
        self.dp[k] = v
        return True

    def query(self, k):
        return self.dp.get(k, -1)

    def max(self):
        return max(self.dp.values())


class class_dp_segment:
    def __init__(self, MIN=NUM_MIN, MAX=NUM_MAX):
        self.START = MIN-1
        self.END = MAX
        self.root = [0] * (4*MAX)

    def modify(self, idx: int, l: int, r: int, i: int, val: int) -> None:
        mx = self.root
        if l == r:
            mx[idx] = val
            return
        m = (l + r) // 2
        if i <= m:
            self.modify(idx * 2, l, m, i, val)
        else:
            self.modify(idx * 2 + 1, m + 1, r, i, val)
        mx[idx] = max(mx[idx * 2], mx[idx * 2 + 1])

    # 返回区间 [L,R] 内的最大值
    def query(self, idx: int, l: int, r: int, L: int, R: int) -> int:  # L 和 R 在整个递归过程中均不变，将其大写，视作常量
        mx = self.root
        if L <= l and r <= R: return mx[idx]
        res = 0
        m = (l + r) // 2
        if L <= m: res = self.query(idx * 2, l, m, L, R)
        if R > m: res = max(res, self.query(idx * 2 + 1, m + 1, r, L, R))
        return res

    def find_dp_between_xy(self, L, R):
        return self.query(1, self.START, self.END, L, R)

    def update(self, k, v):
        self.modify(1, self.START, self.END, k, v)
        return True

    def max(self):
        return self.root[1]


class Solution:
    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        # dp = class_dp_dict()
        dp = class_dp_segment(MIN=min(nums), MAX=max(nums))

        for i in range(len(nums)):
            max_dp_between_xy = dp.find_dp_between_xy(L=max(1, nums[i]-k), R=nums[i]-1)

            if max_dp_between_xy == 0:
                dp.update(nums[i], 1)
            else:
                v = max_dp_between_xy + 1
                dp.update(nums[i], v)

        return dp.max()

# leetcode submit region end(Prohibit modification and deletion)



if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
