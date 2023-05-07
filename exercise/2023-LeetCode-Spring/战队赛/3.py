question_content = """
3. 提取咒文
通过的用户数34
尝试过的用户数158
用户总通过次数34
用户总提交次数204
题目难度Medium
随着兽群逐渐远去，一座大升降机缓缓的从地下升到了远征队面前。借由这台升降机，他们将能够到达地底的永恒至森。
在升降机的操作台上，是一个由魔法符号组成的矩阵，为了便于辨识，我们用小写字母来表示。 matrix[i][j] 表示矩阵第 i 行 j 列的字母。该矩阵上有一个提取装置，可以对所在位置的字母提取。
提取装置初始位于矩阵的左上角 [0,0]，可以通过每次操作移动到上、下、左、右相邻的 1 格位置中。提取装置每次移动或每次提取均记为一次操作。

远征队需要按照顺序，从矩阵中逐一取出字母以组成 mantra，才能够成功的启动升降机。请返回他们 最少 需要消耗的操作次数。如果无法完成提取，返回 -1。

注意：

提取装置可对同一位置的字母重复提取，每次提取一个
提取字母时，需按词语顺序依次提取
示例 1：

输入：matrix = ["sd","ep"], mantra = "speed"

输出：10

解释：如下图所示
矩阵 (2).gif

示例 2：

输入：matrix = ["abc","daf","geg"], mantra = "sad"

输出：-1


输入：
["aabcbcbbcbabaabbaaccaabccbbbbbacacccccabaacbbbacccccacaccbabcbcaaccbcbbbbcacccbac","bcbcaaacccacbbbaacbcacccbaccbccbbaaacaacbcaacabbbcacbccccaaacaacbbbaccaacacabccbc","aaaababcabcbbcaccacacccccaccbbbabbaaccccbacaaccbabcabbacaabcbccbccababcabbacaacaa","ababcaaabaacaccabaaaabacaabaabacababacaaabcbbbbbcbcccbbbaaacabaabcbaabcaabcbbcbcc","bbaabcaaacaababbacccccaacacbbbbabaabaacccaabbbbaaccbacabcbccaacabcbabbbbcabccbabb","bcaaaacacbcbccccabbbbabbcbaaacabcbcaaacaabcbaaabccaabcaacababacaccbabbbcccbcaaabc","baabcacababcabbcccaabbbcbcbaaaabbacbbaabcbabacbbbcbaaaacbaaabbcbbcccbaacbccbcbcbc","bbbabccccabaccbbccbacbabccbcbbbaabacbbacabacbabacaabbccccaccbbcccccaaacaabaacacca","caaababaacacbbcbbbcbbccbbbbcccacaccbabccaacbaaacbbcccbabcbcbaabbbcabacccaaaabacaa","bcacbaacbcacacccbccacaacccacbcaaaacbccaaccaaabcccbabbaababababbaaacbaabaaababccac","abbcbccbbbababbaaaabcabcccabbcbabaccaaaccbacbaaaacaccbabababbccbcaaaaabcaaaccbaac","bcbbbabcbccacbacabbbaabaaabcabccccbabbabbabcbbcabbabbabbaaacabaaaabbabacaaacaaaab","accbcbcbbccaaaaccbcbabbcccbbccbccaabcbcaabaacbcccbbbbaacaccacacaabacccccaabababca","abbacccbbbabaccbbbbccbaaaccabacbabbabcaabbaabbcabbbbaccacbaaccbcacbabbcbbcaccbbbc","bbccaabbacacabaaacbcbbbcacacaaaccaaabcbcaacccbbcccabcbbbabcacaaaaacccbbcacacaacbb","bcbcccaccaacaabcbcabcabcccacabaccbcbbcbaababcbcbbaacbaabaacabbcbccccbabbcbbcaccab","acbabcbaccacbcaaccacacaccbccabccbbababacabaacbbbaabacabbccacabababcbacacaaccabbbc","abcccccbcccbacccbabbbbacbabcbabaaabccabcbccccaabbcbaaacccbacbccacbbbbcacacbacaacb","aabbacabbbbcccababbbacaabccaaabcaabacccbbcbcbbaaacaaccaabacababcababbbbbbabbbacbc","bbbabcaacccaaaaccbabccabaaabaabcaacabbaaccabaccbabbbcbbcbbabcacbbbccacbabaccaacaa","baaabbbabcaabcbabcabacaabcbcbbbcbbccbcccababccabcbabbcbbbbcbcbbaaaabcccaacabbaaab","acbcaacbabcbcccccbcbacbbcbbcccbbbcbaacacbcaacccacbbcabacbcacabaaaccabbbcccbbcacaa","ccbbbcaacaacacacabbcbcacabbbbabaaabbaccaacacbabbabcccbcbbbbccabbaacacaaaccbaaaabc","cbacabccaaccabbcaabbcaacaccaaaccbbaabccacccbbccaccccbccbbabbbccbcacccccccabcbacab","bbabbbabaccbbbbbbcbcbcacaabccaccbcaaaacbaabaaacbcbbacaacabcabaabccaababcacabbbbba","ababbbabcbbaccbccaacaccacabccaabaabbbaccccbaababaccbccbcacababacaabcbaccbaacccabc","abbbcacccaaabbaaaacabbcbbbacbbcbbbabcbbcbbaacbacaccbabacccbaccccbaabcbcaaaaccabbb","aaccaaaabacbaccbacbacaacabbcbccbbabaaaacbcaabaabccacaabbcabbbbacbacacccbcacaaaccb","bccacacaaabbcbabaacbabbbcabbcaaababbbbaaabcbbaaaacbbcaaaaaacbbcbbacabacaaaabcabab","cbbaccccccacacccaabaacbbccbacabaabcaabbbccbcacccbcccaabaabcabacabcaaaacabaaabbcaa","abacabcaacabbcccccbbbcbccccbccacacbbbabbbaccaacaaabbcbbbbbcacacbcbbccbabbaccacbbc","caccbaaccbbbcabacbccacabacacabcaccacaccbbcbbabaaabbcbcbbbbcaabbccbabccbbabaccbccc","cbcbbabbaccaabccccbcaabccbacababccbcbccbacacbaacabacabaabcaccacbacabbcababaaccbbb","cbbbaabcccbbcbababbbbcbcbaccbbcccbcbbaabccbcbababaacaabbbccbccccccbacccccccacaacc","bcacaccabcacccccacacabacbbbcaaaabbccaaabaccaccbbcccaaabacaccccabcccaaabbaacababbc","abbbaaccbaacabacbabaacbbbaccbbcbbcaccabbcaabbaababccccabaaacacbcccbacbcbcccbcbbbc","bacacabcbaccbbbcccbbacabbbaaaabcabaccaaacccabccbbbbababcacbacacbbccbabcaababbbcbb","aacbabbbaaaabccccbbcaacbabaaabbcaccacbcccacbcbbbaacbbacabbaccbcbbbcbacaacacaacbcb","bbcbbaacaabababbababacbacccccbbcbaacbcbbaaacccaccaabccaaccaacaacccbabbcccbbbcaabb","bacaaacbbcabbccabacbbbbbbcabcbbaabbcaacccaaabababaccbbacabacacacabcbacbbacbbbcaaa","bbbbccccccbcccbbbaaacacaaccacbcbcabcbcccbabbaaccaabaabccabcbcaaabcbbaabaacacbaaca","cbbcbcaacaaccabccbbcabbbcbaaccabcbaaccbacbabbcbbbbaccbaccaaacbbbacacacbcaccbbacca","bcacabbcabcbacabcabbaacbcaaaccaabcabcacaacaaaacaaabababbcacbbaaaccacccbccbbacbcab","caacbbabbacaaaaacaccabaacabacbcabcaabbbaaabcababacbbacaacaabcbcbbabcabbbabaaccbbc","cbcbbbcbbaaacbcacacbbcbccbaaaacccabbacaacabcbbaaaaabaacbbcbcacacccbcabaccccaacacc","aabcccbccaccabacbaccbbcabacbbcabbacaabbccaabbacaaccccbbabcccbcbbccbababaabbbbccca","caacbbcbaabcababccbbccbbababcbabbabbabccbcbaccbaaccbabacbabbbbcaacacaacacbcbababb","bbcabbcbbaabccacbabcacbcabcbaaccaccaabcababacaccbbbcaacbabccabbbacaacbcaccbacbbba","abcccabcabccababbccbabaabbccabaccbbcacbacccbcabbaccacaabbbbabcbcacaabcaacbbcbbbac","cbbbabcabccaacbaabacabcabbcaaccccccabaccaaabaacbaacbbabaabacaaaaacbccaccabbacaaba","aaaabbbaccbcbcabacbabccaabcaacacccaccbbcbaabaccacaacacabcbbbbbcaabcccbabccccababb","aabaabbcaacbcbabacaacaaabaabaaccaacbcacaabbbcaaabcbbbbabcbacaaaabcaaccbcbababcccb","cccaccaabcabaacccaacccbbbbaacccbcccbaacbabccccabbababcbccaaccabaaaabbcabcabbccaac","cbbbaccbaccaababcbaabbbccccbbaaaacbbbccbaaacbccacaccabbabbcbccacabaacaccbcabccbaa","bccbbacaaaaaaacabbbaabbaabccbaaccbbacbcbcaaacaccaabccabbcbbabccbbaacbcaacbbcaccbb","cbbbbbbbcaabcccaccabcaacbaccbcaacbaaabbbbbbaaccccaaccbbaccbaabbbabccaaaabaaacacca","ccabcabbbcccbaacbcbccbbcaccaaacabbaaccaabbcabaacacbccabbbccaaaacbaaccbbbbaaacccca","cbaccccaccbccbaaccaacaccabcabccbcbacbcbaabcaabccaccacccabbcabaacbabccbbbabaccccaa","bcaabacbcaabbcbccbcbccaaccbaaababcbbcbacbcccacbcbcabbccbcaacbcacabbbbaaaccccbaaca","abcbabcbcabacccbccacabcaaabbccbabaccbcbbcccccbbccbbbccbcaabcaccaacbccbbaccbcbbbaa","babcaaabcbbacbaccccacaaacbccaabcabcbcbabcbaaccaabbbacacababbacaccaccabccccaabbbac","abaababbcabcbbccabbbababbccaaacacbacbaaaccabcbabbaabbababaaabccccccbbaaababbbbaba","baabacbaababaaaacbcbcabcbaccaaabccacbaaccbacababbacbccabbacbcacbcaaccbbbacccbabab","bcbbbbbacacabaabacccabaabbacbaacabbcbaaaccaaccabcccbaaabbacccaabacbacaacbcaacabca","abbbcaabaabbbbbbacaacaacbccacbacbcbbbcaccabbcabccbbbabcbcccaaaaccabacacccabcaccab","bccbccbaccbbbbbcccaccababaabcaabaabcacccbcabcccccbccccbbbacccabacabbacbbbbcbbbcba","babccbbcabaaabcaabcbcbabbccabccaabbcbcbaacccbcbacabcacbbaaaaaababaaccbcacaacccacc","cbcaaabcaabacbcbcacccbaabaaacabaaabbbbaccbbbcccabcaabcccaccbabccbccbaaaacacabbbbb","ccabcabbccbcbaabbccccbbccbbbaaccbcabbbaacbaacacccacacbabbcacacbcaabababcbaaaaabba","caacbcabaabcbabbabaacbcbccbbccaaabbccabaaccbccbbacbcabaabcbccaabccbbbcabaaccbbcab","accbbcabbbbbaacacbbcaaaabbcccaaccaaccacbcbcbcabaccbbbaccbaaabaabbbbbacaabcacbbcaa","cbccccaabbcbbacccabaaabcaabbbcabbbaabcabcbccabacaaabcbabbcccaabbacbacccbacbcaacba","bccbabcaacabbccbcbcacacacbaacbcaaccbcbbcaccabbcccaaaaabbaacbccbbacbbbcbbbaacaacbc","bccbbbabcaababcbcabcbcabbcaabcbcbacbaabcaccbcccbaccbbaacaababcacababccbbcbbccbaba","cabbcbcbbbcbbaaabaaaacccacacbbcbabbacbcbabbaaccaabbbaacabaacccbbabcbbcbcbaaabcbcb","cabcbaababaabacabccaccccaacbaacbcaacababacccbbcbbccacbbaccacbaaacacbaccaabaacbcbb","bacbccccbbbcbcbabbbbccaaaccabbcaabbbaabbbbccacabcaccacbacaccaccaabaccbbccacbacbab","bcbcccccacabaaccbbccbacbabbbabbaccaaaccbccbccbcaabacbccbabaaabbaacbcacacabbccbcba","babcaacccaccaacccbaacaccbcacbcabcaacccaccccaaabbbbacbaccabbcbccbcabaccbcbccbacbba","abbbbbbbacbababbbcccaabcbbcbbccbbaccbbcbacbcbbbacbbaacccccabaabbacacabacbbcccbccb"]
"bacaccbcbbbbbbbcbcbbbbabbbbcabccacabcaabacbabbcbbbbabcabaaabccacabccaabbaaaacccaaaabb"
输出：
138

解释：矩阵中不存在 s ，无法提取词语

提示：

0 < matrix.length, matrix[i].length <= 100
0 < mantra.length <= 100
matrix 和 mantra 仅由小写字母组成

"""

from typing import *
from PythonLeetcodeRunner import *


# @lc code=start
# leetcode submit region begin(Prohibit modification and deletion)

class Solution:
    def extractMantra(self, matrix: List[str], mantra: str) -> int:
        """ bfs """
        m, n = len(matrix), len(matrix[0])

        start = [(0, 0, 0, 0)]
        vis = set((0, 0, 0))
        q = deque(start)
        ans = -1
        while q:
            for _ in range(len(q)):
                i, j, ori, step = q.popleft()
                # 如果当前字符是待寻找的字符, 更改ori的状态
                while ori < len(mantra) and matrix[i][j] == mantra[ori]:
                    ori += 1
                    q.append((i, j, ori, step))
                if ori == len(mantra):
                    ans = step
                    q = []
                    break

                for x, y in ((i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j),):
                    if not (0 <= x < m and 0 <= y < n):
                        continue
                    if (x, y, ori) in vis:
                        continue
                    vis.add((x, y, ori))
                    q.append((x, y, ori, step + 1))

        if ans == -1: return -1
        return ans + len(mantra)

# leetcode submit region end(Prohibit modification and deletion)
# @lc code=end

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
