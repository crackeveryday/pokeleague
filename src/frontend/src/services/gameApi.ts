import axios from 'axios';
import { SubmitResponse } from '../types/types';

const BASE_URL = 'http://127.0.0.1:5000/api';

export const gameApi = {
  startGame: async () => {
    const response = await axios.get(`${BASE_URL}/game/start`);
    return response.data;
  },

  submitAnswer: async (gameId: string, pokemonName: string): Promise<SubmitResponse> => {
    const response = await axios.post(`${BASE_URL}/game/${gameId}/submit`, {
      pokemon_name: pokemonName.toLowerCase()
    });
    return response.data;
  }
};
