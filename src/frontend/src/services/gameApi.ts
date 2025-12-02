import axios from 'axios';
import { SubmitResponse } from '../types/types';

const BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:5000/api';

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
