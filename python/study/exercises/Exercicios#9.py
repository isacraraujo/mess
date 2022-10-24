#Faça um Programa que peça a temperatura em graus Farenheit.
#Transforme e mostre a temperatura em graus Celsius.
def ConversorFahr():
    fahr = float(input("Qual a temperatura em Fahrenheit? "))
    convF = ((fahr - 32)*5/9)
    print("A temperatura em Celsius é de",convF)
#ConversorFahr()


