class LinkedBinaryTree:
    class _Node:
        __slots__ = '_element', '_parent', '_left', '_right'
        def __init__(self, element, parent=None, left=None, right=None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right

    class Position:
        def __init__(self, container, node):
            self._container = container
            self._node = node
        def element(self):
            return self._node._element
        def __eq__(self, other):
            return type(other) is type(self) and other._node is self._node
        def __ne__(self, other):
            return not (self == other)

    def _validate(self, p):
        if not isinstance(p, self.Position): raise TypeError('p deve ser um tipo Position adequado')
        if p._container is not self: raise ValueError('p não pertence a este container')
        if p._node._parent is p._node: raise ValueError('p não é mais válido')
        return p._node

    def _make_position(self, node):
        return self.Position(self, node) if node is not None else None

    def __init__(self):
        self._root = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return len(self) == 0

    def root(self):
        return self._make_position(self._root)

    def parent(self, p):
        node = self._validate(p)
        return self._make_position(node._parent)

    def left(self, p):
        node = self._validate(p)
        return self._make_position(node._left)

    def right(self, p):
        node = self._validate(p)
        return self._make_position(node._right)

    def num_children(self, p):
        node = self._validate(p)
        count = 0
        if node._left is not None: count += 1
        if node._right is not None: count += 1
        return count
    
    def is_root(self, p): return self.root() == p
    def is_leaf(self, p): return self.num_children(p) == 0

    def children(self, p):
        if self.left(p) is not None: yield self.left(p)
        if self.right(p) is not None: yield self.right(p)

    def sibling(self, p):
        parent = self.parent(p)
        if parent is None: return None
        if p == self.left(parent): return self.right(parent)
        else: return self.left(parent)

    def _add_root(self, e):
        if self._root is not None: raise ValueError('Root exists')
        self._size = 1
        self._root = self._Node(e)
        return self._make_position(self._root)

    def _add_left(self, p, e):
        node = self._validate(p)
        if node._left is not None: raise ValueError('Left child exists')
        self._size += 1
        node._left = self._Node(e, node)
        return self._make_position(node._left)

    def _add_right(self, p, e):
        node = self._validate(p)
        if node._right is not None: raise ValueError('Right child exists')
        self._size += 1
        node._right = self._Node(e, node)
        return self._make_position(node._right)

    def _replace(self, p, e):
        node = self._validate(p)
        old = node._element
        node._element = e
        return old

    def _delete(self, p):
        node = self._validate(p)
        if self.num_children(p) == 2: raise ValueError('p has two children')
        child = node._left if node._left else node._right
        if child is not None: child._parent = node._parent
        if node is self._root: self._root = child
        else:
            parent = node._parent
            if node is parent._left: parent._left = child
            else: parent._right = child
        self._size -= 1
        node._parent = node
        return node._element

    def _attach(self, p, t1, t2):
        node = self._validate(p)
        if not self.is_leaf(p): raise ValueError('position must be leaf')
        if not type(self) is type(t1) is type(t2): raise TypeError('Tree types must match')
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
        for p in self.positions(): yield p.element()

    def positions(self):
        return self.inorder()

    # Percurso Pré-ordem (Preorder Traversal): Raiz -> Esquerda -> Direita
    def preorder(self):
        if not self.is_empty():
            for p in self._subtree_preorder(self.root()):
                yield p
    
    def _subtree_preorder(self, p):
        yield p
        if self.left(p) is not None:
            for other in self._subtree_preorder(self.left(p)):
                yield other
        if self.right(p) is not None:
            for other in self._subtree_preorder(self.right(p)):
                yield other

    # Percurso Em-ordem (Inorder Traversal): Esquerda -> Raiz -> Direita
    def inorder(self):
        if not self.is_empty():
            for p in self._subtree_inorder(self.root()):
                yield p

    def _subtree_inorder(self, p):
        if self.left(p) is not None:
            for other in self._subtree_inorder(self.left(p)):
                yield other
        yield p
        if self.right(p) is not None:
            for other in self._subtree_inorder(self.right(p)):
                yield other

    # Percurso Pós-ordem (Postorder Traversal): Esquerda -> Direita -> Raiz
    def postorder(self):
        if not self.is_empty():
            for p in self._subtree_postorder(self.root()):
                yield p
    
    def _subtree_postorder(self, p):
        if self.left(p) is not None:
            for other in self._subtree_postorder(self.left(p)):
                yield other
        if self.right(p) is not None:
            for other in self._subtree_postorder(self.right(p)):
                yield other
        yield p

    def depth(self, p):
        if self.is_root(p): return 0
        else: return 1 + self.depth(self.parent(p))
    def _height2(self, p):
        if self.is_leaf(p): return 0
        else: return 1 + max(self._height2(c) for c in self.children(p))
    def height(self, p=None):
        if p is None: p = self.root()
        if p is None: return -1
        return self._height2(p)
    

def build_demo_tree(cls=LinkedBinaryTree):
    T = cls()
    r = T._add_root(1)
    p2 = T._add_left(r, 2)
    p3 = T._add_right(r, 3)
    T._add_left(p2, 4)
    T._add_right(p2, 5)
    T._add_left(p3, 6)
    T._add_right(p3, 7)
    return T

T = build_demo_tree()

#Exemplos de uso dos percursos
#      1
#     / \
#    2   3
#   / \ / \
#  4  5 6  7

print("Preorder:  ", " -> ".join(str(p.element()) for p in T.preorder()))
print("Inorder:   ", " -> ".join(str(p.element()) for p in T.inorder()))
print("Postorder: ", " -> ".join(str(p.element()) for p in T.postorder()))