from datetime import datetime
from uuid import uuid4

class Game:
    def __init__(self, move_name, correct_answers):
        self.id = str(uuid4())
        self.move_name = move_name
        self.correct_answers = correct_answers
        self.user_answers = []
        self.start_time = datetime.now()
        self.is_finished = False

    def add_answer(self, pokemon_name):
        if not self.is_finished and pokemon_name in self.correct_answers and pokemon_name not in self.user_answers:
            self.user_answers.append(pokemon_name)
            return True
        return False

    def check_game_status(self):
        if len(self.user_answers) >= 5:
            self.is_finished = True
            return "clear"
        
        time_elapsed = (datetime.now() - self.start_time).seconds
        if time_elapsed > 60:
            self.is_finished = True
            return "timeout"
            
        return "ongoing"
