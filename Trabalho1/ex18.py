from ex12 import LinkedStack

def print_linked_list(L, nome="Lista"):
    elementos = []
    curr = L._head
    while curr:
        elementos.append(curr._element)
        curr = curr._next
    print(f"{nome}: {elementos}")

def split_positive_negative(L):
    positives = LinkedStack()
    negatives = LinkedStack()
    temp_stack = LinkedStack()
    curr = L._head
    while curr is not None:
        temp_stack.push(curr._element)
        curr = curr._next
        
    while not temp_stack.is_empty():
        val = temp_stack.pop()
        if val >= 0:
            positives.push(val)
        else:
            negatives.push(val)
            
    return positives, negatives

if __name__ == '__main__':
    L = LinkedStack()
    numeros = [-5, 10, -2, 8, 0, -1]
    for num in numeros:
        L.push(num)
        
    print("--- Separar Positivos e Negativos ---")
    print_linked_list(L, "Lista Original (LIFO)")
    
    pos, neg = split_positive_negative(L)
    
    print_linked_list(pos, "Positivos")
    print_linked_list(neg, "Negativos")