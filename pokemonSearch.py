'''
Connecting to an API for Pokemon Information
https://www.youtube.com/watch?v=JVQNywo4AbU

Also used: https://medium.com/@mohamed.mywork/learn-apis-with-pok%C3%A9mon-and-python-7003b35b5ba
'''
import requests

base_url = "https://pokeapi.co/api/v2/"
pokemon_name = "mamoswine"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name.lower()}"
    response = requests.get(url)
    if response.status_code == 200:
        pkmn_data = response.json()
        info = {
            "name":     pkmn_data["name"],
            "id":       pkmn_data["id"],
            "height":   pkmn_data["height"],
            "weight":   pkmn_data["weight"],
            "ability":  [ability["ability"]["name"] for ability in pkmn_data["abilities"]],
            "types":    [type_data["type"]["name"] for type_data in pkmn_data["types"]],
        }
        return info
    else:
        print(f"Failed to retrieve pokemon info for {name}")
'''
pokemon_info = get_pokemon_info(pokemon_name)

if pokemon_info:
    print(f"Name: {pokemon_info["name"].capitalize()}")
    print(f"Dex No: {pokemon_info["id"]}")
    print(f"Types: {', '.join(pokemon_info['types'])}")
'''
if __name__ == '__main__':
    get_pokemon_info(input)