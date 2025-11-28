from ex1 import LinkedBinaryTree

def is_sum_tree(tree):
    valid_state = [True]

    def get_subtree_sum(p):
        if p is None:
            return 0
        
        if not valid_state[0]:
            return 0

        left_sum = get_subtree_sum(tree.left(p))
        right_sum = get_subtree_sum(tree.right(p))
        
        current_val = int(p.element())

        if tree.is_leaf(p):
            return current_val
        
        if current_val != (left_sum + right_sum):
            valid_state[0] = False

        return current_val + left_sum + right_sum

    if tree.is_empty():
        return True

    get_subtree_sum(tree.root())
    return valid_state[0]

if __name__ == "__main__":
    t_valid = LinkedBinaryTree()
    root = t_valid._add_root(44)
    
    n9 = t_valid._add_left(root, 9)
    n13 = t_valid._add_right(root, 13)
    
    t_valid._add_left(n9, 4)
    t_valid._add_right(n9, 5)
    
    t_valid._add_left(n13, 6)
    t_valid._add_right(n13, 7)

    t_invalid = LinkedBinaryTree()
    root_inv = t_invalid._add_root(10)
    t_invalid._add_left(root_inv, 3) 
    t_invalid._add_right(root_inv, 4) 

    print("--- Teste 1: Arvore Soma Valida (Exemplo do PDF) ---")
    print("Estrutura:")
    print("      44")
    print("     /  \\")
    print("    9    13")
    print("   / \\   / \\")
    print("  4   5 6   7")
    print("\nVerificacao:")
    print("Nó 9: 4 + 5 = 9 (OK)")
    print("Nó 13: 6 + 7 = 13 (OK)")
    print("Raiz 44: 9 + 4 + 5 + 13 + 6 + 7 = 44 (OK)")
    print(f"Resultado: {is_sum_tree(t_valid)}")
    print()

    print("--- Teste 2: Arvore Invalida ---")
    print("Estrutura:")
    print("      10")
    print("     /  \\")
    print("    3    4")
    print("\nVerificacao:")
    print("Raiz 10 != 3 + 4 (Soma e 7)")
    print(f"Resultado: {is_sum_tree(t_invalid)}")