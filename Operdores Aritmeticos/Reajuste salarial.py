sal = float(input('Digite o seu salário atual: R$'))
aum = float(sal + (sal * 0.15))
print('Um funcionário que ganhava R${:.2f}, com o reajuste de 15%, passou a receber R${:.2f}!'.format(sal, aum))
