#João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento
# diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo
# regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente.
# João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso.
# Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa
# que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

#limite de 50 kg
#excedendo, multa de 4 reais por kg

def PeixeKG():
    peixe = float(input("Insira o total em kg de peixes: "))
    if peixe <= 50:
        print("Você não pagará multa")
    elif peixe >= 50:
        multa = (4*(peixe-50))
        print("Você excendeu o limite, a multa será de",multa,"reais")
PeixeKG()