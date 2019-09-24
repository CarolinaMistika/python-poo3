'''
9. Elabore um procedimento que recebe por parâmetro o tempo de produção de uma
peça expresso em segundos e apresente o tempo em horas, minutos e segundos.
'''

segundos = int(input('Digite o tempo em segundos: '))
horas = int(segundos/3600)
minutos = int((segundos - (horas * 3600))/60)
novos_segundos = int(segundos%60)
return str(horas)+'h:'+str(minutos)+'m:'+str(novos_segundos)+'s'