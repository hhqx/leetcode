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

class extract_value:
    def __init__(self, str=''):

        # remove space
        str = str.replace(' ', '')

        # find ',' before '='
        out = {'comma': [], }
        comma = -1
        for idx, c in enumerate(str):
            if c == ',':
                comma = idx
            elif c == '=':
                out['comma'].append(comma)
        print(out)

        # extract key-value string
        start_end_position = [-1] + out['comma'][1:] + [len(str)]
        for i in range(len(start_end_position)-1):
            start, end = start_end_position[i] + 1, start_end_position[i+1]
            print(str[start:end])

        # transform key-value string to dict

        pass


str = 'nums = [2,7,11,15], target = 9, target = 9'
# extract_value(str)

out = extract_KeyValue_before_equal(str)
print(out)