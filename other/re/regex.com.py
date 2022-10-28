# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility

import re

regex = r"^(Input|Output): ?(.*)$"

test_str = ("Given an array of integers nums and an integer target, return indices of the \n"
            "two numbers such that they add up to target. \n\n"
            " You may assume that each input would have exactly one solution, and you may \n"
            "not use the same element twice. \n\n"
            " You can return the answer in any order. \n"
            "heello\n"
            " \n"
            " Example 1: \n\n"
            " \n"
            "Input:nums = [2,7,11,15], target = 9\n"
            "Output: [0,1]\n"
            "Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].\n"
            " \n\n"
            " Example 2: \n\n"
            " \n"
            "Input: nums = [3,2,4], sdf = [3,2,4], target = 6\n"
            "Output: [1,2]\n"
            " \n\n"
            " Example 3: \n\n"
            " \n"
            "Input: nums = [3,3], target = 6, sdf = [3,2,4]\n"
            "Output: [0,1]\n"
            " \n\n"
            " \n"
            " Constraints: \n\n"
            " \n"
            " 2 <= nums.length <= 10⁴ \n"
            " -10⁹ <= nums[i] <= 10⁹ \n"
            " -10⁹ <= target <= 10⁹ \n"
            " Only one valid answer exists. \n"
            " \n\n"
            " \n"
            "Follow-up: Can you come up with an algorithm that is less than O(n²) time \n"
            "complexity? Related Topics Array Hash Table 👍 33227 👎 1052")

matches = re.finditer(regex, test_str, re.MULTILINE)

out = {'Input': [], 'Output': []}
for matchNum, match in enumerate(matches, start=1):

    print("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum=matchNum, start=match.start(),
                                                                        end=match.end(), match=match.group()))

    inout_type = match.group(1)
    inout_str = match.group(2)
    out[inout_type].append(inout_str)  # append input and output string

    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1

        print("Group {groupNum} found at {start}-{end}: {group}".format(groupNum=groupNum, start=match.start(groupNum),
                                                                        end=match.end(groupNum),
                                                                        group=match.group(groupNum)))

# Note: for Python 2.7 compatibility, use ur"" to prefix the regex and u"" to prefix the test string and substitution.
print(out)

