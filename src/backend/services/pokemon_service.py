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
