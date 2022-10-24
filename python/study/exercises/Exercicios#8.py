#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês.
def Salario():
    sal_hora  = float(input("Quanto você ganha por hora? "))
    horas_mes = float(input("Quantas horas você trabalhou no mês? "))
    total_sal = sal_hora*horas_mes
    print("Seu salário desse mês é de",total_sal,"reais\n")
Salario()

#EXTRA I: Faça um programa que o usuário informa o salário e quantas horas ele trabalhou no mês.
#Calcule quanto ele ganhou em cada dia.
def SalarioDiario():
    sal_mes   = float(input("Quanto você ganhou esse mês? "))
    horas_mes = float(input("Quantas horas você trabalhou no mês? "))
    total_dia = sal_mes/horas_mes
    print("Você ganhou",total_dia,"reais por dia trabalhado\n")
SalarioDiario()

#EXTRA II: Faça um programa que o usuário informa o salário mensal e o salário diário
#Calcule as horas feitas no mês
def BancoDeHoras():
    sal_mes   = float(input("Quanto você ganhou esse mês? "))
    horas_dia = float(input("Quanto você ganha por hora? "))
    total_hrs = sal_mes/horas_dia
    print("Seu banco de horas é de",total_hrs,"\n")
BancoDeHoras()