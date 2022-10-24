#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit.
def ConversorCels():
    cels = float(input("Qual a temperatura em Celsius? "))
    convC = ((cels*9/5)+32)
    print("A temperatura em Fahreinheit é de",convC)
ConversorCels()