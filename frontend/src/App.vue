<template>
  <div id="app">
    <h1>Inventario de Productos</h1>
    <div class="main-container">
      <InventoryView />
    </div>
  </div>
</template>

<script>
import InventoryView from './views/InventoryView.vue';

export default {
  components: {
    InventoryView
  }
};
</script>

<style>
body {
  font-family: Arial, sans-serif;
  background-color: #d0d8e6;
  text-align: center;
}

.main-container {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
}
</style>
