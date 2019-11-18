'''
7. Faça um programa para imprimir:
1
2 2
3 3 3
.....
n n n n n n ... n
para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima
até a n-ésima linha.
'''


valor = int(input('Informe um numero: '))
for i in range(1, valor + 1):
    print(('%s '%i)*i)