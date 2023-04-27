question_content = """
有效 IP 地址 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 0），整数之间用 '.' 分隔。 

 
 例如："0.1.2.201" 和 "192.168.1.1" 是 有效 IP 地址，但是 "0.011.255.245"、"192.168.1.312" 和 
"192.168@1.1" 是 无效 IP 地址。 
 

 给定一个只包含数字的字符串 s ，用以表示一个 IP 地址，返回所有可能的有效 IP 地址，这些地址可以通过在 s 中插入 '.' 来形成。你 不能 重新排序
或删除 s 中的任何数字。你可以按 任何 顺序返回答案。 

 

 示例 1： 

 
输入：s = "25525511135"
输出：["255.255.11.135","255.255.111.35"]
 

 示例 2： 

 
输入：s = "0000"
输出：["0.0.0.0"]
 

 示例 3： 

 
输入：s = "101023"
输出：["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
 

 

 提示： 

 
 1 <= s.length <= 20 
 s 仅由数字组成 
 

 Related Topics 字符串 回溯 👍 1209 👎 0

"""

from typing import *
from PythonLeetcodeRunner import *

# @lc code=start
# leetcode submit region begin(Prohibit modification and deletion)
from itertools import combinations


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        choice = range(1, n)
        ans = []
        for seps in combinations(choice, 3):
            # print(seps)
            bound = [0] + list(seps) + [n]
            ip = []
            # hasPos = False
            for i in range(len(bound) - 1):
                l, r = bound[i], bound[i + 1]
                val = int(s[l:r])
                if s[l:r] != str(val) or val > 255:
                    break
                # if val == 0 and hasPos is False or val > 255:
                #     break
                # hasPos = val > 0
                ip.append(s[l:r])
            else:
                ans.append(".".join(ip))

        return ans


# leetcode submit region end(Prohibit modification and deletion)
# @lc code=end

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
