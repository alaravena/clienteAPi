import requests

def generate_request(url, params={}):
    # requests.post(url, data, headers, timeout)
    try:
        response = requests.get(url, params=params)
    except requests.exceptions.ConnectionError as e:
        response = "No hay respuesta"
    if response.status_code == 200:
        return response.json()

def get_starWars():
    response = generate_request('https://rawcdn.githack.com/akabab/starwars-api/0.2.1/api/all.json')
    if response:
       return response