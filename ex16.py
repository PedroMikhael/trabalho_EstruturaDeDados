from ex12 import CircularQueue

def count_nodes_circular(C):
    if C.is_empty():
        return 0

    start_node = C._tail._next
    count = 1
    current = start_node._next

    while current is not start_node:
        count += 1
        current = current._next

    return count

if __name__ == '__main__':
    C = CircularQueue()
    C.enqueue(10)
    C.enqueue(20)
    C.enqueue(30)
    C.enqueue(40)

    print("--- Contagem em Lista Circular ---")
    contagem = count_nodes_circular(C)
    print(f"Número de nós na lista circular: {contagem}")