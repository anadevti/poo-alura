from herança import Banco

class Agencia(Banco):
    def __init__(self, nome, endereco, numero):
        self.nome = nome
        self.endereco = endereco
        self.numero = numero
        super().__init__(nome, endereco)
        self.numero = numero