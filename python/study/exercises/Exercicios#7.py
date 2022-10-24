#Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
def Quadrado():
    lado     = float(input("Qual o valor equivalente ao lado do quadrado? "))
    area     = lado * lado
    dob_area = area*2
    print("A área do quadrado equivale à",area,"e o dobro da área equivale à",dob_area,"\n")
Quadrado()