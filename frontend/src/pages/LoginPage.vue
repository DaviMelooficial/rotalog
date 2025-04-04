<!-- filepath: src/pages/LoginPage.vue -->
<template>
  <q-page class="flex flex-center">
    <q-card class="q-pa-md" style="width: 400px; max-width: 90%;">
      <q-card-section>
        <div class="text-h6 text-center">Login</div>
      </q-card-section>

      <q-card-section>
        <q-form @submit="handleLogin" class="q-gutter-md">
          <q-input
            v-model="username"
            label="username"
            outlined
            required
          />
          <q-input
            v-model="password"
            label="Senha"
            type="password"
            outlined
            required
          />
          <q-btn
            label="Entrar"
            color="primary"
            type="submit"
            class="full-width"
          />
        </q-form>
      </q-card-section>

      <q-card-actions align="center">
        <q-btn flat label="Esqueceu a senha?" color="primary" @click="forgotPassword" />
      </q-card-actions>
    </q-card>
  </q-page>
</template>

<script>
import axios from 'axios';

export default {
  name: 'LoginPage',
  data() {
    return {
      username: '', // Corrigido de 'email' para 'username'
      password: '',
    };
  },
  methods: {
    async handleLogin() {
      try {
        const response = await axios.post('http://localhost:5000/auth/login', {
          username: this.username, // Usando 'username'
          password: this.password,
        });

        // Exemplo de como lidar com a resposta
        const { access_token, user } = response.data;
        console.log('Token de acesso:', access_token);
        console.log('Usuário:', user);

        // Salve o token no localStorage ou em outro local seguro
        localStorage.setItem('access_token', access_token);

        // Redirecione o usuário para outra página, se necessário
        this.$router.push('/dashboard');
      } catch (error) {
        console.error('Erro ao fazer login:', error.response?.data || error.message);
        alert('Erro ao fazer login. Verifique suas credenciais.');
      }
    },
    forgotPassword() {
      console.log('Redirecionar para recuperação de senha');
    },
  },
};
</script>

<style scoped>
.full-width {
  width: 100%;
}
</style>
