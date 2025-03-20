<template>
  <div class="product-card" :class="{ unavailable: !product.available }">
    <h3>{{ product.name }}</h3>
    <p>Precio: €{{ product.price }}</p>
    <p>Stock: {{ product.stock }}</p>
    <p v-if="product.available" class="available">Disponible</p>
    <p v-else class="unavailable">No Disponible</p>
    <button @click="$emit('update-stock', -1)" :disabled="product.stock === 0">Vender</button>
    <button @click="$emit('update-stock', 1)">Reponer</button>
  </div>
</template>

<script>
export default {
  props: {
    product: Object
  }
};
</script>

<style>
.product-card {
  background: white;
  padding: 15px;
  margin: 10px;
  border-radius: 8px;
  box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
}
.available {
  color: green;
}
.unavailable {
  color: red;
}
button {
  margin: 5px;
}
</style>
