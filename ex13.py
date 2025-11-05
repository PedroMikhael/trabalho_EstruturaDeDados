from ex12 import LinkedStack 

def find_second_to_last(L):
    if L.is_empty() or L._head._next is None:
        return None  
    current = L._head
    while current._next._next is not None:
        current = current._next
    return current._element

if __name__ == '__main__':
    L = LinkedStack()
    L.push('C')
    L.push('B')
    L.push('A')  

    print("--- Encontrar Penúltimo Nó ---")
    penultimo = find_second_to_last(L)
    print(f"Penúltimo elemento: {penultimo}")