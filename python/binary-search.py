lista = [1,2,3,4,5,6,7,8,9,10]
lista.sort()
first = 0
last  = len(lista)-1
mid   = (first+last)//2
item  = int(input("Insira um número para pesquisar: \n"))
found = False

while first<=last and not found:
    mid = (first + last)//2
    if lista[mid] == item:
        print(f"Encontrei a localização {mid}")
        found = True
    else:
        if item < lista[mid]:
            last  = mid - 1
        else:
            first = mid + 1
if found == False:
    print("Número não encontrado!")