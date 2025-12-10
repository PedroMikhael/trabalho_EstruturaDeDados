from ex1 import ArrayStack

def verificar_parentese(expr):
    abertura = '({['           
    fechamento = ')}]'          
    S = ArrayStack()
    
    for c in expr:
        if c in abertura:
            S.push(c)      
        elif c in fechamento:
            if S.is_empty():
                return False 
            if fechamento.index(c) != abertura.index(S.pop()):
                return False 
    
    return S.is_empty()     
if __name__ == '__main__':
    expressoes = [
        "[(5+x)-(y+z)]",     
        "((()(()){([()])}))", 
        ")((){([()])}",       
        "({[])}",             
        "("                  
    ]

    print("--- Verificador de Parênteses ---\n")
    for expr in expressoes:
        resultado = verificar_parentese(expr)
        status = "Correto" if resultado else "Incorreto"
        print(f"Expressão: {expr:<20} -> {status}")