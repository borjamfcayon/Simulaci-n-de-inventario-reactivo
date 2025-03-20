<template>
  <div id="app">
    <h1>Inventario de Productos</h1>
    <InventoryView />
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
  background-color: #f4f4f4;
  padding: 20px;
  text-align: center;
}
</style>
