import random

question = input('Desea lanzar los dados [y/n]?\n')
sum = 0
while question != 'n':
    if question == 'y':
        diceRes1 = random.randint(1, 6)
        diceRes2 = random.randint(1, 6)
        sum = diceRes1 + diceRes2
        print("Resultado: ", diceRes1, diceRes2)
        print("Suma: ", sum)
        question = input('Desea lanzar los dados [y/n]?\n')
    else:
        print('IRespuesta inválida. Por favor escriba "y" or "n".') 
        question = input('Desea lanzar los dados [y/n]?\n')      

print('Good-bye!')