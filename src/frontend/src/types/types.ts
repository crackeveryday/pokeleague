export interface GameState {
    gameId: string;
    moveName: string;
    startTime: string;
    isGameActive: boolean;
    answers: string[];
    timeRemaining: number;
  }
  
  export interface SubmitResponse {
    status: 'ongoing' | 'clear' | 'timeout' | 'error';
    correct: boolean;
    answers_count: number;
    user_answers: string[];
    correct_answers?: string[];
    message?: string;
  }
  