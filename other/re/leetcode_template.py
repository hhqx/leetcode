import re

def extract_KeyValue_before_equal(str):
    dict_out = {}
    # remove space
    str = str.replace(' ', '')

    # find ',' before '='
    out = {'comma': [], }
    comma = -1
    for idx, c in enumerate(str):
        if c == ',':
            comma = idx
        elif c == '=' and comma >= 0:
            out['comma'].append(comma)
    # print(out)

    # extract key-value string
    start_end_position = [-1] + out['comma'] + [len(str)]
    for i in range(len(start_end_position) - 1):
        start, end = start_end_position[i] + 1, start_end_position[i + 1]
        # print(f'i={i}, {str[start:end]}')

        string = str[start:end]  # key-value string
        # data = re.findall(r'(.*)=(.*)', string)
        # print(data)
        key, value_string = re.findall(r'(.*)=(.*)', string)[0]
        dict_out[key] = eval(value_string)
        print((key, value_string))

    pass

    return dict_out

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

# input and output variable
inout_string = {'Input': [], 'Output': []}
inout_dict = {'Input': [], 'Output': []}

# 正则表达式匹配
matches = re.finditer(regex, test_str, re.MULTILINE)
for matchNum, match in enumerate(matches, start=1):
    # extract input output string
    inout_type = match.group(1)
    inout_str = match.group(2)
    # save to dict
    inout_string[inout_type].append(inout_str)  # append input and output string
    key_value = extract_KeyValue_before_equal(inout_str) if inout_type == "Input" else eval(inout_str)  # get dict
    inout_dict[inout_type].append(key_value)

print(inout_dict)
