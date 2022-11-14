
question_content = """
给定你一个整数数组
 nums 

 我们要将
 nums 数组中的每个元素移动到 A 数组 或者 B 数组中，使得 A 数组和
 B 数组不为空，并且
 average(A) == average(B) 。 

 如果可以完成则返回true ， 否则返回 false 。 

 注意：对于数组
 arr , 
 average(arr) 是
 arr 的所有元素的和除以
 arr 长度。 

 

 示例 1: 

 
输入: nums = [5,3,11,19,2]
输出: true
 
输入: nums = [1,2,3,4,5,6,7,8]
输出: true
解释: 我们可以将数组分割为 [1,4,5,8] 和 [2,3,6,7], 他们的平均值都是4.5。
 

 示例 2: 

 
输入: nums = [3,1]
输出: false
 

 

 提示: 

 
 1 <= nums.length <= 30 
 0 <= nums[i] <= 10⁴ 
 

 Related Topics 位运算 数组 数学 动态规划 状态压缩 👍 213 👎 0

"""

from typing import *
from PythonLeetcodeRunner import *

# @lc code=start
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        """ 折半枚举, 时间复杂度: n*2^(n/2), 空间复杂度: 2^(n/2) """
        if len(nums) <= 1:
            return False
        n = len(nums)
        total = sum(nums)

        dcnt_tol = defaultdict(set)
        # 枚举前 2 ** (n/2), 记录所有的 (lcnt, ltol) 对
        nl = n // 2
        for i in range(1 << (nl)):
            cnt, tol = 0, 0
            for k in range(nl):
                if i >> k & 1:
                    tol += nums[k]
                    cnt += 1
            dcnt_tol[cnt].add(n * tol)

        # 枚举后一半数组的 (tol, cnt)
        # nl = n//2
        for i in range(1 << (n - nl)):
            cnt, tol = 0, 0
            for k in range(n - nl):
                if i >> k & 1:
                    tol += nums[nl + k]
                    cnt += 1
            rcnt, rtol = cnt, tol
            # if i == 0b001:
            #     print(i)

            # 枚举查找是否存在: (ltotal + rtotal) / (lcnt + rcnt) = total / n
            # 等价于: (ltotal + rtotal) * n = total * (lcnt + rcnt)
            #        ltotal * n = total * (lcnt + rcnt) - rtotal * n
            for lcnt in dcnt_tol:
                if total * (lcnt + rcnt) - rtol * n in dcnt_tol[lcnt]:
                    if (lcnt + rcnt) in {0, n}:  # 所选元素不可全选, 不可不选
                        # print(cnt, cnt1)
                        pass
                    else:
                        return True

        return False
# leetcode submit region end(Prohibit modification and deletion)
# @lc code=end

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
