from ex12 import LinkedStack

def print_list(node):
    values = []
    while node:
        values.append(node._element)
        node = node._next
    print(values)

def reverse_recursive(curr, prev=None):   
    if curr is None:
        return prev  

    next_node = curr._next

    curr._next = prev

    return reverse_recursive(next_node, curr)

if __name__ == '__main__':
    L = LinkedStack()
    L.push(6)
    L.push(5)
    L.push(4)
    L.push(3)
    L.push(2)
    L.push(1)
    L.push(0)
    
    print("--- Reversão Recursiva ---")
    print("Lista original:")
    print_list(L._head) 
    new_head = reverse_recursive(L._head)
    L._head = new_head

    print("Lista invertida:")
    print_list(L._head) 