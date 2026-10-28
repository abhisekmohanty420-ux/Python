import requests

base_url='https://pokeapi.co/api/v2/'


def get_pokemon_info(name):
    url=f"{base_url}/pokemon/{name}"
    res=requests.get(url)
    if res.status_code==200:
        print('data retrived')
        pokemon_data=res.json()
        # print(pokemon_data)
        return pokemon_data
    else:
        print(f"failed to retrive data {res.status_code}")
    

pokemon_name='Pikachu'
pokemon=get_pokemon_info(pokemon_name)



if pokemon:
    print(f"name:{pokemon['name'].capitalize()}")
    print(f"id:{pokemon['id']}")
    print(f"height:{pokemon['height']}")
    print(f"weight:{pokemon['weight']}")