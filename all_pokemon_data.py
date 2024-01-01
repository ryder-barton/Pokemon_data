from bs4 import BeautifulSoup
import requests
from tabulate import tabulate
import pandas as pd

def get_pokemon_info():
    base_url = 'https://pokeapi.co/api/v2/pokemon/'  
    data = []

    for number in range(1, 152):  
        url = base_url + str(number)
        response = requests.get(url)

        id = response.json()['id']
        name = response.json()['name'].title()
        types = ', '.join([t['type']['name'] for t in response.json()['types']])
        height = round(response.json()['height'] / 10 * 3.28084, 2)
        weight = round(response.json()['weight'] / 10 * 2.20462, 2)

        data.append([f'#{id}', name, types, height, weight])

    headers = ["ID", "Name", "Types", "Height(ft)", "Weight(lbs)"]

    df = pd.DataFrame(data, columns=headers)

    print(tabulate(df, headers=headers, tablefmt="grid"))

    df.to_excel('pokemon_data01.xlsx', index=False)

get_pokemon_info()
