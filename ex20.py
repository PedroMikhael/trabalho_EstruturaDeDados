from ex12 import LinkedDeque

class ReversibleLinkedDeque(LinkedDeque):
    def reverse(self):
        curr = self._header
        while curr is not None:
            curr._next, curr._prev = curr._prev, curr._next
            curr = curr._prev
        self._header, self._trailer = self._trailer, self._header

def print_deque(D, nome="Deque"):
    elementos = []
    if not D.is_empty():
        curr = D._header._next
        while curr is not D._trailer:
            elementos.append(curr._element)
            curr = curr._next
    print(f"{nome}: {elementos}")

if __name__ == '__main__':
    D = ReversibleLinkedDeque()
    for i in range(1, 6):
        D.insert_last(i)

    print("--- Inverter Lista Duplamente Encadeada (In-place) ---")
    print_deque(D, "Original")
    
    D.reverse()
    
    print_deque(D, "Invertido")
    
    print(f"Novo primeiro elemento: {D.first()}")
    print(f"Novo último elemento: {D.last()}")
    
    D.insert_last(6)
    print_deque(D, "Após inserir 6 no final apenas para mostrar que o 1 virou o ultimo elemento")