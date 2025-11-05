from ex1 import ArrayDeque

def imprimir_deque(D):
    if D.is_empty():
        print(f"  Deque : []")
    else:
        logica = [D._data[(D._front + i) % len(D._data)] for i in range(len(D))]
        print(f"  Deque : {logica}")
    print(f"  (Array interno: {D._data}, size: {len(D)})")

D = ArrayDeque()
print("Estado Inicial:")
imprimir_deque(D)

D.add_first(4)
imprimir_deque(D)

D.add_last(8)
imprimir_deque(D)

D.add_last(9)
imprimir_deque(D)

D.add_first(5)
imprimir_deque(D)

retorno = D.last()
imprimir_deque(D)

retorno = D.delete_first()
imprimir_deque(D)

retorno = D.delete_last()
imprimir_deque(D)

D.add_last(7)
imprimir_deque(D)

retorno = D.first()
imprimir_deque(D)

retorno = D.last()
imprimir_deque(D)

D.add_last(6)
imprimir_deque(D)

retorno = D.delete_first()
imprimir_deque(D)

retorno = D.delete_first()
imprimir_deque(D)

imprimir_deque(D)