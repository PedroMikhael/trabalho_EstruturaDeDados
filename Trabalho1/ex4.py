from ex1 import ArrayStack

def empty_stack_recursively(S):
    if S.is_empty():
        return
    S.pop()
    empty_stack_recursively(S)

if __name__ == '__main__':
    S = ArrayStack()
    for i in range(1, 6):
        S.push(i)

    print(f"Pilha antes: {S._data}")
    empty_stack_recursively(S)
    print(f"Pilha depois: {S._data}")