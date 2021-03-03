largura = float(input('Largura da parede: '))
comprimento = float(input('Comprimento da parede: '))
area = largura * comprimento
tinta = area / 2

print('Sua parede tem dimensão de {} x {} e sua area é de {} m quadrados.'.format(largura, comprimento, area))
print('Para pintar a sua parede, será necessário comprar {} litros de tinta!'.format(tinta))
