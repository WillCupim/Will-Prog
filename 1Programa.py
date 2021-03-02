import random
A1 = str(input('Primeiro Aluno: '))
A2 = str(input('Segundo Aluno: '))
A3 = str(input('Terceiro Aluno: '))
A4 = str(input('Quarto Aluno: '))
lista = [A1, A2, A3, A4]
random.shuffle(lista)
print('A ordem de aprensentação é: ')
print(lista)