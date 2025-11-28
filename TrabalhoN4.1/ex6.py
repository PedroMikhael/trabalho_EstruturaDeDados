from ex1 import LinkedBinaryTree

def print_paths(tree):
    if tree.is_empty():
        return

    def _recurse(p, path):
        path.append(str(p.element()))

        if tree.is_leaf(p):
            print(" -> ".join(path))
        else:
            if tree.left(p) is not None:
                _recurse(tree.left(p), path)
            if tree.right(p) is not None:
                _recurse(tree.right(p), path)
        
        path.pop()

    _recurse(tree.root(), [])

if __name__ == "__main__":
    t = LinkedBinaryTree()
    root = t._add_root(1)
    
    n2 = t._add_left(root, 2)
    n3 = t._add_right(root, 3)
    
    t._add_left(n2, 4)
    t._add_right(n2, 5)
    
    n6 = t._add_left(n3, 6)
    n7 = t._add_right(n3, 7)
    
    t._add_left(n6, 8)
    t._add_right(n7, 9)

    print("--- Teste: Caminhos da Raiz ate as Folhas ---")
    print("Arvore de Exemplo (visual):")
    print("       1")
    print("     /   \\")
    print("    2     3")
    print("   / \\   / \\")
    print("  4   5 6   7")
    print("       /     \\")
    print("      8       9")
    print("\nCaminhos encontrados:")
    
    print_paths(t)