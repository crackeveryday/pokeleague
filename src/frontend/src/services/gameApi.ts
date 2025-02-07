import axios from 'axios';
import { SubmitResponse } from '../types/types';

const BASE_URL = import.meta.env.VITE_API_URL;

export const gameApi = {
  startGame: async () => {
    console.log('API URL:', import.meta.env.VITE_API_URL);
    const response = await axios.get(`${BASE_URL}/game/start`);
    console.log('Response:', response);
    return response.data;
  },

  submitAnswer: async (gameId: string, pokemonName: string): Promise<SubmitResponse> => {
    const response = await axios.post(`${BASE_URL}/game/${gameId}/submit`, {
      pokemon_name: pokemonName.toLowerCase()
    });
    return response.data;
  }
};
