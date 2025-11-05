from ex12 import LinkedStack

def count_nodes_recursive(node):
    if node is None:
        return 0
    else:
        return 1 + count_nodes_recursive(node._next)

if __name__ == '__main__':
    L = LinkedStack()
    for i in range(8):
        L.push(i)

    print("--- Contagem Recursiva de Nós ---")
    contagem = count_nodes_recursive(L._head)
    print(f"Número de nós na lista: {contagem}")