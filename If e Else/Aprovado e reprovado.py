aluno = input('Nome do aluno: ')
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = float((nota1 + nota2) / 2)

print('{} tirou na primeira prova nota {} e na segunda prova nota {}. \nSendo assim, sua média final é {}!'.format(aluno, nota1, nota2, media))

if media >= 7:
    print('{} passou de ano!!'.format(aluno))
else:
    print('{} reprovou !!'.format(aluno))
    