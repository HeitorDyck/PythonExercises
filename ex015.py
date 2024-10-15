km = float(input('Quantos quilômetros você percorreu?'))
dias = int(input('Quantos dias se passaram?'))
p = (dias * 60) + (km * 0.15)
print('O preço a se pagar pelo aluguel do carro é de R${}'.format(p))