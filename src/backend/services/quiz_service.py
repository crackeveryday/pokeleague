import random
from models.game import Game
from services.pokemon_service import PokemonService

class QuizService:
    def __init__(self):
        self.pokemon_service = PokemonService()
        self.active_games = {}
        self.available_moves = [
            'surf', 'thunderbolt', 'flamethrower', 
            'psychic', 'earthquake'
        ]  # 出題する技のリスト

    def create_new_game(self):
        """新しいゲームを作成"""
        move_name = random.choice(self.available_moves)
        correct_answers = self.pokemon_service.get_pokemon_by_move(move_name)
        
        game = Game(move_name, correct_answers)
        self.active_games[game.id] = game
        return game

    def submit_answer(self, game_id, pokemon_name):
        """回答を提出"""
        game = self.active_games.get(game_id)
        if not game:
            return {"status": "error", "message": "Game not found"}

        if game.is_finished:
            return {"status": "error", "message": "Game already finished"}

        is_correct = game.add_answer(pokemon_name)
        game_status = game.check_game_status()

        response = {
            "status": game_status,
            "correct": is_correct,
            "answers_count": len(game.user_answers),
            "user_answers": game.user_answers
        }

        if game_status != "ongoing":
            response["correct_answers"] = game.correct_answers
            del self.active_games[game_id]

        return response
