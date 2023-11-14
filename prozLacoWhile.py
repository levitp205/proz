# Precisamos imprimir um número para cada andar de um 
# hotel de 20 andares. Porém, o dono do hotel é supersticioso
# e optou por não ter um 13ro andar.
# Escreva um código que imprima todos os números exceto
# o número 13.
# Escreva mais um código que resolva o mesmo problema, 
# mas dessa vez usando o laço de repetição 'while'.

# Como desafio, imprima eles em ordem decrescente 
# (20, 19, 18...)

import time
# andar = 20
# while andar > -1:
#     if andar != 13:
#         print(f"{andar}° andar")
#     andar -= 1
#     time.sleep(1)
# print("Este prédio não possui o 13° andar") 

andar = 20
while andar > -1:
    if andar == 13:
       andar -= 1
       continue
    else:
        print(f"{andar}° andar")
        andar -= 1
    time.sleep(1)
print("Este prédio não possui o 13° andar") 