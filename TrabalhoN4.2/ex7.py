from ex3 import RedBlackTreeMap
from ex4 import print_arvore

def run_ex7():
    print("=== EXERCÍCIO 7: Inserção em Árvore Rubro-Negra ===")
    print("Sequência: 5, 16, 22, 45, 2, 10, 18, 30, 50, 12, 1")
    
    rbt = RedBlackTreeMap()
    keys = [5, 16, 22, 45, 2, 10, 18, 30, 50, 12, 1]
    
    print("\nIniciando inserções...")
    for k in keys:
        rbt[k] = None
    
    print("\n[Estado Final da Árvore Rubro-Negra]")
    print(f"Total de nós: {len(rbt)}")
    print(f"Raiz: {rbt.root().key()}")
    print("-" * 40)
    
    print_arvore(rbt)
    
    print("-" * 40)
    print("Nota: A árvore Rubro-Negra garante balanceamento O(log n)")
    print("através de rotações e recolorações automáticas.")

if __name__ == "__main__":
    run_ex7()