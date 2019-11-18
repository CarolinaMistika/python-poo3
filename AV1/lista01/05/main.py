'''
5. Faça um programa que receba duas listas A e B de 6 posições e calcule a lista C que
contem na sua primeira posição a subtração do primeiro elemento de A e o último de B,
na segunda posição o segundo elemento de A e o penúltimo elemento de B e assim
por diante até que todos os elementos de C sejam preenchidos.

'''

A = []
B = []
C = []
i = 0
qtde = 3

print('**************** CADASTRO DE 4 NUMEROS INTEIROS PARA LISTA A E B *****************')

while(i <= qtde):
    
    print('**************** Cadastro de numero n° ',i+1,' *****************')

    numero = int(input('Digite um número inteiro para a lista A:'))
    A.append(numero)

    numero = int(input('Digite um número inteiro para a lista B:'))
    B.append(numero)

    i += 1

i = 0

while(i <= qtde):

    index = (len(B) - (i+1) )
    print(index)

    C.append(A[i] + B[index])
    i += 1


print('Numeros lista A: ',A)

print('Numeros lista B: ',B)

print('Numeros lista C: ',C)