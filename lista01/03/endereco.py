class Endereco:
    __slots__ = ['logradouro','numero','complemento','bairro','cidade','estado']

    def __init__(self, logradouro, numero, complemento, bairro, cidade, estado):
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
