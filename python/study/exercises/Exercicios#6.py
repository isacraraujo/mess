#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
def Circulo():
    diametro = float(input("Qual o raio do círculo? "))
    pi       = (3.14)
    area     = pi*diametro**2
    print("A área do círculo é equivalente à", area,"\n")
Circulo()