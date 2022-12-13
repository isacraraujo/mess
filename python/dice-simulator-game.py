import random

while True:
    print('1. Roll the Dice\n',
            '2. Exit')
    user = input("O que você quer fazer?\n")
    if user==1:
        number = random.randint(1,6)
        print('\nO número é: ',number,'\n')
    else:
        print('Você saiu!')
        break