class Empty(Exception):
    pass

class ArrayStack:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, e):
        self._data.append(e)

    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()

class ArrayQueue:
    DEFAULT_CAPACITY = 10

    def __init__(self):
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[self._front]

    def dequeue(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        if 0 < self._size < len(self._data) // 4:
             self._resize(len(self._data) // 2)
        return answer

    def enqueue(self, e):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def _resize(self, cap):
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old)
        self._front = 0

class ArrayDeque(ArrayQueue):
    def last(self):
        if self.is_empty():
            raise Empty("Deque is empty")
        back = (self._front + self._size - 1) % len(self._data)
        return self._data[back]

    def delete_first(self):
        return self.dequeue()

    def add_last(self, e):
        self.enqueue(e)

    def add_first(self, e):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        self._front = (self._front - 1) % len(self._data)
        self._data[self._front] = e
        self._size += 1

    def delete_last(self):
        if self.is_empty():
            raise Empty("Deque is empty")
        back = (self._front + self._size - 1) % len(self._data)
        answer = self._data[back]
        self._data[back] = None
        self._size -= 1
        if 0 < self._size < len(self._data) // 4:
             self._resize(len(self._data) // 2)
        return answer

if __name__ == '__main__':
    print("--- Teste ArrayStack ---")
    S = ArrayStack()
    S.push(5)
    S.push(3)
    print(f"Tamanho da pilha: {len(S)}")
    print(f"Topo da pilha: {S.pop()}")
    print(f"Pilha vazia? {S.is_empty()}")
    print(f"Topo da pilha: {S.pop()}")
    print(f"Pilha vazia? {S.is_empty()}")

    print("\n--- Teste ArrayQueue ---")
    Q = ArrayQueue()
    Q.enqueue(5)
    Q.enqueue(3)
    print(f"Tamanho da fila: {len(Q)}")
    print(f"Primeiro da fila (removido): {Q.dequeue()}")
    print(f"Fila vazia? {Q.is_empty()}")
    print(f"Primeiro da fila (removido): {Q.dequeue()}")
    print(f"Fila vazia? {Q.is_empty()}")

    print("\n--- Teste ArrayDeque ---")
    D = ArrayDeque()
    D.add_first(3)
    D.add_last(7)
    print(f"Primeiro do deque: {D.first()}")
    print(f"Último do deque: {D.last()}")
    print(f"Removendo o primeiro: {D.delete_first()}")
    print(f"Removendo o último: {D.delete_last()}")
    print(f"Deque vazio? {D.is_empty()}")