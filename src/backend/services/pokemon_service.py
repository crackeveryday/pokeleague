import requests

class PokemonService:
    def __init__(self):
        self.base_url = "https://pokeapi.co/api/v2"

    def get_pokemon_by_move(self, move_name):
        """指定された技を覚えるポケモンのリストを取得"""
        try:
            response = requests.get(f"{self.base_url}/move/{move_name}")
            response.raise_for_status()
            
            move_data = response.json()
            pokemon_list = [
                pokemon['name'] 
                for pokemon in move_data['learned_by_pokemon']
            ]
            return pokemon_list
        except requests.RequestException as e:
            print(f"API error: {e}")
            return []

    def get_pokemon_sprite(self, pokemon_name):
        """ポケモンの画像URLを取得"""
        try:
            response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}")
            response.raise_for_status()
            return response.json()['sprites']['front_default']
        except:
            return None