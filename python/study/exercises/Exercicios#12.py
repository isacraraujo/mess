#Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal,
# usando a seguinte fórmula: (72.7*altura) - 58
def Estatura():
    altura  = float(input("Qual sua altura? "))
    formula = (72.7*(altura)-58)
    print(formula)
Estatura()

#Fórmula original do IMC
def IMC():
    altura1  = float(input("Qual sua altura? "))
    peso1    = float(input("Quanto você está pesando? "))
    formula1 = (peso1/altura1**2)
    print(formula1)
IMC()