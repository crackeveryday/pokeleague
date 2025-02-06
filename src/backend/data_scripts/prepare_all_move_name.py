import time
import requests
import pickle

# url = "https://pokeapi.co/api/v2/move?limit=1500"

# response = requests.get(url).json()

# all_pokemon = [pokemon['name'] for pokemon in response['results']]
# # print(all_pokemon)

base_url = "https://pokeapi.co/api/v2/move/"


ja_en_dict = {}

for i in range(1, 920):
    if i % 100 == 0:
        print(i)
    url = base_url + str(i)
    try:
        response = requests.get(url)
        num_learned_by_pokemon = len(response.json()['learned_by_pokemon'])
        if num_learned_by_pokemon >= 5:
            jp_name = response.json()['names'][0]['name']
            en_name = response.json()['name']
            ja_en_dict[jp_name] = (en_name, num_learned_by_pokemon)
    except:
        print(i)
        continue
    finally:
        time.sleep(0.1)
        


# print(ja_en_dict)
with open('move_learned_by_more_than_5.pkl', 'wb') as f:
    pickle.dump(ja_en_dict, f)