from ex1 import LinkedBinaryTree

def transform_to_sum_tree(tree):
    if tree.is_empty():
        return

    def _process_node(p):
        if p is None:
            return 0
        
        left_sum = _process_node(tree.left(p))
        right_sum = _process_node(tree.right(p))
        
        old_val = int(p.element())
        
        new_val = left_sum + right_sum
        
        tree._replace(p, new_val)
        
        return old_val + new_val

    _process_node(tree.root())

if __name__ == "__main__":
    t = LinkedBinaryTree()
    
    root = t._add_root(1)
    
    n2 = t._add_left(root, 2)
    n3 = t._add_right(root, 3)
    
    t._add_left(n2, 4)
    n5 = t._add_right(n2, 5)
    
    t._add_right(n3, 6)
    
    t._add_left(n5, 7)
    t._add_right(n5, 8)

    print("--- Teste: Transformacao em Arvore Soma (Exercicio 8) ---")
    print("Arvore Original (Pre-transformacao):")
    print("Estrutura visual:")
    print("        1")
    print("      /   \\")
    print("     2     3")
    print("    / \\     \\")
    print("   4   5     6")
    print("      / \\")
    print("     7   8")
    print(f"Percurso Inorder Original: {' -> '.join(str(p.element()) for p in t.inorder())}")
    
    transform_to_sum_tree(t)

    print("\nArvore Transformada:")
    print("Logica: Valor do no = Soma de todos os elementos das subarvores esquerda e direita")
    print("Folhas tornam-se 0.")
    print("No 5 = 7 + 8 = 15")
    print("No 2 = 4 + (5 + 7 + 8) = 24")
    print("No 3 = 6")
    print("Raiz 1 = (2 + 4 + 5 + 7 + 8) + (3 + 6) = 26 + 9 = 35")
    
    print(f"Percurso Inorder Transformado: {' -> '.join(str(p.element()) for p in t.inorder())}")