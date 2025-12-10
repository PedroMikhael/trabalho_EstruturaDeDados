from ex1 import ArrayStack

def transfer(S, T):
    while not S.is_empty():
        T.push(S.pop())

if __name__ == '__main__':
    S = ArrayStack()
    T = ArrayStack()

    S.push(1)
    S.push(2)
    S.push(3)
    S.push(4)

    print(f"Pilha S antes da transferência: {S._data}")
    print(f"Pilha T antes da transferência: {T._data}")

    transfer(S, T)

    print(f"Pilha S depois da transferência: {S._data}")
    print(f"Pilha T depois da transferência: {T._data}")