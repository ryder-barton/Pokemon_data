from bs4 import BeautifulSoup
import requests
from tabulate import tabulate
import pandas as pd

def get_pokemon_info():
    base_url = 'https://pokeapi.co/api/v2/pokemon/'  
    data = {}

    for number in range(1, 152):  
        url = base_url + str(number)
        response = requests.get(url)

        id = response.json()['id']
        name = response.json()['name'].title()
        types = [t['type']['name'] for t in response.json()['types']]
        height = round(response.json()['height'] / 10 * 3.28084, 2)
        weight = round(response.json()['weight'] / 10 * 2.20462, 2)

        for pokemon_type in types:
            if pokemon_type not in data:
                data[pokemon_type] = []

            data[pokemon_type].append([f'#{id}', name, ', '.join(types), height, weight])

    with pd.ExcelWriter('pokedata_type.xlsx', engine='xlsxwriter') as writer:
        for pokemon_type, pokemon_data in data.items():
            headers = ["ID", "Name", "Types", "Height(ft)", "Weight(lbs)"]
            df = pd.DataFrame(pokemon_data, columns=headers)
            
            # Write each DataFrame to a different sheet
            df.to_excel(writer, sheet_name=pokemon_type, index=False)
            
            print(f"\nType: {pokemon_type}")
            print(tabulate(df, headers=headers, tablefmt="grid"))


get_pokemon_info()





