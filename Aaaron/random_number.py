import random

# def guess(x):
#     random_number = random.randint(1,x)
#     guess = 0
#     while guess != random_number:
#         guess = int(input(f'Guess the number betwee 1 and {x}: '))
#         if guess < random_number:
#             print('Sorry, guess again. Too low.')
#         elif guess > random_number:
#             print('Sorry, guess again. Too high.')
#     print('Yay, congrats. You have guessed the number.')
# guess(5)


# def cara_del_dado():
#     print('\n------El juego del dado------\n\nRegla:\n-    Si falla el dado se gira nuevamente a otra cara.\n-    Tome en cuenta que el dado tiene 6 caras.\n')
#     guess = 1
#     cara_del_dado = 0
    
#     while guess != cara_del_dado:
#         guess = int(input('Escriba el número que cree que va a salir: '))
#         cara_del_dado = random.randint(1,6)
#         if guess != cara_del_dado:
#             print('\nEl dado acaba de girar...')
#             print(f'La cara del dado es: {cara_del_dado} y usted escribió el {guess}, intente nuevamente.\n--------------------------------\n')
#         elif guess == cara_del_dado:
#             print(f'Cara del dado adivinada. CONTRATULATIONS!!!!!!!!\n{cara_del_dado} == {guess}')
# cara_del_dado()

# Uno le especifica que es alto o bajo.
# Conforme a eso 

def computadora_pregunta():
    print('\nJuguemos a que la computadora adivine el número que usted elije.\n')
    guess = int(input('Escriba el número que la computadora quiere que adivne: '))
    numero1 = int(input('Entre qué rango se encuentra el número que tengo que adivinar?\n\nEstá entre el número: '))
    numero2 = int(input('Y el número: '))
    computadora = -1

    while guess != computadora:
        computadora = random.randint(numero1,numero2)
        print(f'La computadora cree que el número es: {computadora}')
        if computadora != guess:
            print(f'La computadora se equivoca, intentando otra vez...\n')
        elif computadora == guess:
            print(f'La computadora adivinó!!!!!!!\n\n----Fin del programa.----')
computadora_pregunta()            
    