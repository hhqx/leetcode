
question_content = """
你打算做甜点，现在需要购买配料。目前共有 n 种冰激凌基料和 m 种配料可供选购。而制作甜点需要遵循以下几条规则： 

 
 必须选择 一种 冰激凌基料。 
 可以添加 一种或多种 配料，也可以不添加任何配料。 
 每种类型的配料 最多两份 。 
 

 给你以下三个输入： 

 
 baseCosts ，一个长度为 n 的整数数组，其中每个 baseCosts[i] 表示第 i 种冰激凌基料的价格。 
 toppingCosts，一个长度为 m 的整数数组，其中每个 toppingCosts[i] 表示 一份 第 i 种冰激凌配料的价格。 
 target ，一个整数，表示你制作甜点的目标价格。 
 

 你希望自己做的甜点总成本尽可能接近目标价格 target 。 

 返回最接近 target 的甜点成本。如果有多种方案，返回 成本相对较低 的一种。 

 

 示例 1： 
 
输入：baseCosts = [10], toppingCosts = [1], target = 1
输出：10
解释：注意，你可以选择不添加任何配料，但你必须选择一种基料。 

 
 
# 输入：baseCosts = [1,7], toppingCosts = [3,4], target = 10
# 输出：10
解释：考虑下面的方案组合（所有下标均从 0 开始）：
- 选择 1 号基料：成本 7
- 选择 1 份 0 号配料：成本 1 x 3 = 3
- 选择 0 份 1 号配料：成本 0 x 4 = 0
总成本：7 + 3 + 0 = 10 。
 

 示例 2： 

 
输入：baseCosts = [2,3], toppingCosts = [4,5,100], target = 18
输出：17
解释：考虑下面的方案组合（所有下标均从 0 开始）：
- 选择 1 号基料：成本 3
- 选择 1 份 0 号配料：成本 1 x 4 = 4
- 选择 2 份 1 号配料：成本 2 x 5 = 10
- 选择 0 份 2 号配料：成本 0 x 100 = 0
总成本：3 + 4 + 10 + 0 = 17 。不存在总成本为 18 的甜点制作方案。
 

 示例 3： 

 
输入：baseCosts = [3,10], toppingCosts = [2,5], target = 9
输出：8
解释：可以制作总成本为 8 和 10 的甜点。返回 8 ，因为这是成本更低的方案。
 

 示例 4： 



 提示： 

 
 n == baseCosts.length 
 m == toppingCosts.length 
 1 <= n, m <= 10 
 1 <= baseCosts[i], toppingCosts[i] <= 10⁴ 
 1 <= target <= 10⁴ 
 

 Related Topics 数组 动态规划 回溯 👍 124 👎 0

"""

from typing import *
from PythonLeetcodeRunner import *

# @lc code=start
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        """ 理解错题目意思了, 我真是orz,
        我这里尝试写, 在a,b数组中各取x,y个, 且y<= x//2
        实际题目要求: 在a中选1一个, 在b中选y个, 0<=y<=2*lenb, 且b每种不超过2个
        """
        m, n = len(baseCosts), len(toppingCosts)
        tar = target
        maxd = target

        # dp求出不同长度的baseCost的可能值
        dp = [0 for _ in range(maxd + 1)]
        dp[0] = 0b001

        for i in range(maxd+1):
            for d in range(maxd, 1 - 1, -1):
                if d < i + 1: continue
                for num in baseCosts:
                    # for k in range(tar // num):
                    dp[d] |= dp[d - 1] << num

            # if (dp[d] >> target) & 1:
            #     return target

        dp1 = dp

        # dp求出不同长度的toppingCosts的可能值
        dp = [0 for _ in range(maxd + 1)]
        dp[0] = 0b001 << maxd
        for i in range(maxd+1):
            for d in range(maxd, 1 - 1, -1):
                if d < i + 1: continue
                for num in toppingCosts:
                    dp[d] |= dp[d - 1] >> num

        # 对dp2进行前缀累加 位或操作
        dp2 = dp
        tmp = dp2[0]
        for d in range(1, len(dp2)):
            dp2[d] |= dp2[d - 1]

        val1, val2 = [], []
        for i in range(len(dp1)):
            state = dp1[i]
            # tmp = []
            tmp = [j for j in range(maxd+1) if (state >> j) & 1]
            val1.append(tmp)
            tmp = [target-j for j in range(maxd+1) if (state >> j) & 1]
            val2.append(tmp)

        # 查找最接近target的
        # mtol: max total
        # tar - p, tar, tar + q
        p, q = tar, tar
        for x in range(len(dp1)):
            # sa: state a, sb: state b
            # target, ... 1, 0
            sa = dp1[x]
            # 0, 1, 2 .. target
            sb = dp2[x // 2]

            delta = min(p, q)
            if delta == 0:
                return tar
            for k in range(0, delta + 1):
                if (sb >> k) & sa:
                    p = min(p, k)
                    break
                if (sa >> k) & sb:
                    q = min(q, k)
                    break
        if p <= q:
            return tar - p
        else:
            return tar + q

class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        """
        题目要求: 在 a 中选 1 个, 在 b 中选 y 个, 0 <= y <= 2 * lenb, 且 b 每种不超过 2 个
        """
        m, n = len(baseCosts), len(toppingCosts)
        tar = target

        # 求出 sa 中所有可能的值, (0, 2*tar] 范围内, 0不可取
        sa = 0
        for i in range(m):
            if 2*tar - baseCosts[i] < 0:
                continue
            if baseCosts[i] == tar:
                return tar
            # 施加一个关于 nbit=tar 对称的偏移
            sa |= 1 << (2*tar - baseCosts[i])

        # dp求出不同长度的 toppingCosts 的可能值
        sb = 0b001
        for i, num in enumerate(toppingCosts + toppingCosts):
            sb |= sb << num
            if (sa >> tar) & sb:
                return tar

        # valb = [j for j in range(2*tar + 1) if (sb >> j) & 1]
        # vala = [2 * tar - j for j in range(2*tar + 1) if (sa >> j) & 1]

        # target, ... 1, 0
        # sa: 0, 1, 2 ... 2*tar
        # sb: 2*tar, ... 1, 0
        # (sa >> x) & sb 标识了是否存在和为 2*tar-x 的值
        for delta in range(0, tar+1):
            if (sa >> (tar + delta)) & sb:
                return tar - delta
            if (sa >> (tar - delta)) & sb:
                return tar + delta

        return min(baseCosts)

class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        """
        题目要求: 在 a 中选 1 个, 在 b 中选 y 个, 0 <= y <= 2 * lenb, 且 b 每种不超过 2 个
        优化一下,
        """
        # GCD = target
        # for item in baseCosts + toppingCosts:
        #     GCD = gcd(GCD, item)

        # GCD = reduce(gcd, baseCosts + toppingCosts + [target])
        # if GCD != 1:
        #     return GCD*self.closestCost([num//GCD for num in baseCosts], [num//GCD for num in toppingCosts], target//GCD)
        # print(GCD)
        amin = min(baseCosts + [target])
        if amin != 0:
            return amin + self.closestCost([num - amin for num in baseCosts], toppingCosts, target - amin)

        m, n = len(baseCosts), len(toppingCosts)
        tar = target
        # totalb = sum(toppingCosts)

        # 求出 sa 中所有可能的值, (0, 2*tar] 范围内, 0不可取
        sa = 0
        for i in range(m):
            if 2*tar - baseCosts[i] < 0:
                continue
            if baseCosts[i] == tar:
                return tar
            # 施加一个关于 nbit=tar 对称的偏移
            sa |= 1 << (2*tar - baseCosts[i])

        # dp求出不同长度的 toppingCosts 的可能值
        sb = 0b001
        for i, num in enumerate(toppingCosts + toppingCosts):
            sb |= sb << num
            if (sa >> tar) & sb:
                return tar

        # target, ... 1, 0
        # sa: 0, 1, 2 ... 2*tar
        # sb: 2*tar, ... 1, 0
        # (sa >> x) & sb 标识了是否存在和为 2*tar-x 的值
        for delta in range(0, tar+1):
            if (sa >> (tar + delta)) & sb:
                return tar - delta
            if (sa >> (tar - delta)) & sb:
                return tar + delta

        return min(baseCosts)

class Solution1:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        """
        题目要求: 在 a 中选 1 个, 在 b 中选 y 个, 0 <= y <= 2 * lenb, 且 b 每种不超过 2 个
        优化一下, 貌似更慢了
        """
        amin = min(baseCosts + [target])
        if amin != 0:
            return amin + self.closestCost([num - amin for num in baseCosts], toppingCosts, target - amin)

        m, n = len(baseCosts), len(toppingCosts)
        tar = target
        # totalb = sum(toppingCosts)

        # 求出 sa 中所有可能的值, (0, 2*tar] 范围内, 0不可取
        sa = 0
        for i in range(m):
            if 2*tar - baseCosts[i] < 0:
                continue
            if baseCosts[i] == tar:
                return tar
            # 施加一个关于 nbit=tar 对称的偏移
            sa |= 1 << (2*tar - baseCosts[i])

        # dp求出不同长度的 toppingCosts 的可能值
        sb = sa
        for i, num in enumerate(toppingCosts + toppingCosts):
            sb |= sb >> num
            if sb & (1 << tar):
                return tar

        # target, ... 1, 0
        # sa: 0, 1, 2 ... 2*tar
        # sb: 2*tar, ... 1, 0
        # (sa >> x) & sb 标识了是否存在和为 2*tar-x 的值
        for delta in range(0, tar+1):
            if sb & (1 << (tar + delta)):
                return tar - delta
            if sb & (1 << (tar - delta)):
                return tar + delta

        return min(baseCosts)
# leetcode submit region end(Prohibit modification and deletion)
# @lc code=end

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
