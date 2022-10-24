#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
#Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para
#o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#a. Salário bruto.
#b. Quanto pagou ao INSS.
#c. Quanto pagou ao sindicato.
#d. O Salário líquido.
#calcule os descontos e o salário líquido, conforme a tabela abaixo:
#+ Salário Bruto : R$
#- IR (11%) : R$
#- INSS (8%) : R$
#- Sindicato ( 5%) : R$
#= Salário Liquido : R$
def SaldoTrabalho():
    sal_hora  = float(input("Quanto você ganha por hora? "))
    horas_mes = float(input("Quantas horas você trabalhou no mês? "))
    return sal_hora, horas_mes
def SalarioBruto():
    teste  = SaldoTrabalho()
    print(teste)
#def ImpostoRenda():
   # ir      = ((sal_bru)/11/100)
#def INSS():
   # inss_d    = ((sal_bru)/8/100)
#def Sindicato():
  #  sind    = ((sal_bru)/5/100)
#def SalarioLiquido():

#def ContraCheque(SalarioBruto,ImpostoRenda,INSS,Sindicato,SaldoTrabalho,SalarioLiquido):
   # print("Seu contra cheque é de"+
    #       "Salário Bruto:",sal_bru, +
    #       "Sindicato:",sind, +
    #       "INSS:",inss_d, +
     #      "Salário Líquido:",)

SalarioBruto()