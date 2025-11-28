from ex1 import TreeMap

class AVLTreeMap(TreeMap):
    class _Node(TreeMap._Node):
        __slots__ = '_height'
        def __init__(self, element, parent=None, left=None, right=None):
            super().__init__(element, parent, left, right)
            self._height = 0
        def left_height(self):
            return self._left._height if self._left is not None else 0
        def right_height(self):
            return self._right._height if self._right is not None else 0

    def _recompute_height(self, p):
        p._node._height = 1 + max(p._node.left_height(), p._node.right_height())

    def _isbalanced(self, p):
        return abs(p._node.left_height() - p._node.right_height()) <= 1

    def _tall_child(self, p, favorleft=False):
        if p._node.left_height() + (1 if favorleft else 0) > p._node.right_height():
            return self.left(p)
        else:
            return self.right(p)

    def _tall_grandchild(self, p):
        child = self._tall_child(p)
        alignment = (child == self.left(p))
        return self._tall_child(child, alignment)

    def _rebalance(self, p):
        while p is not None:
            old_height = p._node._height
            if not self._isbalanced(p):
                p = self._restructure(self._tall_grandchild(p))
                self._recompute_height(self.left(p))
                self._recompute_height(self.right(p))
            self._recompute_height(p)
            if p._node._height == old_height:
                p = None
            else:
                p = self.parent(p)

    def _rebalance_insert(self, p):
        self._rebalance(p)

    def _rebalance_delete(self, p):
        self._rebalance(p)

if __name__ == "__main__":
    print("=== EXERCÍCIO 2: Teste da Classe AVLTreeMap (Balanceada) ===")
    
    avl = AVLTreeMap()
    
    print("\n1. Inserindo elementos em ordem sequencial: 1, 2, 3, 4, 5, 6, 7")
    print("   (Em uma árvore comum, isso criaria uma lista de altura 7)")
    
    for i in range(1, 8):
        avl[i] = None
        
    root_pos = avl.root()
    print(f"\n2. Verificação da Raiz Atual: {root_pos.key()}")
    
    print(f"3. Altura da Raiz (deve ser pequena, aprox log n): {root_pos._node._height}")
    
    left_child = avl.left(root_pos)
    right_child = avl.right(root_pos)
    
    print(f"4. Estrutura imediata abaixo da raiz:")
    print(f"   Filho Esquerdo: {left_child.key() if left_child else 'None'}")
    print(f"   Filho Direito:  {right_child.key() if right_child else 'None'}")
    
    print("\n5. Removendo a raiz atual...")
    del avl[root_pos.key()]
    
    new_root = avl.root()
    print(f"   Nova Raiz após remoção e rebalanceamento: {new_root.key()}")
    print(f"   Nova Altura: {new_root._node._height}")