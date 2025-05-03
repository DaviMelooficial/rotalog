import axios from 'axios';

const API_URL = 'http://localhost:5000/auth';

const authService = {
  async login(username, password) {
    try {
      const response = await axios.post(`${API_URL}/login`, {
        username,
        password
      });
      
      if (response.data.access_token) {
        localStorage.setItem('token', response.data.access_token);
        localStorage.setItem('user', JSON.stringify(response.data.user));
      }
      
      return response.data;
    } catch (error) {
      if (error.response?.status === 401) {
        throw new Error('Usuário ou senha inválidos');
      }
      throw new Error('Erro ao conectar ao servidor');
    }
  },

  async resetPassword(email) {
    try {
      const response = await axios.post(`${API_URL}/forgot_password`, {
        email
      });
      return response.data;
    } catch (error) {
      if (error.response?.status === 404) {
        return { message: 'Se o e-mail estiver cadastrado, você receberá as instruções.' };
      }
      throw new Error('Erro ao processar sua solicitação. Tente novamente mais tarde.');
    }
  }
};

export default authService;