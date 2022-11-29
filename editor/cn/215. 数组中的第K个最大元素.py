
question_content = """
给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。 

 请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。 

 你必须设计并实现时间复杂度为 O(n) 的算法解决此问题。 

 

 示例 1: 

 
输入: [3,2,1,5,6,4], k = 2
输出: 5
 

 示例 2: 

 
输入: [3,2,3,1,2,4,5,5,6], k = 4
输出: 4 

 

 提示： 

 
 1 <= k <= nums.length <= 10⁵ 
 -10⁴ <= nums[i] <= 10⁴ 
 

 Related Topics 数组 分治 快速选择 排序 堆（优先队列） 👍 1974 👎 0

"""

from typing import *
from PythonLeetcodeRunner import *

# @lc code=start
# leetcode submit region begin(Prohibit modification and deletion)
def bisect_right(arr, tar, key=lambda x: x):
    left, right = 0, len(arr)
    while right > left:
        mid = left + right >> 1
        if key(arr[mid]) <= tar:
            left = mid + 1
        else:
            right = mid
    return right

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """ 树状数组统计 特定值域内的元素个数 + 二分枚举值域,
        二分的思想和之前的一致,

        """
        # LOWER, UPPER = min(nums), max(nums)+1
        LOWER, UPPER = int(-1e4), int(1e4) + 1

        class BIT:
            def __init__(self, LOWER, UPPER):
                self.M = LOWER
                self.N = UPPER
                # 需要存下 N-M 个数, 外加 tree[0] 闲置, 所以长度为 N-M+1
                self.tree = [0] * (UPPER - LOWER + 1)

            @staticmethod
            def lowbit(x: int):
                return x & -x

            def add(self, x: int):
                # idx到1的距离等于x到M的距离, 因为本质上是, [1, idx] 映射到 [M, x]
                idx = x - self.M + 1
                while idx < len(self.tree):
                    self.tree[idx] += 1
                    idx += self.lowbit(idx)
                    # print(idx)

            def query(self, x: int):
                # idx到1的距离等于x到M的距离, 因为本质上是, [1, idx] 映射到 [M, x]
                idx = x - self.M + 1
                ans = 0
                while idx > 0:
                    ans += self.tree[idx]
                    idx -= self.lowbit(idx)
                return ans

        # 树状数组初始化
        bitArray = BIT(LOWER, UPPER)
        for num in nums:
            bitArray.add(num)

        def CountLargeThan(x):
            """ 统计大于x的元素个数 """
            # (0, UPPER-1] - (0, x] = [x, UPPER]
            ret = bitArray.query(UPPER - 1) - bitArray.query(x - 1)
            return ret

        # def CountLargeThan(x):
        #     """ 统计大于x的元素个数 """
        #     cnt = sum(ni >= x for ni in nums)
        #     return cnt

        # # True -> False, Find the last True
        # KthLargest = bisect.bisect_right(range(LOWER, UPPER), True, key=lambda x: CountLargeThan(x) >= k) + LOWER - 1

        # False -> True, Find the last False
        KthLargest = bisect_right(range(LOWER, UPPER), False, key=lambda x: CountLargeThan(x) < k) + LOWER - 1

        return KthLargest

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """ 仿照快排 """
        n = len(nums)

        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]

        def partion(l, r):
            import random
            p = random.randint(l, r - 1)
            swap(p, r - 1)
            # left 指向小于pivot的最后一个位置, [l, left) 里全是小于pivot的
            left = l
            for i in range(l, r):
                if nums[i] < nums[r - 1]:
                    swap(left, i)
                    left += 1
            swap(left, r - 1)
            return left

        # 二分查找第k大个数
        left, right = 0, n
        while right > left:
            mid = partion(left, right)
            if mid < n - k:
                left = mid + 1
            else:
                right = mid

        return nums[right]
# leetcode submit region end(Prohibit modification and deletion)
# @lc code=end

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
