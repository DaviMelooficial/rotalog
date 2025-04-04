<template>
  <q-drawer show-if-above v-model="drawer" side="left" bordered>
    <div class="q-pa-md">
      <h1>Sidebar Teste</h1>
      <p>Este é um exemplo de texto na sidebar.</p>
    </div>
  </q-drawer>
</template>

<script>
export default {
  name: "SideBarMenu",
  data() {
    return {
      drawer: true, // Controla a visibilidade do drawer
    };
  },
};
</script>

<style>
.q-drawer {
  background-color: #2c6da4; /* Cor de fundo azul */
  color: white; /* Cor do texto padrão */
}
</style>
