'''
1. Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-
Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.
'''
from semana import Semana

semana = []
semana.append(Semana(1,"Segunda"))
semana.append(Semana(2,"Terça"))
semana.append(Semana(3,"Quarta"))
semana.append(Semana(4,"Quinta"))
semana.append(Semana(5,"Sexta"))
semana.append(Semana(6,"Sabado"))
semana.append(Semana(7,"Domingo"))

num_semana = input('Entre com o dia da semana(1, 2...): ')
num_semana = int(num_semana) 
encontra = 0

for x in semana:
    if x.dia_semana == num_semana:
        encontra = 1
        print(x.get_semana)
        break
    
if encontra == 0:
    print("Valor invalido")