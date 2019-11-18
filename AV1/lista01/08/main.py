'''
8. Escreva uma função que recebe por parâmetro um valor inteiro e positivo N e retorna
o valor de S.
S = 1 + 1⁄2 + 1/3 + 1⁄4 + 1/5 + 1/N.
'''

valor = int(input('Informe um valor para S: '))
soma = 0
for i in range (1, valor+1):
    soma += 1/i

print("O total de S : ", soma)