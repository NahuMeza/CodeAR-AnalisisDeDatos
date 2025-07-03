import requests as rq

response = rq.get('https://pokeapi.co/api/v2/pokemon/pikachu')

if (response.status_code != 404):
    print(len(response.json()['abilities']))
else:
    print("no se encuentra")