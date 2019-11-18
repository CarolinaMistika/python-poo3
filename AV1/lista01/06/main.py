'''
6. Faça um programa que converta da notação de 24 horas para a notação de 12 horas.
Por exemplo, o programa deve converter 14:25 em 2:25 P.M. A entrada é dada em
dois inteiros. Deve haver pelo menos duas funções: uma para fazer a conversão e uma
para a saída. Registre a informação A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para
P.M. Assim, a função para efetuar as conversões terá um parâmetro formal para
registrar se é A.M. ou P.M. Inclua um loop que permita que o usuário repita esse
cálculo para novos valores de entrada todas as vezes que desejar.
'''
continua = True

def Converte(horas,minutos):
    if horas == 24:
        horaConvertida = 0
        horas = 0
    elif horas <=12:
        horaConvertida = horas
    else:
        horaConvertida = horas-12
        
    amOuPm = "AM" if horas <12 else "PM"
    return str(horaConvertida)+":"+str(minutos)+amOuPm


	    
while (continua==True):
    horas=int(input("Digite a hora a ser convertida: "))
    minutos=int(input("Digite o minuto: "))
    print(Converte(horas,minutos))
    sair=int(input("Deseja sair? Digite 0 para sair e 1 para continuar"))
    if(sair==0):
        continua=False