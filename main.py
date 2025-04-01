import requests
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/")
def read_root():
    '''
    Endpoint que exibe uma mensagem dando boas vindas à API!
    '''
    return {"message": "Bem-vindo à API de Restaurantes!"}

@app.get('/api/restaurantes/')
def get_restaurantes(restaurante: str = Query(None)):
    '''
    Endpoint para ver os cardápios do restaurantes
    '''
    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
    response = requests.get(url)
 
    if response.status_code == 200:
        dados_json = response.json()
        if restaurante is None:
            return {'Dados': dados_json}

        dados_restaurante = []
        for item in dados_json:
            if item['Company'] == restaurante:
                dados_restaurante.append({
                "item": item['Item'],
                "price": item['price'],
                "description": item['description']
            })
        return {'Restaurante': restaurante, 'Cardapio': dados_restaurante}
    else: 
     return {'Erro':f'{response.status_code} - {response.text}'}