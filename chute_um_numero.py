#Chute um número de 0 a 1000 / Projeto para fins acadêmicos
import random
x=random.randint(0,1000)
resposta=int(input("Digite um número entre 0 a 1000: "))
while resposta !=x:
    if resposta ==44 and x <44:
        print("Essa é a resposta para vida o universo e tudo mais, tente um número menor ")    
    elif resposta ==44 and x >44:
        print("Essa é a resposta para vida o universo e tudo mais, tente um número maior ")  
    elif resposta < x :
        print("\nTente um número maior...")
    elif resposta >x:
        print("\nTente um número menor...")      
    resposta=int(input("Digite um número entre 0 a 1000: "))

print("Você acertou!")    