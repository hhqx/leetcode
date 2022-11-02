
question_content = """
Given an array of integers arr, find the sum of min(b), where b ranges over 
every (contiguous) subarray of arr. Since the answer may be large, return the 
answer modulo 10⁹ + 7. 

 
 Example 1: 

 
Input: arr = [3,1,2,4]
Output: 17
Explanation: 
Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,
4]. 
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
Sum is 17.
 

 Example 2: 

 
Input: arr = [11,81,94,43,3]
Output: 444
 

 
 Constraints: 

 
 1 <= arr.length <= 3 * 10⁴ 
 1 <= arr[i] <= 3 * 10⁴ 
 

 Related Topics 栈 数组 动态规划 单调栈 👍 567 👎 0

"""

from typing import *
from PythonLeetcodeRunner import *

# @lc code=start
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    """ 单调栈法 """
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        # i,j在[0,n)中共有n*n种选择方式, 其中n中i=j, 剩下i在j前或后的数量对半分,
        # 故不合法数量为 (n*n - n)/2 = n(n-1)/2, 合法数量为
        # arr = arr + [float('-inf')]
        q = deque()
        # left, right 表示在 (left[i], right[i]) 区间内, arr的最小值为 arr[i]
        left = [-1] * n  # (left, i]是区间左边的选择
        right = [n] * n  # [i, right)是区间右边的选择
        for i in range(n):
            while q and arr[i] <= arr[q[0]]:
                start = q.popleft()
                right[start] = i
            left[i] = q[0] if q else -1
            q.appendleft(i)

        ans = sum((i-left[i]) * (right[i]-i) * arr[i] for i in range(n))
        return ans % (int(1e9+7))
# leetcode submit region end(Prohibit modification and deletion)
# @lc code=end

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
