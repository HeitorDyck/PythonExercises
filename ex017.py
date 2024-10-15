import math
co = int(input('Qual o comprimento do cateto oposto?'))
ca = int(input('Qual o comprimento do cateto adjacente?'))
h = math.hypot(co, ca)
print('A Hipotenusa vale {}'.format(h))