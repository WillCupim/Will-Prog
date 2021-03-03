real = float(input('Quanto dinheiro você tem na sua carteira? '))
dolar = float(real / 3.27)
print('Com R${:.2f} você pode comprar US${:.2f}!'.format(real, dolar))
