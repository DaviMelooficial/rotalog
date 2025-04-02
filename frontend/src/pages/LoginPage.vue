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
            v-model="email"
            label="E-mail"
            type="email"
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
export default {
  name: 'LoginPage',
  data() {
    return {
      email: '',
      password: '',
    };
  },
  methods: {
    handleLogin() {
      console.log('E-mail:', this.email);
      console.log('Senha:', this.password);
      // Adicione aqui a lógica para autenticação
    },
    forgotPassword() {
      console.log('Redirecionar para recuperação de senha');
      // Adicione aqui a lógica para recuperação de senha
    },
  },
};
</script>

<style scoped>
.full-width {
  width: 100%;
}
</style>
