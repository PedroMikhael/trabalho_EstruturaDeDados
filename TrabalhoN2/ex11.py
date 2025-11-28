from ex1 import ArrayStack, ArrayQueue

def is_palindrome(s):
    stack = ArrayStack()
    queue = ArrayQueue()

    for char in s:
        if char.isalnum():
            lower_char = char.lower()
            stack.push(lower_char)
            queue.enqueue(lower_char)

    while not stack.is_empty() and not queue.is_empty():
        if stack.pop() != queue.dequeue():
            return False
    
    return stack.is_empty() and queue.is_empty()

if __name__ == '__main__':
    strings = [
        "arara",
        "A man a plan a canal Panama",
        "racecar",
        "hello world",
        "Was it a car or a cat I saw?"
    ]

    print("--- Verificador de Palíndromos ---\n")
    for s in strings:
        resultado = "É palíndromo" if is_palindrome(s) else "NÃO é palíndromo"
        print(f"'{s}' -> {resultado}")