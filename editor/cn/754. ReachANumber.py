
question_content = """
You are standing at position 0 on an infinite number line. There is a 
destination at position target. 

 You can make some number of moves numMoves so that: 

 
 On each move, you can either go left or right. 
 During the iᵗʰ move (starting from i == 1 to i == numMoves), you take i steps 
in the chosen direction. 
 

 Given the integer target, return the minimum number of moves required (i.e., 
the minimum numMoves) to reach the destination. 

 
 Example 1: 

 
Input: target = 2
Output: 3
Explanation:
On the 1ˢᵗ move, we step from 0 to 1 (1 step).
On the 2ⁿᵈ move, we step from 1 to -1 (2 steps).
On the 3ʳᵈ move, we step from -1 to 2 (3 steps).
 

 Example 2: 

 
Input: target = 3
Output: 2
Explanation:
On the 1ˢᵗ move, we step from 0 to 1 (1 step).
On the 2ⁿᵈ move, we step from 1 to 3 (2 steps).
 

 
 Constraints: 

 
 -10⁹ <= target <= 10⁹ 
 target != 0 
 

 Related Topics 数学 二分查找 👍 318 👎 0

"""

from typing import *
from PythonLeetcodeRunner import *

# @lc code=start
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def reachNumber(self, target: int) -> int:
        """
        完整说明见: https://leetcode.cn/problems/reach-a-number/solution/by-hhqx-l8xa/
        """

        target = abs(target)

        # 求出满足 sn >= target 的最小的整数 n0
        n0 = (-1 + sqrt(1 + 8 * target)) / 2
        n0 = ceil(n0)

        # 由于sn数列的性质, 三项之内必定包含奇数和偶数,
        # 因此sn - target三项之内必定有偶数
        for n in range(n0, n0 + 3):
            sn = n * (n + 1) / 2
            if (sn - target) % 2 == 0:
                return n

        return None
# leetcode submit region end(Prohibit modification and deletion)
# @lc code=end

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
