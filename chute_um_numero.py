#Chute um número de 0 a 1000 / Projeto para fins acadêmicos 
import random
x=random.randint(0,1000)
resposta=int(input("Digite um número entre 0 a 1000: "))
while resposta !=x:
    if resposta<x:
        print("\nTente um número menor...")
    elif resposta>x:
        print("\nTente um número maior...")
    elif resposta<0 or resposta>1000:
        print("Escolha um número entre 0 e 1000")
    resposta=int(input("Digite um número entre 0 a 1000: "))
else:
    print("Você acertou!")        