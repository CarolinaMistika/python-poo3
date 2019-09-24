'''
3. Apresente um programa que receba o nome e endereço (nome da rua e número da
casa/ap) de 5 pessoas e acrescente essas informações em dois vetores independentes,
um para os nomes e outro para os endereços.
'''


from endereco import Endereco
from pessoa import Pessoa

endereco = []
pessoa = []
i = 1

while(i <= 5):
    print('**************** Cadastro de Pessoa n° ',i,' *****************')
    nome = input('Digite o seu nome: ')
    logradouro = input('Digite o logradouro: ')
    numero = input('Digite o numero do logradouro: ')
    complemento = input('Digite o seu complemento: ')
    bairro = input('Digite o seu bairro: ')
    cidade = input('Digite a sua cidade: ')
    estado = input('Digite o seu estado:')

    pessoa.append(Pessoa(nome))
    endereco.append(Endereco(logradouro, numero, complemento, bairro, cidade, estado))
    i += 1