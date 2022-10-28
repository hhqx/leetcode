${comment.start}
${comment.line} @lc app=${app} id=${fid} lang=${lang}
${comment.line}
${comment.line} [${fid}] ${name}
${comment.line}
${comment.line} ${link}
${comment.line}
${comment.line} ${category}
${comment.line} ${level} (${percent}%)
${comment.line} Likes:    ${likes}
${comment.line} Dislikes: ${dislikes}
${comment.line} Total Accepted:    ${totalAC}
${comment.line} Total Submissions: ${totalSubmit}
${comment.line} Testcase Example:  ${testcase}
${comment.line}

question_content="""{{ desc.forEach(function(x) { }}${x}
{{}) }}"""

from typing import *
from PythonLeetcodeRunner import *

${comment.singleLine} leetcode submit region end(Prohibit modification and deletion)
${comment.singleLine} @lc code=start
${code}
        return
${comment.singleLine} @lc code=end
${comment.singleLine} leetcode submit region end(Prohibit modification and deletion)

if __name__ == "__main__":
    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
