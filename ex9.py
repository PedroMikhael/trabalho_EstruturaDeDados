from ex1 import ArrayStack

def is_operator(c):
    return c in ['+', '-', '*', '/', '^']

def prefix_to_infix(expr):
    S = ArrayStack()
    tokens = expr.split()[::-1]

    for token in tokens:
        if is_operator(token):
            op1 = S.pop()
            op2 = S.pop()
            temp = f"({op1} {token} {op2})"
            S.push(temp)
        else:
            S.push(token)

    return S.pop()

def prefix_to_postfix(expr):
    S = ArrayStack()
    tokens = expr.split()[::-1]

    for token in tokens:
        if is_operator(token):
            op1 = S.pop()
            op2 = S.pop()
            temp = f"{op1} {op2} {token}"
            S.push(temp)
        else:
            S.push(token)

    return S.pop()

if __name__ == '__main__':
    prefix_exprs = [
        "* + A B - C D",
        "+ - * A B C D",
        "+ * A B C"
    ]

    print("--- Conversor de Expressões (Prefixada) ---\n")
    for expr in prefix_exprs:
        print(f"Prefixada Original: {expr}")
        print(f" -> Infixa:         {prefix_to_infix(expr)}")
        print(f" -> Pós-fixada:     {prefix_to_postfix(expr)}")
        print("-" * 30)