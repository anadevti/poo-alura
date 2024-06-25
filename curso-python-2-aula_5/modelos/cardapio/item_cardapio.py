from abc import ABC, abstractclassmethod
class ItemCardapio(ABC):
    def __init__(self, nome, preco, tipo, tamanho):
        self._nome = nome
        self._preco = preco
        self.tipo = tipo
        self.tamanho = tamanho
        
        @abstractclassmethod
        def aplicar_desconto(self):
            pass