<template>
    <div class="main-container">
        <h2>Lista de Productos</h2>
        <button @click="$emit('show-dialog')">Añadir Producto</button>
        <div class="product-list">
            <div v-for="product in products" :key="product.id">
                <ProductItem :product="product" @update-stock="$emit('update-stock', product.id, $event)" />
            </div>
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

<style>
.main-container {
    width: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
}

.product-list {
    width: 100%;
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    justify-content: start;
    overflow-y: auto;
    gap: 8px;
}
</style>