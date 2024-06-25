'''
3- Crie uma Classe Filha (Carro): Agora, crie uma classe chamada Carro que herda da classe Veiculo. 
No construtor da classe Carro, inclua um novo atributo chamado portas que indica a quantidade de portas do carro.
'''
from exercicios_Alura import Veiculo
class Carro(Veiculo):
  def __init__(self, marca, modelo, portas):
    super().__init__(marca, modelo)
    self.portas = portas
    
'''
4- Implemente o Método Especial str na Classe Filha: Adicione um método especial str à classe Carro que estenda o método da 
classe pai (Veiculo) e inclua a informação sobre a quantidade de portas do carro
'''

def __str__(self):
    return f'{super(Veiculo).__str__()}, Portas: {self.portas}'