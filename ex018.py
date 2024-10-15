import math
ang = float(input('Digite o valor do ângulo: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tg = math.tan(math.radians(ang))
print('O valor do seno é de {:.2f}, seu cosseno é {:.2f} e sua tangente é {:.2f}'.format(sen, cos, tg))