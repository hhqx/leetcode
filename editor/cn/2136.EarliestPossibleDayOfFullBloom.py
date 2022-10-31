
question_content = """
You have n flower seeds. Every seed must be planted first before it can begin 
to grow, then bloom. Planting a seed takes time and so does the growth of a seed. 
You are given two 0-indexed integer arrays plantTime and growTime, of length n 
each: 

 
 plantTime[i] is the number of full days it takes you to plant the iᵗʰ seed. 
Every day, you can work on planting exactly one seed. You do not have to work on 
planting the same seed on consecutive days, but the planting of a seed is not 
complete until you have worked plantTime[i] days on planting it in total. 
 growTime[i] is the number of full days it takes the iᵗʰ seed to grow after 
being completely planted. After the last day of its growth, the flower blooms and 
stays bloomed forever. 
 

 From the beginning of day 0, you can plant the seeds in any order. 

 Return the earliest possible day where all seeds are blooming. 

 
 Example 1: 
 
 
Input: plantTime = [1,4,3], growTime = [2,3,1]
Output: 9
Explanation: The grayed out pots represent planting days, colored pots 
represent growing days, and the flower represents the day it blooms.
One optimal way is:
On day 0, plant the 0ᵗʰ seed. The seed grows for 2 full days and blooms on day 3
.
On days 1, 2, 3, and 4, plant the 1ˢᵗ seed. The seed grows for 3 full days and 
blooms on day 8.
On days 5, 6, and 7, plant the 2ⁿᵈ seed. The seed grows for 1 full day and 
blooms on day 9.
Thus, on day 9, all the seeds are blooming.
 

 Example 2: 
 
 
Input: plantTime = [1,2,3,2], growTime = [2,1,2,1]
Output: 9
Explanation: The grayed out pots represent planting days, colored pots 
represent growing days, and the flower represents the day it blooms.
One optimal way is:
On day 1, plant the 0ᵗʰ seed. The seed grows for 2 full days and blooms on day 4
.
On days 0 and 3, plant the 1ˢᵗ seed. The seed grows for 1 full day and blooms 
on day 5.
On days 2, 4, and 5, plant the 2ⁿᵈ seed. The seed grows for 2 full days and 
blooms on day 8.
On days 6 and 7, plant the 3ʳᵈ seed. The seed grows for 1 full day and blooms 
on day 9.
Thus, on day 9, all the seeds are blooming.
 

 Example 3: 

 
Input: plantTime = [1], growTime = [1]
Output: 2
Explanation: On day 0, plant the 0ᵗʰ seed. The seed grows for 1 full day and 
blooms on day 2.
Thus, on day 2, all the seeds are blooming.
 

 
 Constraints: 

 
 n == plantTime.length == growTime.length 
 1 <= n <= 10⁵ 
 1 <= plantTime[i], growTime[i] <= 10⁴ 
 

 Related Topics 贪心 数组 排序 👍 31 👎 0

"""

from typing import *
from PythonLeetcodeRunner import *

# @lc code=start
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        """
        ## 算法思路: 贪心策略
        经过分析后得知:
            1, 非连续种同一种不是最优解, 或者说连续种同一种的最终结果一定小于等于非连续的.
            2. 最优解中, growTime[i]越大越应先种, 可以用反证法证明.
        """

        accmu = 0
        ans = 0
        for p, g in sorted(zip(plantTime, growTime), key=lambda x: -x[1]):
            accmu += p
            ans = max(ans, accmu + g)
        return ans

    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        """
            根据key排序的另一种写法: cmp_to_key()
        """
        def fn(i, j):
            if growTime[i] > growTime[j]:
                return -1
            elif growTime[i] == growTime[j]:
                return 0
            else:
                return 1

        # from functools import cmp_to_key
        # idx = sorted(range(len(plantTime)), key=cmp_to_key(fn))
        idx = sorted(range(len(plantTime)), key=lambda x: -growTime.__getitem__(x))

        accmu = 0
        ans = 0
        for i in idx:
            accmu += plantTime[i]
            ans = max(ans, accmu + growTime[i])
        return ans


# leetcode submit region end(Prohibit modification and deletion)
# @lc code=end

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
