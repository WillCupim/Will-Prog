import math
an = float(input('Digite um ângulo: '))
seno = math.sin(math.radians(an))
print('O ângulo de {} tem seno de {:.2f}'.format(an, seno))
cosseno = math.cos(math.radians(an))
print('O ângulo de {} tem cosseno de {:.2f}'.format(an, cosseno))
tangente = math.tan(math.radians(an))
print('O ângulo de {} tem tangente de {:.2f}'.format(an, tangente))
