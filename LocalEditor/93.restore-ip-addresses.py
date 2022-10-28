#
# @lc app=leetcode.cn id=93 lang=python3
#
# [93] Restore IP Addresses
#
# https://leetcode.cn/problems/restore-ip-addresses/description/
#
# algorithms
# Medium (57.17%)
# Likes:    1021
# Dislikes: 0
# Total Accepted:    270.3K
# Total Submissions: 472.7K
# Testcase Example:  '"25525511135"'
#

question_content="""A valid IP address consists of exactly four integers separated by single
dots. Each integer is between 0 and 255 (inclusive) and cannot have leading
zeros.


For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but
"0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP
addresses.


Given a string s containing only digits, return all possible valid IP
addresses that can be formed by inserting dots into s. You are not allowed to
reorder or remove any digits in s. You may return the valid IP addresses in
any order.


Example 1:


Input: s = "25525511135"
Output: ["255.255.11.135","255.255.111.35"]


Example 2:


Input: s = "0000"
Output: ["0.0.0.0"]


Example 3:


Input: s = "101023"
Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]



Constraints:


1 <= s.length <= 20
s consists of digits only.


"""

from typing import *
from PythonLeetcodeRunner import *

# @lc code=start
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:

        def isValid(s):
            # status = (0 < int(s) <= 255 and s[0] != '0') or s == '0'
            # if status:
            #     print(f'{s}: {(s)}')
            # return status
            return (0 < int(s) <= 255 and s[0] != '0') or s == '0'       
        
        result = []
        path = []
        def backtracking(s, startIndex):
            
            
            if len(path) == 4 or startIndex == len(s):
                if startIndex == len(s) and len(path) == 4:
                    # path.append(s[startIndex:])
                    result.append('.'.join(path[:]))
                return
            
            for i in range(startIndex, len(s)):
                if not isValid(s[startIndex:i+1]):
                    continue
                path.append(s[startIndex:i+1])
                backtracking(s, i+1)
                path.pop()

        backtracking(s, 0)
        return result
# @lc code=end


if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()

