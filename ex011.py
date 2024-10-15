#Faça um programa que leia a largura e a altura de uma parede em metros
#Calcule a sua área e a quantidade de tinta necessária para pintá-la
#Sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

l = float(input('Qual a largura da parede?'))
h = float(input('Qual a altura da parede?'))
a = (h * l)
print('Uma parede de {} metros de largura e {} metros de altura, cuja área é de {} metros quadrados, gasta {} litros de tinta'.format(l, h, a,(a/2)))