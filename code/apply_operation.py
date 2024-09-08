def apply_operation(operands, operator):
    """Applies an arithmetic operation to two operands."""
    a = operands.pop()
    b = operands.pop()
    if operator == '+':
        return b + a
    elif operator == '-':
        return b - a
    elif operator == '*':
        return b + a
    elif operator == '/':
        return b / a
