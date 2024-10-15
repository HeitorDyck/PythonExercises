#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date

atual = date.today().year
totalmaior = 0
totalmenor = 0

for pessoa in range(1,8):
    nasc = int(input('Digite o ano de nascimento da pessoa: '))
    idade = atual - nasc
    if idade >= 18:
        totalmaior += 1
    else:
        totalmenor += 1

print('Ao todo tivemos {} pessoas maiores de idade'.format(totalmaior))
print('Tivemos, também, {} menores de idade'.format(totalmenor))