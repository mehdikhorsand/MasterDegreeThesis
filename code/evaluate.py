def evaluate(expression):
    """Evaluates a given arithmetic expression."""
    Recorder.method_called()    # added manually
    i = 0
    operators = []
    operands = []
    while i < len(expression):
        Recorder.loop_covered()    # added manually
        if expression[i] == ' ':
            i += 1
            continue
        elif expression[i] == '(':
            operators.append(expression[i])
        elif expression[i].isdigit():
            val = 0
            while i < len(expression) and expression[i].isdigit():
                Recorder.loop_covered()    # added manually
                val = (val * 10) + int(expression[i])
                i += 1
            operands.append(val)
            i -= 1
        elif expression[i] == ')':
            while operators and operators[-1] != '(':
                Recorder.loop_covered()    # added manually
                process(operators, operands)
            operators.pop()
        else:
            while operators and precedence(operators[-1]) >= precedence(expression[i]):
                Recorder.loop_covered()    # added manually
                process(operators, operands)
            operators.append(expression[i])
        i += 1
    while operators:
        Recorder.loop_covered()    # added manually
        process(operators, operands)
    return operands[-1]
