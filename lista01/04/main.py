'''
4. Elabore um programa que solicite ao usuário 15 valores inteiros, e um intervalo [x,y]. E
apresente:
a) A quantidade e os números pares no intervalo;
b) A soma dos números ímpares.

'''
numero_par = []
numero_impar = []
soma_numero_impar = 0
i = 0

print('**************** CADASTRO DE 15 NUMEROS INTEIROS no intervalo de 1 a 100 *****************')

while(i <= 14):
    
    print('**************** Cadastro de numero n° ',i+1,' *****************')

    numero = int(input('Digite um número inteiro:'))

    if numero >= 1 and numero <= 100:
        resto = numero % 2

        if resto == 0:
            numero_par.append(numero)
        else:
            numero_impar.append(numero)
        i += 1
    else:
        print('**************** Numero invalido! *****************')

for x in numero_impar:    
    soma_numero_impar += x

print('Foi realizado um cadastro de ',i+1,' numeros')

print('Numeros par: ',numero_par)

print('Soma de numeros impar: ',soma_numero_impar)


