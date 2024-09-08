def evaluate(expression):
    """Evaluates a given arithmetic expression."""
    i = 0
    operators = []
    operands = []
    while i < len(expression):
        if expression[i] == ' ':
            i += 1
            continue
        elif expression[i] == '(':
            operators.append(expression[i])
        elif expression[i].isdigit():
            val = 0
            while i < len(expression) and expression[i].isdigit():
                val = (val * 10) + int(expression[i])
                i += 1
            operands.append(val)
            i -= 1
        elif expression[i] == ')':
            while operators and operators[-1] != '(':
                process(operators, operands)
            operators.pop()
        else:
            while operators and precedence(operators[-1]) >= precedence(expression[i]):
                process(operators, operands)
            operators.append(expression[i])
        i += 1
    while operators:
        process(operators, operands)
    return operands[-1]

def precedence(op):
    """Returns the precedence of an operator. Higher number means higher precedence."""
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    return 0

def process(operators, operands):
    """Processes the top operator on the operator stack."""
    operator = operators.pop()
    operands.append(apply_operation(operands, operator))

def apply_operation(operands, operator):
    """Applies an arithmetic operation to two operands."""
    a = operands.pop()
    b = operands.pop()
    if operator == '+':
        return b + a
    elif operator == '-':
        return b - a
    elif operator == '*':
        return b * a
    elif operator == '/':
        return b / a
