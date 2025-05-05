import axios from 'axios';

const API_URL = 'http://localhost:5000/auth';

export const userService = {
  async listUsers() {
    const response = await axios.get(`${API_URL}/list_users`);
    return response.data;
  },

  async registerUser(userData) {
    const response = await axios.post(`${API_URL}/register`, userData);
    return response.data;
  },

  async consultUser(queryParams) {
    const query = new URLSearchParams(queryParams).toString(); // Converte os parâmetros para query string
    const response = await axios.get(`${API_URL}/consult_user?${query}`);
    return response.data;
  },

  async disableUser(userId) {
    const response = await axios.delete(`${API_URL}/disable_user/${userId}`);
    return response.data;
  },
};