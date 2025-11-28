from ex12 import LinkedStack

def print_singly_linked_list(L, message=""):
    """Função auxiliar para imprimir os elementos da lista."""
    if L.is_empty():
        print(f"{message} []")
        return
    
    nodes = []
    curr = L._head
    while curr is not None:
        nodes.append(curr._element)
        curr = curr._next
    print(f"{message} {nodes}")

def concatenate(L, M):
    
    if L.is_empty():
        L._head = M._head
        L._size = M._size
    elif not M.is_empty():
        tail_L = L._head
        while tail_L._next is not None:
            tail_L = tail_L._next
        
        tail_L._next = M._head
        L._size += M._size
    
    M._head = None
    M._size = 0

if __name__ == '__main__':
    L = LinkedStack()
    L.push('C')
    L.push('B')
    L.push('A')
    
    M = LinkedStack()
    M.push('F')
    M.push('E')
    M.push('D')
    
    print("--- Concatenar Listas ---")
    print_singly_linked_list(L, "Lista L antes (A->B->C):")
    print_singly_linked_list(M, "Lista M antes (D->E->F):")

    concatenate(L, M)
    
    print("\n--- Resultado ---")
    print_singly_linked_list(L, "Lista L depois (A->...->F):")
    print_singly_linked_list(M, "Lista M depois:")