#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#a. o produto do dobro do primeiro com metade do segundo .
#b. a soma do triplo do primeiro com o terceiro.
#c. o terceiro elevado ao cubo.
def Math():
    valor1 = int(input("Insira um número inteiro: "))
    valor2 = float(input("Insira um número real: "))
    
    calc1  = ((valor1*2)+valor2/2)
    calc2  = ((valor1*3)+calc1)
    calc3  = calc1 **(1/3)
    print("Letra A é igual a",calc1)
    print("Letra B é igual a",calc2)
    print("Letra C é igual a",calc3)

Math()