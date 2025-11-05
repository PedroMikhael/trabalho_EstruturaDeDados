from ex1 import ArrayStack

def precedence(op):
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    return 0

def apply_op(op, b, a):
    if op == '+': return a + b
    if op == '-': return a - b
    if op == '*': return a * b
    if op == '/': return a // b
    return 0

def evaluate(expression):
    values = ArrayStack()
    ops = ArrayStack()
    i = 0
    while i < len(expression):
        if expression[i] == ' ':
            i += 1
            continue
        elif expression[i] == '(':
            ops.push(expression[i])
        elif expression[i].isdigit():
            val = 0
            while i < len(expression) and expression[i].isdigit():
                val = (val * 10) + int(expression[i])
                i += 1
            values.push(val)
            i -= 1
        elif expression[i] == ')':
            while not ops.is_empty() and ops.top() != '(':
                val2 = values.pop()
                val1 = values.pop()
                op = ops.pop()
                values.push(apply_op(op, val2, val1))
            if not ops.is_empty():
                ops.pop()
        else:
            while not ops.is_empty() and precedence(ops.top()) >= precedence(expression[i]):
                val2 = values.pop()
                val1 = values.pop()
                op = ops.pop()
                values.push(apply_op(op, val2, val1))
            ops.push(expression[i])
        i += 1
    while not ops.is_empty():
        val2 = values.pop()
        val1 = values.pop()
        op = ops.pop()
        values.push(apply_op(op, val2, val1))
    return values.pop()

if __name__ == '__main__':
    exprs = [
        "10 + 2 * 6",
        "100 * ( 2 + 12 )",
        "100 * ( 2 + 12 ) / 14",
        "50 - 20 - 10"
    ]

    print("--- Calculadora (Inteiros) ---")
    for expr in exprs:
        print(f"{expr} = {evaluate(expr)}")