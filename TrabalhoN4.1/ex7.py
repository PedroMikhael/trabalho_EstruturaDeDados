from ex1 import LinkedBinaryTree

def get_ancestors(tree, p):
    ancestors = []
    curr = tree.parent(p)
    
    while curr is not None:
        ancestors.append(curr.element())
        curr = tree.parent(curr)
        
    return ancestors

if __name__ == "__main__":
    t = LinkedBinaryTree()
    
    n1 = t._add_root(1)
    
    n2 = t._add_left(n1, 2)
    n3 = t._add_right(n1, 3)
    
    n4 = t._add_left(n2, 4)
    n5 = t._add_right(n2, 5)
    
    n6 = t._add_left(n3, 6)
    n7 = t._add_right(n3, 7)
    
    n8 = t._add_right(n6, 8)
    n9 = t._add_right(n7, 9)

    print("--- Teste: Encontrar Ancestrais (Exemplo do PDF) ---")
    print("Arvore Montada:")
    print("       1")
    print("     /   \\")
    print("    2     3")
    print("   / \\   / \\")
    print("  4   5 6   7")
    print("         \\   \\")
    print("          8   9")
    print()

    anc_9 = get_ancestors(t, n9)
    print(f"Ancestrais do no 9 (Esperado: [7, 3, 1]): {anc_9}")

    anc_6 = get_ancestors(t, n6)
    print(f"Ancestrais do no 6 (Esperado: [3, 1]): {anc_6}")

    anc_5 = get_ancestors(t, n5)
    print(f"Ancestrais do no 5 (Esperado: [2, 1]): {anc_5}")