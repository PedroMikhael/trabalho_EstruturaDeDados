from ex1 import ArrayStack

def reverse_list(L):
    S = ArrayStack()
    for e in L:
        S.push(e)
    for i in range(len(L)):
        L[i] = S.pop()

if __name__ == '__main__':
    lista_exemplo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"Lista original: {lista_exemplo}")

    reverse_list(lista_exemplo)

    print(f"Lista invertida: {lista_exemplo}")