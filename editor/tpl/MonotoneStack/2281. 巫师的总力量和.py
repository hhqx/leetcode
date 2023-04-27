
question_content = """
作为国王的统治者，你有一支巫师军队听你指挥。 

 给你一个下标从 0 开始的整数数组 strength ，其中 strength[i] 表示第 i 位巫师的力量值。对于连续的一组巫师（也就是这些巫师的力量值是
 strength 的 子数组），总力量 定义为以下两个值的 乘积 ： 

 
 巫师中 最弱 的能力值。 
 组中所有巫师的个人力量值 之和 。 
 

 请你返回 所有 巫师组的 总 力量之和。由于答案可能很大，请将答案对 10⁹ + 7 取余 后返回。 

 子数组 是一个数组里 非空 连续子序列。 

 

 示例 1： 

 输入：strength = [1,3,1,2]
输出：44
解释：以下是所有连续巫师组：
- [1,3,1,2] 中 [1] ，总力量值为 min([1]) * sum([1]) = 1 * 1 = 1
- [1,3,1,2] 中 [3] ，总力量值为 min([3]) * sum([3]) = 3 * 3 = 9
- [1,3,1,2] 中 [1] ，总力量值为 min([1]) * sum([1]) = 1 * 1 = 1
- [1,3,1,2] 中 [2] ，总力量值为 min([2]) * sum([2]) = 2 * 2 = 4
- [1,3,1,2] 中 [1,3] ，总力量值为 min([1,3]) * sum([1,3]) = 1 * 4 = 4
- [1,3,1,2] 中 [3,1] ，总力量值为 min([3,1]) * sum([3,1]) = 1 * 4 = 4
- [1,3,1,2] 中 [1,2] ，总力量值为 min([1,2]) * sum([1,2]) = 1 * 3 = 3
- [1,3,1,2] 中 [1,3,1] ，总力量值为 min([1,3,1]) * sum([1,3,1]) = 1 * 5 = 5
- [1,3,1,2] 中 [3,1,2] ，总力量值为 min([3,1,2]) * sum([3,1,2]) = 1 * 6 = 6
- [1,3,1,2] 中 [1,3,1,2] ，总力量值为 min([1,3,1,2]) * sum([1,3,1,2]) = 1 * 7 = 7
所有力量值之和为 1 + 9 + 1 + 4 + 4 + 4 + 3 + 5 + 6 + 7 = 44 。
 

 示例 2： 

 输入：strength = [5,4,6]
输出：213
解释：以下是所有连续巫师组：
- [5,4,6] 中 [5] ，总力量值为 min([5]) * sum([5]) = 5 * 5 = 25
- [5,4,6] 中 [4] ，总力量值为 min([4]) * sum([4]) = 4 * 4 = 16
- [5,4,6] 中 [6] ，总力量值为 min([6]) * sum([6]) = 6 * 6 = 36
- [5,4,6] 中 [5,4] ，总力量值为 min([5,4]) * sum([5,4]) = 4 * 9 = 36
- [5,4,6] 中 [4,6] ，总力量值为 min([4,6]) * sum([4,6]) = 4 * 10 = 40
- [5,4,6] 中 [5,4,6] ，总力量值为 min([5,4,6]) * sum([5,4,6]) = 4 * 15 = 60
所有力量值之和为 25 + 16 + 36 + 36 + 40 + 60 = 213 。
 

 

 提示： 

 
 1 <= strength.length <= 10⁵ 
 1 <= strength[i] <= 10⁹ 
 

 Related Topics 栈 数组 前缀和 单调栈 👍 79 👎 0

"""

from typing import *
from PythonLeetcodeRunner import *

# @lc code=start
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def totalStrength(self, strength: List[int]) -> int:
        """
        单调栈枚举每个最值nums[i]的左右边界L,R,  s.t. min(s[left:right+1]) = nums[i]
            其中: left属于(L, i], right属于[i, R)

        对于每个最值为nums[i]的子区间:  ans_i = sum{ nums[i] * sum(s[left:right+1]) },
            其中, left属于(L, i], right属于[i, R)


        定义前缀和: p[y]-p[x] = sum(s[x:y+1]), len(p) = len(s)+1
        定义前缀和的前缀和: pp[y]-pp[x] = sum(p[x:y+1]), len(pp) = len(p)+1

        化简(note: left属于(L, i], right属于[i, R)):
            ans_i   = sum{ nums[i] * sum(s[left:right+1]) }
                    = nums[i] * sum{ p(right+1) - p(left) }
                    = nums[i] * ( (i-L)*(pp[R+1]-pp[i+1]) - (R-i)*(pp[i+1]-pp[L+1]) )
        """
        mod = int(1e9 + 7)
        n = len(strength)
        nums = strength

        # 前缀和
        p = [0]
        for num in strength:
            p.append(p[-1] + num)

        # 前缀和的前缀和
        pp = [0]
        for num in p:
            pp.append(pp[-1] + num)

        ans = 0

        # 单调栈枚举最值nums[i]的边界
        st = []
        L = [-1] * n
        R = [n] * n
        for i in range(n):
            while st and nums[i] <= nums[st[-1]]:
                R[st[-1]] = i
                st.pop()
            L[i] = st[-1] if st else -1
            st.append(i)

        # 累计所有子区间
        for i in range(n):
            # ans += (i - L[i]) * (R[i] - i)
            # print(L[i], i, R[i])

            groupSum = (pp[R[i] + 1] - pp[i + 1]) * (i - L[i]) - \
                       (pp[i + 1] - pp[L[i] + 1]) * (R[i] - i)
            ans += (nums[i] * groupSum) % mod

        return ans % mod


# leetcode submit region end(Prohibit modification and deletion)
# @lc code=end

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
