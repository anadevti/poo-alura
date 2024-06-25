from modelos.cardapio.item_cardapio import ItemCardapio

class Bebida(ItemCardapio): #herdando de item_cardapio
    def __init__(self, nome, preco, tamanho):
      super().__init__(nome, preco) # acessando informações da classe pai (item_cardapio)
      self.tamanho = tamanho
      
    def __str__(self):
      return self._nome
    
    def aplicar_desconto(self):
      self._preco -= (self._preco * 0.05)