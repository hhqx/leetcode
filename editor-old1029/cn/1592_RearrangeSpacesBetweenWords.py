
question_content = """
You are given a string text of words that are placed among some number of 
spaces. Each word consists of one or more lowercase English letters and are separated 
by at least one space. It's guaranteed that text contains at least one word. 

 Rearrange the spaces so that there is an equal number of spaces between every 
pair of adjacent words and that number is maximized. If you cannot redistribute 
all the spaces equally, place the extra spaces at the end, meaning the returned 
string should be the same length as text. 

 Return the string after rearranging the spaces. 

 
 Example 1: 

 
Input: text = "  this   is  a sentence "
Output: "this   is   a   sentence"
Explanation: There are a total of 9 spaces and 4 words. We can evenly divide 
the 9 spaces between the words: 9 / (4-1) = 3 spaces.
 

 Example 2: 

 
Input: text = " practice   makes   perfect"
Output: "practice   makes   perfect "
Explanation: There are a total of 7 spaces and 3 words. 7 / (3-1) = 3 spaces 
plus 1 extra space. We place this extra space at the end of the string.
 

 
 Constraints: 

 
 1 <= text.length <= 100 
 text consists of lowercase English letters and ' '. 
 text contains at least one word. 
 

 Related Topics 字符串 👍 47 👎 0

"""

from typing import *

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def reorderSpaces(self, text: str) -> str:

        last_c = '.'
        words = []
        cnt = 0
        for i, c in enumerate(text):
            if 'a' <= c <= 'z':
                if not ('a' <= last_c <= 'z'):
                    words.append('')
                words[-1] += c
                cnt += 1
            last_c = c

        # 计算空格间隔大小, 和尾部空格个数
        space_delta = (len(text) - cnt) // (len(words) - 1)
        space_end = (len(text) - cnt) // (len(words) - 1)

        # 生成结果
        # ans = (' ' * space_delta).join(words) + (' ' * space_end)
        ans = ''
        for w in words[:-1]:
            ans += w
            ans += ' ' * space_delta
        ans += words[-1]
        ans += ' ' * space_end

        return ans

# leetcode submit region end(Prohibit modification and deletion)
 

from RunLeetCodeInPycharm import StartTest

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
