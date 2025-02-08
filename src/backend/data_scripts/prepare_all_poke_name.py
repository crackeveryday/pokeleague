import time
import requests
import pickle

url = "https://pokeapi.co/api/v2/pokemon-species?limit=1500"

response = requests.get(url).json()

all_pokemon = [pokemon['name'] for pokemon in response['results']]
# print(all_pokemon)

base_url = "https://pokeapi.co/api/v2/pokemon-species/"


en_ja_dict = {}

for pokemon in all_pokemon:
    url = base_url + pokemon
    response = requests.get(url).json()
    jp_name = response['names'][0]['name']
    en_default_name = response['varieties'][0]['pokemon']['name']
    en_ja_dict[en_default_name] = jp_name
    time.sleep(0.1)

# test_all_pokemon = ['bulbasaur', 'ivysaur', 'venusaur', 'charmander', 'charmeleon', 'charizard', 'squirtle', 'wartortle', 'blastoise', 'caterpie', 'metapod', 'butterfree', 'weedle', 'kakuna', 'beedrill', 'pidgey', 'pidgeotto', 'pidgeot', 'rattata', 'raticate', 'spearow', 'fearow', 'ekans', 'arbok', 'pikachu', 'raichu', 'sandshrew', 'sandslash', 'nidoran-f', 'nidorina']

print(en_ja_dict)
with open('pokemon_names_en_ja.pkl', 'wb') as f:
    pickle.dump(en_ja_dict, f)