from ex12 import LinkedDeque

def print_deque(D, nome="Deque"):
    elementos = []
    if not D.is_empty():
        curr = D._header._next
        while curr is not D._trailer:
            elementos.append(curr._element)
            curr = curr._next
    print(f"{nome}: {elementos}")

def remove_duplicates(D):
    if D.is_empty():
        return

    vistos = set()
    curr = D._header._next
    
    while curr is not D._trailer:
        next_node = curr._next
        
        if curr._element in vistos:
            D._delete_node(curr)
        else:
            vistos.add(curr._element)
            
        curr = next_node

if __name__ == '__main__':
    D = LinkedDeque()
    elementos = [10, 20, 10, 30, 20, 40, 10]
    for e in elementos:
        D.insert_last(e)

    print("--- Remover Duplicatas (Lista Duplamente Encadeada) ---")
    print_deque(D, "Deque Original")
    
    remove_duplicates(D)
    
    print_deque(D, "Deque sem Duplicatas")