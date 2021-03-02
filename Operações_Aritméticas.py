nome = str(input('Qual é o seu nome? '))
print('Prazer em conhecer {:^10}!'.format(nome))
print('Prazer em conhecer {:>10}!'.format(nome))
print('Prazer em conhecer {:<10}!'.format(nome))
print('Prazer em conhecer {:=^10}!'.format(nome))

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1+n2
m = n1*n2
d = n1+n2
di = n1//n2
p = n1**n2

print('A soma é {}, a multiplicação é {} e a divisão é {:.5f}!'.format(s, m, d))
# {:.5f} (float) indica que eu quero apenas que aparece 5 casas decimais de um número
print('A divisão integral é {} e a potência é {}!'.format(di, p))
