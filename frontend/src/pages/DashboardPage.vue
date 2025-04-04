<!-- filepath: src/pages/DashboardPage.vue -->
<template>
  <q-layout view="hHh lpR fFf">
    <!-- Sidebar -->
    <SideBarMenu />
    <!-- Conteúdo Principal -->
    <q-page-container>
      <q-page class="q-pa-md">
        <div class="q-mb-md">
          <h1>Painel de Logística</h1>
        </div>

        <!-- Cards de Status -->
        <div class="row q-col-gutter-md q-mb-md">
          <q-card class="col-6">
            <q-card-section>
              <div class="text-h6">Status das Entregas</div>
            </q-card-section>
            <q-card-section>
              <div class="row items-center">
                <q-icon name="check_circle" color="green" size="40px" />
                <div class="q-ml-md">
                  <div class="text-h5">185</div>
                  <div class="text-caption">Entregas no Prazo</div>
                  <div class="text-positive text-caption">+12.3% Comparado ao mês anterior</div>
                </div>
              </div>
            </q-card-section>
          </q-card>

          <q-card class="col-6">
            <q-card-section>
              <div class="text-h6">Entregas Atrasadas</div>
            </q-card-section>
            <q-card-section>
              <div class="row items-center">
                <q-icon name="error" color="red" size="40px" />
                <div class="q-ml-md">
                  <div class="text-h5">23</div>
                  <div class="text-caption">15 devido a condições de trânsito</div>
                </div>
              </div>
            </q-card-section>
          </q-card>
        </div>

        <!-- Tabela de Entregas -->
        <q-card>
          <q-card-section>
            <div class="text-h6">Entregas do Dia</div>
          </q-card-section>
          <q-table
            :rows-per-page-options="[5, 10, 15]"
            :rows="entregas"
            :columns="columns"
            row-key="id"
          >
            <template v-slot:body-cell-actions>
              <q-td>
                <q-btn label="Detalhes" color="primary" flat />
              </q-td>
            </template>
          </q-table>
        </q-card>
      </q-page>
    </q-page-container>
  </q-layout>
</template>

<script>
import SideBarMenu from "src/components/SideBar.vue";

export default {
  name: "DashboardPage",
  components: {
    SideBarMenu,
  },
  data() {
    return {
      entregas: [
        { id: "#ORD-2350", cidade: "Curitiba, PR" },
        { id: "#ORD-2351", cidade: "Porto Alegre, RS" },
        { id: "#ORD-2352", cidade: "Goiânia, GO" },
        { id: "#ORD-2353", cidade: "Manaus, AM" },
      ],
      columns: [
        { name: "id", required: true, label: "ID do Pedido", align: "left", field: "id" },
        { name: "cidade", label: "Cidade", align: "left", field: "cidade" },
        { name: "actions", label: "Ações", align: "center" },
      ],
    };
  },
};
</script>

<style scoped>
h1 {
  font-size: 1.5rem;
  font-weight: bold;
}
</style>
