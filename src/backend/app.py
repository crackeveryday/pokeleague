from flask import Flask, jsonify, request
from flask_cors import CORS
from services.quiz_service import QuizService
from models.game import Game
import os

app = Flask(__name__)

allowed_origins = os.environ.get(
    'ALLOWED_ORIGINS',
    'https://crackeveryday.github.io'
).split(',')
CORS(app, origins=allowed_origins)

quiz_service = QuizService()

@app.route('/api/game/start', methods=['GET', 'POST'])  # GETメソッドも許可
def start_game():
    game = quiz_service.create_new_game()
    return jsonify({
        'game_id': game.id,
        'move_name': game.move_name,
        'start_time': game.start_time.isoformat()
    })

@app.route('/api/game/<game_id>/submit', methods=['GET', 'POST'])
def submit_answer(game_id):  # game_idを引数として追加
    pokemon_name = request.json['pokemon_name']
    
    result = quiz_service.submit_answer(game_id, pokemon_name)
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='backend', port=5000, debug=False)
