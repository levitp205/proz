
def soma(x,y):
    return x + y

def subtracao(x,y):
    return x - y

def multiplicacao(x,y):
    return x * y

def divisao(x,y):
    return x / y


def calculadora():
    while True:
        print("Escolha a operação:")
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("0. Sair")
        

        operacao = input("Digite o número da opração desejada: ")
        if operacao == '0':
            print("Saindo...") 
            break
        elif operacao in ('1', '2', '3','4'):
            num1 = int(input("Digite o primeiro número:  "))
            num2 = int(input("Digite o segundo número: "))      
        if operacao == '1':
            soma = num1 + num2
            print(f'Resultado: {num1} + {num2} = {soma}')
        elif operacao == '2':
            soma = num1 - num2
            print(f'Resultado: {num1} - {num2} = {soma}')    
        elif operacao == '3':
            soma = num1 * num2
            print(f'Resultado: {num1} * {num2} = {soma}')  
        elif operacao == '4':
            soma = num1 - num2
            print(f'Resultado: {num1} / {num2} = {soma}') 
        else:      
            print("Esta opração não exite...tente novamente!") 

cal =calculadora() 
print(cal)     