<template>
  <div>
    <h2>Lista de Productos</h2>
    <div v-for="product in products" :key="product.id">
      <ProductItem :product="product" @update-stock="$emit('update-stock', product.id, $event)" />
    </div>
  </div>
</template>

<script>
import ProductItem from './ProductItem.vue';

export default {
  props: {
    products: Array
  },
  components: {
    ProductItem
  }
};
</script>
