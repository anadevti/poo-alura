from fastapi import FastAPI, Query
import requests

app = FastAPI()

@app.get("/api/hello")
def hello():
    return {"message": "Hello World"}
  
@app.get("/api/restaurantes")
def get_restaurantes(restaurante: str = Query(None)):
  url = "https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json"
  response = requests.get(url)
  print (response)

  if response.status_code == 200:
    dados_json = response.json()
    if restaurante is None:
      return dados_json
    
    dados_restaurante = []
    for item in dados_json:
      if item ['Company'] == restaurante:
        dados_restaurante.append({
        "item": item['Item'],
        "price": item['price'],
        "description": item['description']
      })
  else:
    print(f'Erro ao acessar a URL: {url}')
    
    return {'Restaurante': restaurante, 'Cardapio': dados_restaurante}
'''
  for nome_do_restaurante, dados_do_restaurante in dados_restaurante.items():
    print(f"Restaurante: {nome_do_restaurante}")
    for item in dados_do_restaurante:
      print(f"  Item: {item['item']}")
      print(f"  Preço: {item['price']}")
      print(f"  Descrição: {item['description']}")
      print()
      '''