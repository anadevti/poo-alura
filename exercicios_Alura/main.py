'''
7 - Crie um Arquivo Main (main.py): Crie um arquivo chamado main.py no mesmo diretório que suas classes.
'''

'''
8 - Importe e Instancie Objetos: No arquivo main.py, importe as classes Carro e Moto. Em seguida,
crie três instâncias de Carro e Moto com diferentes marcas, modelos, quantidade de portas e tipos.
'''

from exercicios_Alura import Carro, Moto

carro1 = Carro('Fiat', 'Uno', 4)
carro2 = Carro('Chevrolet', 'Camaro', 2)
carro3 = Carro('Ford', 'Fusion', 4)

moto1 = Moto('Honda', 'CBR', 'Esportiva')
moto2 = Moto('Yamaha', 'Factor', 'Casual')
moto3 = Moto('Suzuki', 'Boulevard', 'Casual')

'''
9 - Exiba as Informações: Para cada instância, imprima no console as informações utilizando o método str.
'''

print (carro1)
print (carro2)
print (carro3)
print (moto1)
print (moto2)
print (moto3)
