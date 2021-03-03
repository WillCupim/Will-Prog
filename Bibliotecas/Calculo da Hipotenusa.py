#Programa para calcular o comprimento da hipotenusa, usando bibliotecas.

from math import sqrt, trunc
co = float(input('Digite o valor do C.O: '))
ca = float(input('Digite o valor do C.A: '))
coca = (co**2) + (ca**2)
hip = sqrt(coca)
print('Se C.O é {} e o C.A é {}, o valor da Hipotenusa será {:.2f}'.format(co, ca, hip))
