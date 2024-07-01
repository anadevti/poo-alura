import requests

url = "https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json"
response = requests.get(url)
print (response)

if response.status_code == 200:
  dados_json = response.json()
  print (dados_json)
else:
  print(f'Erro ao acessar a URL: {url}')