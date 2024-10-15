import random
a1 = input('Qual o nome do primeiro aluno? ')
a2 = input('Qual o nome do segundo aluno? ')
a3 = input('Qual o nome do terceiro aluno? ')
a4 = input('Qual o nome do quarro aluno? ')
ae = [a1, a2, a3, a4]
(random.shuffle(ae))
print('A ordem de apresentação será ')
print(ae)