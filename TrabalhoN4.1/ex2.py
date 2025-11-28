class ArrayBinaryTree:
    """Implementa o TAD BinaryTree usando a representação baseada em array (lista Python)."""
    class Position:
        """Abstração representando a localização de um único elemento (seu índice no array)."""

        def __init__(self, container, index):
            self._container = container
            self._index = index

        def element(self):
            """Retorna o elemento armazenado nesta Posição."""
            return self._container._data[self._index]

        def __eq__(self, other):
            """Retorna True se 'other' representa o mesmo local (mesmo índice)."""
            return type(other) is type(self) and other._index == self._index
            
        def __ne__(self, other):
            return not (self == other)

    
    def _validate(self, p):
        """Retorna o índice associado, se a posição for válida."""
        if not isinstance(p, self.Position):
            raise TypeError('p deve ser um tipo Position adequado')
        if p._container is not self:
            raise ValueError('p não pertence a este container')
        
        if not (0 <= p._index < len(self._data) and self._data[p._index] is not None):
             raise ValueError('p é um índice inválido ou está vazio')
        return p._index

    def _make_position(self, index):
        """Retorna a instância Position para um dado índice (ou None se não houver elemento no índice)."""
        if index < 0 or index >= len(self._data) or self._data[index] is None:
            return None
        return self.Position(self, index)
    
    def __init__(self, capacity=1000):
        """Cria uma árvore binária com uma capacidade de array predefinida."""
        self._data = [None] * capacity  
        self._size = 0  
        self._capacity = capacity

    def __len__(self):
        """Retorna o número total de elementos (nós) na árvore."""
        return self._size

    def is_empty(self):
        """Retorna True se a árvore estiver vazia."""
        return len(self) == 0

    def root(self):
        """Retorna a Posição raiz (índice 0)."""
        return self._make_position(0)

    def parent(self, p):
        """Retorna a Posição do pai de p: (i-1) // 2."""
        index = self._validate(p)
        if index == 0:
            return None
        return self._make_position((index - 1) // 2)

    def left(self, p):
        """Retorna a Posição do filho esquerdo de p: 2i + 1."""
        index = self._validate(p)
        left_index = 2 * index + 1
        return self._make_position(left_index)

    def right(self, p):
        """Retorna a Posição do filho direito de p: 2i + 2."""
        index = self._validate(p)
        right_index = 2 * index + 2
        return self._make_position(right_index)

    def num_children(self, p):
        """Retorna o número de filhos de Posição p."""
        count = 0
        if self.left(p) is not None:
            count += 1
        if self.right(p) is not None:
            count += 1
        return count
    
    def is_root(self, p):
        """Retorna True se a Posição p representa a raiz (índice 0)."""
        return self._validate(p) == 0

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
        """Retorna a Posição do irmão de p."""
        parent = self.parent(p)
        if parent is None:
            return None  
        
        if p == self.left(parent):
            return self.right(parent)
        else:
            return self.left(parent)
    
    def depth(self, p):
        """Calcula a profundidade da Posição p."""
        index = self._validate(p)
        d = 0
        while index > 0:
            index = (index - 1) // 2 
            d += 1
        return d

    def _height2(self, p):
        """Calcula a altura da subárvore com raiz na Posição p (recursivamente)."""
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self._height2(c) for c in self.children(p))

    def height(self, p=None):
        """Retorna a altura da árvore/subárvore."""
        if p is None:
            p = self.root()
        if p is None or self.is_empty():
            return -1
        return self._height2(p)

    def __iter__(self):
        """Gera uma iteração dos elementos (usando percurso in-order por padrão)."""
        for p in self.positions(): 
            yield p.element()

    def positions(self):
        """Gera uma iteração das posições da árvore (In-order)."""
        for i in range(len(self._data)):
            if self._data[i] is not None:
                yield self.Position(self, i)
        
    
    def _set_element(self, index, e):
        """Auxiliar que garante a alocação do elemento e atualiza o tamanho (size)."""
        if index >= self._capacity:
            raise IndexError('Capacidade do array da árvore excedida.')
        
        if self._data[index] is None:
            self._size += 1 
            
        self._data[index] = e
        return self._make_position(index)
        
    def _add_root(self, e):
        """Coloca o elemento e na raiz (índice 0)."""
        if not self.is_empty():
            raise ValueError('Existe raiz')
        return self._set_element(0, e)

    def _add_left(self, p, e):
        """Cria um novo filho esquerdo para a Posição p no índice 2i + 1."""
        index = self._validate(p)
        left_index = 2 * index + 1
        if left_index >= self._capacity or self._data[left_index] is not None:
            raise ValueError('Filho esquerdo existe ou capacidade excedida')
        return self._set_element(left_index, e)

    def _add_right(self, p, e):
        """Cria um novo filho direito para a Posição p no índice 2i + 2."""
        index = self._validate(p)
        right_index = 2 * index + 2
        if right_index >= self._capacity or self._data[right_index] is not None:
            raise ValueError('Filho direito existe ou capacidade excedida')
        return self._set_element(right_index, e)

    def _replace(self, p, e):
        """Substitui o elemento na posição p por e."""
        index = self._validate(p)
        old = self._data[index]
        self._data[index] = e
        return old

    def _delete(self, p):
        """Remove um nó (funcionalidade limitada devido à ineficiência inerente da representação em array)."""
        index = self._validate(p)
        
        if self.num_children(p) > 0:
            raise ValueError("Não é possível deletar nós internos com filhos sem reestruturação complexa (O(n) na representação em array).")

        old_element = self._data[index]
        self._data[index] = None
        self._size -= 1
        return old_element
    
    def _attach(self, p, t1, t2):
        """Operação complexa e ineficiente na representação em array, omitida por brevidade e ineficiência."""
        raise NotImplementedError('Operação _attach não é eficiente ou trivial na ArrayBinaryTree.')
    

#Exemplos

T = ArrayBinaryTree(capacity=10) 

r = T._add_root('A') 

pB = T._add_left(r, 'B')
pC = T._add_right(r, 'C')

pD = T._add_left(pB, 'D')
pE = T._add_right(pB, 'E')

pF = T._add_left(pD, 'F') 

print("=== Demonstração da ArrayBinaryTree (Ex. 2) ===")
print("Estrutura do Array (elementos e índices):")
for i, el in enumerate(T._data):
    if el is not None:
        print(f"  Índice {i}: {el} (Profundidade: {T.depth(T._make_position(i))})")

print(f"\nNúmero total de nós (size): {len(T)}")
print(f"Capacidade total do Array: {len(T._data)}")
print(f"Acessando Pai de F ('F' está no índice 7): {T.parent(pF).element()}")

print(f"\nPercurso do Array (Positions): {' -> '.join(T)}") 
print(f"Altura da Árvore: {T.height()}")