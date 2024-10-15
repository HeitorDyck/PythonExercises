#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
p_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Dê a razão dessa P.A.: '))
pa = 0
print(p_termo)
for c in range(0, 10):
    p_termo += razao
    print(p_termo)