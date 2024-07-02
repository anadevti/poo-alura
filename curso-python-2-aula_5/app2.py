import requests

url = "https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json"
response = requests.get(url)
print (response)

if response.status_code == 200:
  dados_json = response.json()
  dados_restaurante = {}
  for item in dados_json:
    nome_do_restaurante = item['Company']
    if nome_do_restaurante not in dados_restaurante:
     dados_restaurante[nome_do_restaurante] = [] 
     
     dados_restaurante[nome_do_restaurante].append({
       "item": item['Item'],
       "price": item['price'],
       "description": item['description']
     })
else:
  print(f'Erro ao acessar a URL: {url}')

for nome_do_restaurante, dados_do_restaurante in dados_restaurante.items():
  print(f"Restaurante: {nome_do_restaurante}")
  for item in dados_do_restaurante:
    print(f"  Item: {item['item']}")
    print(f"  Preço: {item['price']}")
    print(f"  Descrição: {item['description']}")
    print()