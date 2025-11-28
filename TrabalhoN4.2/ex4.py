from ex1 import TreeMap

def print_arvore(tree, p=None, prefix="", is_left=True, is_root=True):
    if tree.is_empty():
        print("Árvore Vazia")
        return

    if p is None:
        p = tree.root()

    if tree.right(p):
        new_prefix = prefix + ("│   " if is_left and not is_root else "    ")
        print_arvore(tree, tree.right(p), new_prefix, False, False)

    if is_root:
        conector = "└── " # Raiz
    else:
        conector = "┌── " if not is_left else "└── " # Direita sobe (┌), Esquerda desce (└)

    print(f"{prefix}{conector}{p.key()}")

    # Se tiver filho esquerdo, imprime por último (fica embaixo visualmente)
    if tree.left(p):
        new_prefix = prefix + ("    " if is_left and not is_root else "│   ")
        print_arvore(tree, tree.left(p), new_prefix, True, False)

if __name__ == "__main__":
    print("=== EXERCÍCIO 4: Inserção Progressiva ===")
    print("Objetivo: Inserir [30, 40, 24, 58, 48, 26, 11, 13] e mostrar a evolução.\n")
    print("Dica de Leitura: A Raiz está na esquerda. Galhos para cima são direita (>), para baixo são esquerda (<).\n")
    
    bst = TreeMap()
    chaves = [30, 40, 24, 58, 48, 26, 11, 13]
    
    for i, k in enumerate(chaves):
        print(f"[{i+1}] Inserindo {k}...")
        bst[k] = None # O valor não importa, apenas a chave
        
        # Mostra a árvore atualizada
        print_arvore(bst)
        print("-" * 40) # Linha separadora