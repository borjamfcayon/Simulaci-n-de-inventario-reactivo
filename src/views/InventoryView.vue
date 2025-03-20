<template>
  <div>
    <ProductList :products="products" @update-stock="updateStock" />
  </div>
</template>

<script>
import { reactive, watch } from 'vue';
import ProductList from '../components/ProductList.vue';

export default {
  components: {
    ProductList
  },
  setup() {
    const products = reactive([
      { id: 1, name: "Laptop", price: 1200, stock: 5, available: true },
      { id: 2, name: "Teléfono", price: 800, stock: 3, available: true },
      { id: 3, name: "Tablet", price: 500, stock: 0, available: false }
    ]);

    watch(
      () => products.map(p => p.stock),
      () => {
        products.forEach(p => {
          p.available = p.stock > 0;
        });
      },
      { deep: true }
    );

    const updateStock = (id, change) => {
      const product = products.find(p => p.id === id);
      if (product) {
        product.stock = Math.max(0, product.stock + change);
      }
    };

    return {
      products,
      updateStock
    };
  }
};
</script>
