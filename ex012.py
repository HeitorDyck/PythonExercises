p = float(input('Qual é o preço do produto?'))
d = (p * 0.05)
np = (p - d)
print("O desconto do produto cujo preço é {}, é {:.2f}. O novo preço é {:.2f}".format(p, d, np))