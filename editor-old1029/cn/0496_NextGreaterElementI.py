
question_content = """
The next greater element of some element x in an array is the first greater 
element that is to the right of x in the same array. 

 You are given two distinct 0-indexed integer arrays nums1 and nums2, where 
nums1 is a subset of nums2. 

 For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j]
 and determine the next greater element of nums2[j] in nums2. If there is no 
next greater element, then the answer for this query is -1. 

 Return an array ans of length nums1.length such that ans[i] is the next 
greater element as described above. 

 
 Example 1: 

 
Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so 
the answer is -1.
- 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
- 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so 
the answer is -1.
 

 Example 2: 

 
Input: nums1 = [2,4], nums2 = [1,2,3,4]
Output: [3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 2 is underlined in nums2 = [1,2,3,4]. The next greater element is 3.
- 4 is underlined in nums2 = [1,2,3,4]. There is no next greater element, so 
the answer is -1.
 

 
 Constraints: 

 
 1 <= nums1.length <= nums2.length <= 1000 
 0 <= nums1[i], nums2[i] <= 10⁴ 
 All integers in nums1 and nums2 are unique. 
 All the integers of nums1 also appear in nums2. 
 

 
Follow up: Could you find an 
O(nums1.length + nums2.length) solution?

 Related Topics 栈 数组 哈希表 单调栈 👍 821 👎 0

"""

from typing import *

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    """ 基于题739 """
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = [-1] * len(nums1)
        idx = self.dailyTemperatures(nums2)
        n1_map = {n: i for i, n in enumerate(nums1)}
        for i, n2 in enumerate(nums2):
            if n2 in n1_map and idx[i] >= 0:
                result[n1_map[n2]] = nums2[idx[i]]
        return result

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [0]  # 升序栈
        result = [-1] * len(temperatures)
        for i in range(1, len(temperatures)):
            temp, s = temperatures[i], temperatures[stack[-1]]
            # 若当前温度小于等于之前温度, 则继续往后面找
            if temp <= s:
                stack.append(i)
            elif temp > s:
                # 把以前温度比当前温度小的值pop出去
                while len(stack) > 0 and temp > temperatures[stack[-1]]:
                    idx_in = stack.pop()
                    result[idx_in] = i
                stack.append(i)
        return result

class Solution:
    """ 单调栈 """
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1_map = {n: i for i, n in enumerate(nums1)}
        stack = [0]  # 升序栈
        result = [-1] * len(nums1)
        for i in range(1, len(nums2)):
            n2, s = nums2[i], nums2[stack[-1]]
            # 若当前值小于等于之前温度, 则继续往后面找
            if n2 <= s:
                stack.append(i)
            elif n2 > s:
                # 把以前温度比当前温度小的值pop出去
                while len(stack) > 0 and n2 > nums2[stack[-1]]:
                    idx_in = stack.pop()
                    # 找到pop出去的元素(搜索基准值)在nums1中的位置, 在result对应位置中保存n2(搜索结果值)
                    n2_in = nums2[idx_in]
                    if n2_in in n1_map:
                        result[n1_map[n2_in]] = n2
                stack.append(i)
        return result
# leetcode submit region end(Prohibit modification and deletion)
 

from RunLeetCodeInPycharm import StartTest

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
