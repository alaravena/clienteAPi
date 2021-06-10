import requests

def generate_request(url, params={}):
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()

def get_starWars():
    response = generate_request('https://rawcdn.githack.com/akabab/starwars-api/0.2.1/api/all.json')
    if response:
       return response