a = input("Digite algo: ")

print('O tipo primitivo desse valor é', type(a))
# Identifica qual a classe do valor.

print('É somente espaços?', a.isspace())
# Identifica se o comando só possui espaços. (ínutil)

print('É um número?', a.isnumeric())
# Identifica se é número.

print('É alfabético?', a.isalpha())
# Identifica se possui apenas letras.

print('É alfanumérico?', a.isalnum())
# Identifica se possui letras e números.

print('Esta em minúsculo?', a.islower())
# Identifica se possui apenas letras minúsculas.

print('Está em maiúscula?', a.isupper())
# Identifica se possui apenas letras maisúculas.

print('Está capitalizada?', a.istitle())
# Identifica se a palavra possui a primeira letra maiúscula e o restante minúscula