import requests
import json


# Task 2: Fetch data of a pokemon named "pikachu" from the pokeapi

response = requests.get('https://pokeapi.co/api/v2/pokemon/pikachu')

json_data = response.text

pikachu_data = json.loads(json_data)

print(pikachu_data["name"])
print(pikachu_data["abilities"])

# Task 3: Analyzing and Displaying the data

def fetch_pokemon_data(pokemon_name):
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}')

    return response.json()

def calulate_average_weight(pokemon_list):
    total_weight = sum(pokemon["weight"] for pokemon in pokemon_list if pokemon)

    return total_weight / len(pokemon_list)

def display_pokemon_data(pokemon_data, average_weight):
    for pokemon in pokemon_data:
        if pokemon:
            print(f'Name: {pokemon["name"].capitalize()}')
    
    print(f'Average weight: {average_weight}')

pokemon_names = ["pikachu", "charizard", "squirtle"]
pokemon_data = [fetch_pokemon_data(name) for name in pokemon_names]
average_weight = calulate_average_weight(pokemon_data)

display_pokemon_data( pokemon_data, average_weight)