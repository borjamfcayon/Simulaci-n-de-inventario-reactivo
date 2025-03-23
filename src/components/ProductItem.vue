<template>
    <div class="product-card" :class="{ unavailable: !product.available }">
        <h3>{{ product.name }}</h3>
        <div class=" product-card-side">
            <p>Precio: {{ product.price }}€</p>
            <p>Stock: {{ product.stock }}</p>

        </div>
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
    width: 274px;
    padding: 15px;
    border-radius: 8px;
    box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
}

.product-card-side {
    height: 100%;
    display: flex;
    flex-direction: row;
    justify-content: space-around;
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
