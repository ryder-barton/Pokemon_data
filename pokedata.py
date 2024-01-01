from bs4 import BeautifulSoup
import requests

def get_pokemon_info():
    base_url = 'https://pokeapi.co/api/v2/pokemon/'  # Replace with your API endpoint
    for number in range(1, 152):  # Range from 1 to 150 (151 is exclusive)
        url = base_url + str(number)
        response = requests.get(url)


        id = response.json()['id']
        name = response.json()['name']
        types = response.json()['types']
        height = response.json()['height']
        converted_height = height / 10 * 3.28084
        weight = response.json()['weight']
        converted_weight = weight / 10 * 2.20462

        print()

        print(f'ID: #{id}')
        print(f'Name: {name.title()}')
        # print(f'Types: {types}')
        print(f'Height: {round(converted_height, 2)}ft')
        print(f'Weight: {round(converted_weight, 2)}lbs')

        print()

get_pokemon_info()



