from ex1 import LinkedBinaryTree

def are_identical(tree1, tree2):
    def _check_structure_and_content(p1, p2):
        if p1 is None and p2 is None:
            return True
        
        if p1 is None or p2 is None:
            return False
        
        if p1.element() != p2.element():
            return False
        
        left_identical = _check_structure_and_content(tree1.left(p1), tree2.left(p2))
        right_identical = _check_structure_and_content(tree1.right(p1), tree2.right(p2))
        
        return left_identical and right_identical

    if tree1.is_empty() and tree2.is_empty():
        return True
    
    return _check_structure_and_content(tree1.root(), tree2.root())

if __name__ == "__main__":
    t1 = LinkedBinaryTree()
    r1 = t1._add_root(10)
    t1._add_left(r1, 5)
    t1._add_right(r1, 15)

    t2 = LinkedBinaryTree()
    r2 = t2._add_root(10)
    t2._add_left(r2, 5)
    t2._add_right(r2, 15)

    t3 = LinkedBinaryTree()
    r3 = t3._add_root(10)
    t3._add_left(r3, 5)

    t4 = LinkedBinaryTree()
    r4 = t4._add_root(10)
    t4._add_left(r4, 5)
    t4._add_right(r4, 99)

    print("--- Teste 1: Arvores Identicas ---")
    print(f"Arvore 1: 10 -> (5, 15)")
    print(f"Arvore 2: 10 -> (5, 15)")
    print(f"Resultado: {are_identical(t1, t2)}")
    print()

    print("--- Teste 2: Estruturas Diferentes ---")
    print(f"Arvore 1: 10 -> (5, 15)")
    print(f"Arvore 3: 10 -> (5, None)")
    print(f"Resultado: {are_identical(t1, t3)}")
    print()

    print("--- Teste 3: Mesmo formato, conteudos diferentes ---")
    print(f"Arvore 1: 10 -> (5, 15)")
    print(f"Arvore 4: 10 -> (5, 99)")
    print(f"Resultado: {are_identical(t1, t4)}")