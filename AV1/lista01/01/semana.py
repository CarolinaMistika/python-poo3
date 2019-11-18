class Semana:
    __slots__ = ['dia_semana','nome_semana']

    def __init__(self, dia_semana, nome_semana):
        self.dia_semana = dia_semana
        self.nome_semana = nome_semana

    @property    
    def get_semana(self):
        return self.nome_semana

    @get_semana.setter
    def set_semana(self, valor):
        self.nome_semana = valor