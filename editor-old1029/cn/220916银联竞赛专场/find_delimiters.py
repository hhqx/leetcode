

s = """["StockPrice", "update", "update", "current",
 "maximum", 
"update", "maximum", "update", 
"minimum"
],
[[], [1, 10], [2, 5], [], [], [1, 3], [], [4, 2], []]"""

def find_comma(str):
    delimiter = []
    comma = -1
    for idx, c in enumerate(str):
        if c == ',':
            comma = idx
        elif c == '=' and comma >= 0:
            delimiter.append(comma)
    delimiter += [len(str)]
    return delimiter


def find_delimiter():
    char_in = ['[', '{', '(', '"', "'", ]
    char_out = [']', '}', ')', '"', "'", ]

    ans = []
    stack = []
    for i, c in enumerate(s):
        if c in char_in:
            if stack and stack[-1] in ['"', ","]:
                stack.pop()
            else:
                stack.append(c)
        elif c in char_out:
            stack.pop()
            if not stack:
                ans.append(i+1)
    return ans

# bound = [-1] + find_delimiter()
bound = [-1] + find_comma(s)
for i in range(len(bound)-1):
    print(s[bound[i]+1:bound[i+1]])
    print('-'*20)

