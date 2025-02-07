import random
from models.game import Game
from services.pokemon_service import PokemonService
from services.pokemon_name_converter import PokemonNameConverter
from services.move_name_converter import MoveNameConverter

class QuizService:
    def __init__(self):
        self.pokemon_service = PokemonService()
        self.name_converter = PokemonNameConverter()
        self.move_converter = MoveNameConverter()
        self.active_games = {}
        self.available_moves = list(self.move_converter.ja_to_en.keys())

    def create_new_game(self):
        """新しいゲームを作成"""
        move_name_ja = random.choice(self.available_moves)
        move_name_en = self.move_converter.ja_to_en[move_name_ja][0]
        # 技を覚えるポケモンのリストを取得（英語名）
        pokemon_list = self.pokemon_service.get_pokemon_by_move(move_name_en)
        self.available_moves.remove(move_name_ja)
        # 日本語名に変換
        correct_answers = [
            self.name_converter.get_japanese_name(name) 
            for name in pokemon_list
            if self.name_converter.get_japanese_name(name)
        ]
        
        game = Game(move_name_ja, correct_answers)
        self.active_games[game.id] = game
        return game

    def submit_answer(self, game_id: str, pokemon_name: str):
        """回答を提出"""
        game = self.active_games.get(game_id)
        if not game:
            return {"status": "error", "message": "Game not found"}
        
        if game.is_finished:
            return {"status": "error", "message": "Game already finished"}

        try:
            # 入力された日本語名を正規化して照合
            normalized_input = self.name_converter.normalize_name(pokemon_name)
            is_correct = False

            for correct_answer in game.correct_answers:
                if self.name_converter.normalize_name(correct_answer) == normalized_input:
                    is_correct = True
                    pokemon_name = correct_answer  # 正式な日本語名を使用
                    break

            if is_correct:
                pokemon_name_en = self.name_converter.convert_to_english(pokemon_name)
                image_url = self.pokemon_service.get_pokemon_sprite(pokemon_name_en)
                game.add_answer(pokemon_name, image_url)

            game_status = game.check_game_status()
            
            response = {
                "status": game_status,
                "correct": is_correct,
                "answers_count": len(game.user_answers),
                "user_answers": game.user_answers,
                "images": game.images
            }

            if game_status != "ongoing":
                response["correct_answers"] = game.correct_answers
                del self.active_games[game_id]

            return response

        except Exception as e:
            return {"status": "error", "message": str(e)}
