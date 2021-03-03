nome = input('Digite o seu nome: ')
peso = float(input('Digite seu peso em KG: '))
altura = float(input('Digite sua altura em M: '))
imc = float(peso / (altura * altura))
print('Seu IMC é: {:.2f}'.format(imc))
if imc < 20:
    print('{} está abaixo do peso!'.format(nome))
elif (imc > 20) and (imc < 25):
    print('{} está com o peso normal!'.format(nome))
elif (imc > 30) and (imc < 35):
    print('{} está com excesso de peso!'.format(nome))
elif imc > 35:
    print('{} está com obesidade mórbida!'.format(nome))
