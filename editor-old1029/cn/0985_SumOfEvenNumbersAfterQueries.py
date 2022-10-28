
question_content = """
You are given an integer array nums and an array queries where queries[i] = [
vali, indexi]. 

 For each query i, first, apply nums[indexi] = nums[indexi] + vali, then print 
the sum of the even values of nums. 

 Return an integer array answer where answer[i] is the answer to the iᵗʰ query. 


 
 Example 1: 

 
Input: nums = [1,2,3,4], queries = [[1,0],[-3,1],[-4,0],[2,3]]
Output: [8,6,2,4]
Explanation: At the beginning, the array is [1,2,3,4].
After adding 1 to nums[0], the array is [2,2,3,4], and the sum of even values 
is 2 + 2 + 4 = 8.
After adding -3 to nums[1], the array is [2,-1,3,4], and the sum of even values 
is 2 + 4 = 6.
After adding -4 to nums[0], the array is [-2,-1,3,4], and the sum of even 
values is -2 + 4 = 2.
After adding 2 to nums[3], the array is [-2,-1,3,6], and the sum of even values 
is -2 + 6 = 4.
 

 Example 2: 

 
Input: nums = [1], queries = [[4,0]]
Output: [0]
 

 
 Constraints: 

 
 1 <= nums.length <= 10⁴ 
 -10⁴ <= nums[i] <= 10⁴ 
 1 <= queries.length <= 10⁴ 
 -10⁴ <= vali <= 10⁴ 
 0 <= indexi < nums.length 
 

 Related Topics 数组 模拟 👍 75 👎 0

"""

from typing import *
from PythonLeetcodeRunner import *

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        evenSum = sum(nums[i] for i in range(len(nums)) if nums[i] % 2 == 0)
        answer = []
        for i in range(len(nums)):
            val, idx = queries[i]
            if nums[idx] % 2 == 0:
                evenSum -= nums[idx]
            nums[idx] += val
            if (nums[idx]) % 2 == 0:
                evenSum += nums[idx]
            answer.append(evenSum)

        return answer
# leetcode submit region end(Prohibit modification and deletion)
 


if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
