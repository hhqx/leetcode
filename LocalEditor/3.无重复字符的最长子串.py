# @before-stub-for-debug-begin
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#
# https://leetcode.cn/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (39.01%)
# Likes:    8163
# Dislikes: 0
# Total Accepted:    2M
# Total Submissions: 5.1M
# Testcase Example:  '"abcabcbb"'
#

question_content="""给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。



示例 1:


输入: s = "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。


示例 2:


输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。


示例 3:


输入: s = "aab"
输出: 2


输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。




提示：


0 <= s.length <= 5 * 10^4
s 由英文字母、数字、符号和空格组成


"""

from collections import defaultdict
from typing import *
from PythonLeetcodeRunner import *

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """ 双指针 """
        d = defaultdict(int)  # 记录子串字符词频
        left, right = 0, 0
        Max = 0
        while right < len(s):

            # 右指针移动至出现重复字符的后一位
            # 退出循环时s[left:right-1]无重复字符
            while right < len(s):
                c = s[right]
                right += 1
                d[c] += 1
                if d[c] == 2:
                    break
            
            # 更新最大非重复子串长度, 此时left和right之间仅重复了right前1位
            Max = max(Max, right - 1 - left)
            # 如果直至字符串结束right所指字符都位重复, 则s[left:right]无重复字符
            if right == len(s) and d[s[len(s) - 1]] == 1:
                Max = max(Max, right - left)

            # 左指针向右移动至重复字符的后一位, 退出循环时s[left:right]无重复字符
            while left < right:
                c = s[left]
                left += 1
                d[c] -= 1
                if d[c] == 1:
                    break
                
        return Max

class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        start = maxLength = 0
        usedChar = {}
        
        for i in range(len(s)):
            if s[i] in usedChar and start <= usedChar[s[i]]:
                start = usedChar[s[i]] + 1
            else:
                maxLength = max(maxLength, i - start + 1)

            usedChar[s[i]] = i

        return maxLength
# @lc code=end


if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()

