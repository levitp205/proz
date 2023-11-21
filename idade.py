def idadeIdade():
    nome = input("Qual é o seu nome: ")
    idade = input("Digite o ano que você nasceu: ")
    try:
        if int(idade) >= 1922 and int(idade) <= 2021:
            idade_atual = 2022 - int(idade)
            print(f'{nome} tem {idade_atual} anos!')
            breakpoint  
        else:
            print("Ano inválido!")
    except:
        print("Digite algo ou um cartacter válido!")
        

idadeReal = idadeIdade()
print(idadeReal)
       
                
        