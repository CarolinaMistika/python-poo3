'''
10. Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um
crime. As perguntas são:
a) "Telefonou para a vítima?"
b) "Esteve no local do crime?"
c) "Mora perto da vítima?"
d) "Devia para a vítima?"
e) "Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a participação da pessoa no
crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada
como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário,
ele será classificado como "Inocente".
'''
print('**************** JOGO DO DETETIVE ********************')
print('reponda 1 para sim e 0 para não ')
count = 0
resposta = int(input('Telefonou para a vítima?: '))
if resposta == 1:
  count += 1

resposta = int(input('Esteve no local do crime?: '))
if resposta == 1:
  count += 1

resposta = int(input('Mora perto da vítima?: '))
if resposta == 1:
  count += 1

resposta = int(input('Devia para a vítima?: '))
if resposta == 1:
  count += 1

resposta = int(input('Já trabalhou com a vítima?: '))
if resposta == 1:
  count += 1

if count == 2:
  print('Suspeito(a)')
if count == 3 or count == 4:
  print('Cúmplice')
if count == 5:
  print('Assassino')
else:
  print('Inocente')