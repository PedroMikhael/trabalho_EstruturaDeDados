from ex2 import AVLTreeMap
from ex4 import print_arvore

def run_ex6():
    print("=== EXERCÍCIO 6: Remoção da chave 62 da Árvore da Fig. 11.14b ===")
    

    avl = AVLTreeMap()
    keys_fig_11_14b = [44, 17, 62, 50, 78, 48, 54, 88]
    
    for k in keys_fig_11_14b:
        avl[k] = None

    print("\n[Estado Inicial - Figura 11.14b]")
    print_arvore(avl)
    
    print("\n" + "="*40)
    print(">>> Removendo chave 62...")
    print("O nó 62 tem dois filhos (50 e 78).")
    print("O algoritmo substituirá o 62 pelo seu ANTECESSOR (54) ou SUCESSOR (78),")
    print("dependendo da implementação, e depois rebalanceará.")
    print("="*40 + "\n")
    
    del avl[62]
    
    print("[Estado Final - Após Remoção]")
    print_arvore(avl)

if __name__ == "__main__":
    run_ex6()