export interface GameState {
  gameId: string;
  moveName: string;
  startTime: string;
  isGameActive: boolean;
  answers: Array<{
      name: string;
      image?: string;
  }>;
  timeRemaining: number;
}

export interface SubmitResponse {
  status: 'ongoing' | 'clear' | 'timeout' | 'error';
  correct: boolean;
  answers_count: number;
  user_answers: string[];
  images: { [key: string]: string };
  correct_answers?: string[];
  message?: string;
}
