from ex1 import ArrayStack

S = ArrayStack()

S.push(5)
print(f"Pilha: {S._data}")

S.push(3)
print(f"Pilha: {S._data}")

S.pop()
print(f"Pilha: {S._data}")

S.push(2)
print(f"Pilha: {S._data}")

S.push(8)
print(f"Pilha: {S._data}")

S.pop()
print(f"Pilha: {S._data}")

S.pop()
print(f"Pilha: {S._data}")

S.push(9)
print(f"Pilha: {S._data}")

S.push(1)
print(f"Pilha: {S._data}")

S.pop()
print(f"Pilha: {S._data}")

S.push(7)
print(f"Pilha: {S._data}")

S.push(6)
print(f"Pilha: {S._data}")

S.pop()
print(f"Pilha: {S._data}")

S.pop()
print(f"Pilha: {S._data}")

S.push(4)
print(f"Pilha: {S._data}")

S.pop()
print(f"Pilha: {S._data}")

S.pop()
print(f"Pilha: {S._data}")

print("-" * 20)
print("Resultado Final da Pilha:", S._data)