from ex1 import ArrayQueue

def imprimir_fila(Q):
    if Q.is_empty():
        print(f"  Fila : []")
    else:
        logica = [Q._data[(Q._front + i) % len(Q._data)] for i in range(len(Q))]
        print(f"  Fila : {logica}")
    print(f"  (Array interno: {Q._data}, size: {len(Q)})")

Q = ArrayQueue()
print("Estado Inicial:")
imprimir_fila(Q)


Q.enqueue(5)
imprimir_fila(Q)

Q.enqueue(3)
imprimir_fila(Q)

retorno = Q.dequeue()

imprimir_fila(Q)


Q.enqueue(2)
imprimir_fila(Q)


Q.enqueue(8)
imprimir_fila(Q)


retorno = Q.dequeue()
imprimir_fila(Q)


retorno = Q.dequeue()

imprimir_fila(Q)

Q.enqueue(9)
imprimir_fila(Q)

Q.enqueue(1)
imprimir_fila(Q)

retorno = Q.dequeue()
imprimir_fila(Q)

Q.enqueue(7)
imprimir_fila(Q)

Q.enqueue(6)
imprimir_fila(Q)

retorno = Q.dequeue()
imprimir_fila(Q)

retorno = Q.dequeue()
imprimir_fila(Q)

Q.enqueue(4)
imprimir_fila(Q)

retorno = Q.dequeue()
imprimir_fila(Q)

retorno = Q.dequeue()
imprimir_fila(Q)

print("\n--- RESULTADO FINAL ---")
imprimir_fila(Q)