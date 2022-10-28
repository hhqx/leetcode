
question_content = """
You are given an integer array arr of length n that represents a permutation of 
the integers in the range [0, n - 1]. 

 We split arr into some number of chunks (i.e., partitions), and individually 
sort each chunk. After concatenating them, the result should equal the sorted 
array. 

 Return the largest number of chunks we can make to sort the array. 

 
 Example 1: 

 
Input: arr = [1,2,0,3]
Output: 2
 
Input: arr = [4,3,2,1,0]
Output: 1
Explanation:
Splitting into two or more chunks will not return the required result.
For example, splitting into [4, 3], [2, 1, 0] will result in [3, 4, 0, 1, 2], 
which isn't sorted.
 

 Example 2: 

 
Input: arr = [1,0,2,3,4]
Output: 4
Explanation:
We can split into two chunks, such as [1, 0], [2, 3, 4].
However, splitting into [1, 0], [2], [3], [4] is the highest number of chunks 
possible.
 

 
 Constraints: 

 
 n == arr.length 
 1 <= n <= 10 
 0 <= arr[i] < n 
 All the elements of arr are unique. 
 

 Related Topics 栈 贪心 数组 排序 单调栈 👍 294 👎 0

"""

from typing import *
from PythonLeetcodeRunner import *

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        """
        双指针遍历(或者叫单次循环贪心?), 统计 [left, right] 区间内的极值, 若等于窗口左右索引则分割一次
        """

        # 算法流程: 统计 [left, right] 区间内的极值, 若等于窗口左右索引则分割一次
        ans = 0
        left = 0
        Max, Min = float('-inf'), float('inf')
        for right in range(len(arr)):
            Max = max(Max, arr[right])
            Min = min(Min, arr[right])
            if Max == right and Min == left:
                ans += 1
                left = right+1
                Max, Min = float('-inf'), float('inf')

        return ans

# leetcode submit region end(Prohibit modification and deletion)
 


if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
