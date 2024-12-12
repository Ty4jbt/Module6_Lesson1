# Task 2: Fetching Data of Planets from the API

import requests

def fetch_planet_data():

    url = "https://api.le-systeme-solaire.net/rest/bodies/"

    response = requests.get(url)

    planets = response.json()['bodies']

    planet_data = []

    for planet in planets:
        
        if planet['isPlanet']:
            
            name = planet['englishName']

            mass = planet['mass']['massValue'] if planet.get('mass') else 'Unknown'

            orbital_period = planet['sideralOrbit'] if planet.get('sideralOrbit') else 'Unknown'

            planet_data.append((name, mass, orbital_period))

    return planet_data

planet_data = fetch_planet_data()

for name, mass, orbital_period in planet_data:

    print(f'Name: {name}, Mass: {mass}, Orbital Period: {orbital_period} days')

# Task 3: Data Presentation and Analysis


planets = fetch_planet_data()
def find_heaviest_planet(planets):

    heaviest = max(planets, key=lambda planet: planet[1] if planet[1] != 'Unknown' else float('-inf'))

    return heaviest

heaviest_planet = find_heaviest_planet(planet_data)  

print(f'\nThe heaviest planet is {heaviest_planet[0]} with a mass of {heaviest_planet[1]} kg.')