import React, { useState } from 'react';
import { GameState } from '../types/types';
import { gameApi } from '../services/gameApi';
import Timer from './Timer';
import AnswerForm from './AnswerForm';

const Game: React.FC = () => {
  const [gameState, setGameState] = useState<GameState | null>(null);
  const [isGameOver, setIsGameOver] = useState(false);
  const [message, setMessage] = useState<string>('');

  const startGame = async () => {
    const data = await gameApi.startGame();
    setGameState({
      gameId: data.game_id,
      moveName: data.move_name,
      startTime: data.start_time,
      isGameActive: true,
      answers: [],
      timeRemaining: 60
    });
    setIsGameOver(false);
    setMessage('');
  };

  const handleTimeout = () => {
    setIsGameOver(true);
    setMessage('時間切れ！');
  };

  const handleSubmit = async (answer: string) => {
    if (!gameState || isGameOver) return;

    try {
      const response = await gameApi.submitAnswer(gameState.gameId, answer);
      
      if (response.correct) {
        setGameState(prev => ({
          ...prev!,
          answers: response.user_answers
        }));
      }

      if (response.status === 'clear') {
        setIsGameOver(true);
        setMessage('クリア！おめでとうございます！');
      }
    } catch (error) {
      console.error('Error submitting answer:', error);
    }
  };

  return (
    <div className="game-container">
      {!gameState ? (
        <button onClick={startGame}>ゲームスタート</button>
      ) : (
        <>
          <h2>技「{gameState.moveName}」を覚えるポケモンを5匹答えよ！</h2>
          <Timer 
            initialTime={60} 
            onTimeout={handleTimeout} 
            isActive={gameState.isGameActive && !isGameOver} 
          />
          <AnswerForm 
            onSubmit={handleSubmit} 
            disabled={isGameOver} 
          />
          <div className="answers-list">
            <h3>正解したポケモン ({gameState.answers.length}/5):</h3>
            <ul>
              {gameState.answers.map((answer, index) => (
                <li key={index}>{answer}</li>
              ))}
            </ul>
          </div>
          {message && <div className="message">{message}</div>}
          {isGameOver && (
            <button onClick={startGame}>もう一度プレイ</button>
          )}
        </>
      )}
    </div>
  );
};

export default Game;
