class LinkedBinaryTree:
    """Implementa o TAD BinaryTree usando uma estrutura ligada (encadeada)."""
    class _Node:
        __slots__ = '_element', '_parent', '_left', '_right'

        def __init__(self, element, parent=None, left=None, right=None):
            """Inicializa um nó com referências ao elemento, pai, filho esquerdo e direito."""
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right

    class Position:
        """Abstração representando o local de um único elemento na árvore."""

        def __init__(self, container, node):
            """Construtor não deve ser invocado pelo usuário."""
            self._container = container  
            self._node = node

        def element(self):
            """Retorna o elemento armazenado nesta Posição."""
            return self._node._element

        def __eq__(self, other):
            """Retorna True se 'other' representa o mesmo local."""
            return type(other) is type(self) and other._node is self._node
            
        def __ne__(self, other):
            """Retorna True se 'other' não representa o mesmo local."""
            return not (self == other)

    
    def _validate(self, p):
        """Retorna o nó associado, se a posição for válida"""
        if not isinstance(p, self.Position):
            raise TypeError('p deve ser um tipo Position adequado')
        if p._container is not self:
            raise ValueError('p não pertence a este container')
        if p._node._parent is p._node:  
            raise ValueError('p não é mais válido')
        return p._node

    def _make_position(self, node):
        """Retorna a instância Position para um dado nó (ou None se não houver nó)."""
        return self.Position(self, node) if node is not None else None

    
    def __init__(self):
        """Cria uma árvore binária inicialmente vazia."""
        self._root = None  
        self._size = 0     

    def __len__(self):
        """Retorna o número total de elementos na árvore."""
        return self._size

    def is_empty(self):
        """Retorna True se a árvore estiver vazia."""
        return len(self) == 0

    def root(self):
        """Retorna a Posição raiz da árvore (ou None se vazia)."""
        return self._make_position(self._root)

    def parent(self, p):
        """Retorna a Posição do pai de p (ou None se p for a raiz)."""
        node = self._validate(p)
        return self._make_position(node._parent)

    def left(self, p):
        """Retorna a Posição do filho esquerdo de p (ou None se não houver)."""
        node = self._validate(p)
        return self._make_position(node._left)

    def right(self, p):
        """Retorna a Posição do filho direito de p (ou None se não houver)."""
        node = self._validate(p)
        return self._make_position(node._right)

    def num_children(self, p):
        """Retorna o número de filhos de Posição p."""
        node = self._validate(p)
        count = 0
        if node._left is not None:
            count += 1
        if node._right is not None:
            count += 1
        return count
    
    def is_root(self, p):
        """Retorna True se a Posição p representa a raiz da árvore."""
        return self.root() == p

    def is_leaf(self, p):
        """Retorna True se a Posição p não tem filhos."""
        return self.num_children(p) == 0

    def children(self, p):
        """Gera uma iteração das Posições representando os filhos de p (Esquerda, depois Direita)."""
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)

    def sibling(self, p):
        """Retorna a Posição do irmão de p (ou None se não houver irmão)."""
        parent = self.parent(p)
        if parent is None:
            return None  
        if p == self.left(parent):
            return self.right(parent)  
        else:
            return self.left(parent)  
  

    def _add_root(self, e):
        """Coloca o elemento e na raiz de uma árvore vazia e retorna a nova Posição.
        Levanta ValueError se a árvore não estiver vazia."""
        if self._root is not None: 
            raise ValueError('Root exists')
        self._size = 1
        self._root = self._Node(e)
        return self._make_position(self._root)

    def _add_left(self, p, e):
        """Cria um novo filho esquerdo para a Posição p, armazenando o elemento e.
        Levanta ValueError se p já tiver um filho esquerdo."""
        node = self._validate(p)
        if node._left is not None: 
            raise ValueError('Left child exists')
        self._size += 1
        node._left = self._Node(e, node)  
        return self._make_position(node._left)

    def _add_right(self, p, e):
        """Cria um novo filho direito para a Posição p, armazenando o elemento e.
        Levanta ValueError se p já tiver um filho direito."""
        node = self._validate(p)
        if node._right is not None: 
            raise ValueError('Right child exists')
        self._size += 1
        node._right = self._Node(e, node)  
        return self._make_position(node._right)

    def _replace(self, p, e):
        """Substitui o elemento na posição p por e, e retorna o elemento antigo."""
        node = self._validate(p)
        old = node._element
        node._element = e
        return old

    def _delete(self, p):
        """Remove o nó em p, substituindo-o pelo seu filho, se houver.
        Levanta ValueError se p tiver dois filhos."""
        node = self._validate(p)
        if self.num_children(p) == 2: 
            raise ValueError('p has two children')
            
        child = node._left if node._left else node._right  
        
        if child is not None:
            child._parent = node._parent  
            
        if node is self._root:
            self._root = child  
        else:
            parent = node._parent
            if node is parent._left:
                parent._left = child
            else:
                parent._right = child
                
        self._size -= 1
        node._parent = node 
        return node._element

    def _attach(self, p, t1, t2):
        """Anexa árvores t1 e t2 como subárvores esquerda e direita do nó folha p.
        Reseta t1 e t2 para árvores vazias. Levanta erro se p não for folha."""
        node = self._validate(p)
        if not self.is_leaf(p): 
            raise ValueError('position must be leaf')
        if not type(self) is type(t1) is type(t2):
            raise TypeError('Tree types must match')
        
        self._size += len(t1) + len(t2)
        
        if not t1.is_empty():
            t1._root._parent = node
            node._left = t1._root
            t1._root = None
            t1._size = 0
            
        if not t2.is_empty():
            t2._root._parent = node
            node._right = t2._root
            t2._root = None
            t2._size = 0
    
    def __iter__(self):
        """Gera uma iteração dos elementos da árvore (usa positions() por padrão)."""
        for p in self.positions(): 
            yield p.element()

    def positions(self):
        """Gera uma iteração das posições da árvore (Em-ordem para BinaryTree)."""
        return self.inorder()

    def inorder(self):
        """Gera uma iteração em-ordem das posições na árvore binária."""
        if not self.is_empty():
            for p in self._subtree_inorder(self.root()):
                yield p

    def _subtree_inorder(self, p):
        """Função auxiliar recursiva para percurso em-ordem."""
        if self.left(p) is not None:
            for other in self._subtree_inorder(self.left(p)):
                yield other
        yield p
        if self.right(p) is not None:
            for other in self._subtree_inorder(self.right(p)):
                yield other
    
    def depth(self, p):
        """Calcula a profundidade da Posição p."""
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))

    def _height2(self, p):
        """Calcula a altura da subárvore com raiz na Posição p."""
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self._height2(c) for c in self.children(p))

    def height(self, p=None):
        """Retorna a altura da subárvore com raiz na Posição p (ou da árvore inteira)."""
        if p is None:
            p = self.root()
        if p is None:
            return -1
        return self._height2(p)
    
#Exemplos

T = LinkedBinaryTree()
print("Árvore está vazia:", T.is_empty())

r = T._add_root('A')
print("Raiz adicionada:", r.element())

pB = T._add_left(r, 'B')
pC = T._add_right(r, 'C')
print("Filhos de A:", [p.element() for p in T.children(r)])

pD = T._add_left(pB, 'D')
pE = T._add_right(pB, 'E')

pF = T._add_right(pC, 'F')
print("Pai de F:", T.parent(pF).element())
print("Profundidade de F:", T.depth(pF))
print("Altura da Árvore:", T.height())

print("\nPercurso In-order (Elementos):", " -> ".join(T))

try:
    T._delete(pC)
    print("\nNó C removido com sucesso. Novo pai de F:", T.parent(pF).element())
except ValueError as e:
    print(f"\nErro ao deletar C: {e}")

print("Novo Percurso In-order (Elementos):", " -> ".join(T))
print("Novo tamanho da Árvore:", len(T))