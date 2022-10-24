#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
#utilizando as seguintes fórmulas:
#A. Para homens: (72.7*h) - 58
#B. Para mulheres: (62.1*h) - 44.7
def PesoIdeal():
    h      = float(input("Digite sua altura: "))
    homem  = (72.7*h)-58
    mulher = (62.1*h)-44.7
    print("Seu peso ideal na estutura masculina é", homem,". E na feminina é",mulher)

PesoIdeal()