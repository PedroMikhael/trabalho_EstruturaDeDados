from ex2 import AVLTreeMap
from ex4 import print_arvore

def run_ex5():
    print("=== EXERCÍCIO 5: Inserção de 52 na Árvore da Fig. 11.14b ===")
    
    avl = AVLTreeMap()
    keys_fig_11_14b = [62, 44, 78, 17, 50, 88, 48, 54]
    
    for k in keys_fig_11_14b:
        avl[k] = None

    print("\n[Estado Inicial - Figura 11.14b]")
    print_arvore(avl)
    
    print("\n" + "="*40)
    print(">>> Inserindo chave 52...")
    print("Isso causará um desbalanceamento no nó 44.")
    print("Correção esperada: Rotação (Trinode Restructuring) envolvendo 44, 50 e 54.")
    print("="*40 + "\n")
    
    avl[52] = None
    
    print("[Estado Final - Após Inserção e Balanceamento]")
    print_arvore(avl)

if __name__ == "__main__":
    run_ex5()