class Funcionario:
    __slots__ = ['nome','_salario','registro','cpf','data_entrada','setor']

    def __init__(self, nome, salario, registro, cpf, data_entrada, setor):
        self.nome = nome
        self._salario = salario
        self.registro = registro
        self.cpf = cpf
        self.data_entrada = data_entrada
        self.setor = setor

    @property    
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self, valor):
        self._salario = valor

    def altera_Salario(self, valor):
        self.salario(valor)

    def altera_Setor(self,setor):
        self.setor = setor
