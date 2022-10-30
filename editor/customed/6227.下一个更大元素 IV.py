
question_content = """

(6227)下一个更大元素 IV:
    https://leetcode.cn/problems/next-greater-element-iv/


输入：nums =[11,13,15,12,0,15,12,11,9]
# 输出：[15,15,-1,-1,-1,-1,-1,-1,-1]
输出：[15,15,-1,-1,12,-1,-1,-1,-1]


输入：nums = [2,4,0,9,6]
输出：[9,6,6,-1,-1]
解释：
下标为 0 处：2 的右边，4 是大于 2 的第一个整数，9 是第二个大于 2 的整数。
下标为 1 处：4 的右边，9 是大于 4 的第一个整数，6 是第二个大于 4 的整数。
下标为 2 处：0 的右边，9 是大于 0 的第一个整数，6 是第二个大于 0 的整数。
下标为 3 处：右边不存在大于 9 的整数，所以第二大整数为 -1 。
下标为 4 处：右边不存在大于 6 的整数，所以第二大整数为 -1 。
所以我们返回 [9,6,6,-1,-1] 。
示例 2：

输入：nums = [3,3]
输出：[-1,-1]
解释：
由于每个数右边都没有更大的数，所以我们返回 [-1,-1] 。



"""

from typing import *
from PythonLeetcodeRunner import *

# @lc code=start
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def secondGreaterElement(self, nums: List[int]) -> List[int]:
        import heapq
        st = []
        st2 = []
        heap = []
        ans = [-1] * len(nums)
        large = [-1] * len(nums)
        for i, n in enumerate(nums):
            if n == 12:
                print(i)
                pass
            while heap and nums[i] > heap[0][0]:
                n_pre, llarg_idx = heapq.heappop(heap)
                # llarg_idx = st2.pop()
                # ans[llarg_idx] = idx
                ans[llarg_idx] = nums[i]

            while st and n > nums[st[-1]]:
                idx = st.pop()
                large[idx] = i

                # while st2 and nums[idx] > nums[st2[-1]]:
                #     llarg_idx = st2.pop()
                #     # ans[llarg_idx] = idx
                #     ans[llarg_idx] = nums[idx]
                # st2.append(idx, )
                heapq.heappush(heap, (nums[idx], idx))
            st.append(i)
        # print(st)
        # print(large)

        # ans = []
        # for i, lar in enumerate(large):
        #     if lar > 0 and large[lar] > 0:
        #         ans.append(large[lar])
        #     else:
        #         ans.append(-1)
        return ans


# leetcode submit region end(Prohibit modification and deletion)
# @lc code=end

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
