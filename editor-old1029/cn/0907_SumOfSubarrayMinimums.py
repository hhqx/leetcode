
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
 

 Related Topics 栈 数组 动态规划 单调栈 👍 549 👎 0

"""

from typing import *
from PythonLeetcodeRunner import *

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
# leetcode submit region end(Prohibit modification and deletion)
 


if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
