lista_de_numeros =[12,15,7,9,27,34]
achou = False
n = int(input("Digite o número a procurar: "))
x = 0
while (x < len (lista_de_numeros)):
    if (lista_de_numeros[x] == n):
        achou = True
        posicao = x
    x += 1
if (achou):
    print(f"{n} achado na posição {posicao}")
else:
    print(f"{n} não encontrado")
    
