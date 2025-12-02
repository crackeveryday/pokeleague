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
            // スプライトURLを含む新しい回答配列を作成
            const updatedAnswers = response.user_answers.map(answer => ({
                name: answer,
                image: response.images?.[answer]
            }));

            setGameState(prev => ({
                ...prev!,
                answers: updatedAnswers
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
        <div className="start-screen">
          <div className="start-content">
            <p className="start-description">技名からポケモンを当てるクイズゲーム！<br />制限時間は60秒、5匹答えてクリアを目指そう！</p>
            <button className="start-button" onClick={startGame}>
              <span className="button-icon">▶</span> ゲームスタート
            </button>
          </div>
        </div>
      ) : (
        <>
          <div className="question-section">
            <h2 className="question-title">
              <span className="question-label">お題</span>
              <span className="move-name">「{gameState.moveName}」</span>
              を覚えるポケモンを5匹答えよ！
            </h2>
          </div>

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
            <h3 className="answers-title">
              正解したポケモン
              <span className="progress-badge">{gameState.answers.length}/5</span>
            </h3>
            <div className="pokemon-grid">
                {gameState.answers.map((answer, index) => (
                    <div key={index} className="pokemon-card">
                        {answer.image && (
                            <img
                                src={answer.image}
                                alt={answer.name}
                                className="pokemon-image"
                            />
                        )}
                        <span className="pokemon-name">{answer.name}</span>
                    </div>
                ))}
            </div>
          </div>

          {message && (
            <div className={`message ${isGameOver ? 'message-gameover' : ''}`}>
              {message}
            </div>
          )}

          {isGameOver && (
            <button className="restart-button" onClick={startGame}>
              <span className="button-icon">🔄</span> もう一度プレイ
            </button>
          )}
        </>
      )}
    </div>
  );
};

export default Game;
