def idadeIdade():
    nome = input("Qual é o seu nome: ")
    
    executar = True
    
    while(executar == True):
        print("Digite seu ano de nascimento: ")
        try:
            ano = int(input())
            if (ano < 1922) or (ano > 2021):
                print('O ano precisa ser entre 1922 e 2021') 
            else:
                idade = 2022 - ano
                print(f"O usuário {nome}, completou ou completará {idade} anos de idade em 2022")
                executar = False
        except:
            print("Os anos precisan ser escritos somente por números")
            

idadeReal = idadeIdade()
print(idadeReal)
       
                
        