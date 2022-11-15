def infix_evaluator(infix_expression: str) -> int:
    '''这是中缀表达式求值的函数
    :参数 infix_expression:中缀表达式
    '''
    token_list = infix_expression.split()
    print(token_list)
    # 运算符优先级字典
    pre_dict = {'*': 3, '/': 3, '+': 2, '-': 2, '(': 1}
    # 运算符栈
    operator_stack = []
    # 操作数栈
    operand_stack = []
    for token in token_list:
        # 数字进操作数栈
        if token.isdecimal() or token[1:].isdecimal():
            operand_stack.append(int(token))
        # 左括号进运算符栈
        elif token == '(':
            operator_stack.append(token)
        # 碰到右括号，就要把栈顶的左括号上面的运算符都弹出求值
        elif token == ')':
            top = operator_stack.pop()
            while top != '(':
                # 每弹出一个运算符，就要弹出两个操作数来求值
                # 注意弹出操作数的顺序是反着的，先弹出的数是op2
                op2 = operand_stack.pop()
                op1 = operand_stack.pop()
                # 求出的值要压回操作数栈
                # 这里用到的函数get_value在下面有定义
                operand_stack.append(get_value(top, op1, op2))
                # 弹出下一个栈顶运算符
                top = operator_stack.pop()
        # 碰到运算符，就要把栈顶优先级不低于它的都弹出求值
        elif token in '+-*/':
            while operator_stack and pre_dict[operator_stack[-1]] >= pre_dict[token]:
                top = operator_stack.pop()
                op2 = operand_stack.pop()
                op1 = operand_stack.pop()
                operand_stack.append(get_value(top, op1, op2))
            # 别忘了最后让当前运算符进栈
            operator_stack.append(token)
    # 表达式遍历完成后，栈里剩下的操作符也都要求值
    while operator_stack:
        top = operator_stack.pop()
        op2 = operand_stack.pop()
        op1 = operand_stack.pop()
        operand_stack.append(get_value(top, op1, op2))
    # 最后栈里只剩下一个数字，这个数字就是整个表达式最终的结果
    return operand_stack[0]


def get_value(operator: str, op1: int, op2: int):
    '''这是四则运算函数
    :参数 operator:运算符
    :参数 op1:左边的操作数
    :参数 op2:右边的操作数
    '''
    if operator == '+':
        return op1 + op2
    elif operator == '-':
        return op1 - op2
    elif operator == '*':
        return op1 * op2
    elif operator == '/':
        return op1 / op2


# 用一个例子试试，得出了结果  -10
print(infix_evaluator(' -5 * 2 - ( -2 + 3 )'))
