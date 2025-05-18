<template>
    <ProductList :products="products" @update-stock="updateStock" />
</template>

<script>
import { ref, onMounted, watch } from 'vue';
import ProductList from '../components/ProductList.vue';

export default {
    components: {
        ProductList
    },
    setup() {
        const products = ref([]);
        const API_URL = 'http://localhost:5000/graphql';

        const fetchProducts = async () => {
            try {
                const response = await fetch(API_URL, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        query:
                            ' query{ products { id name stock available }}'
                    })

                });

                const result = await response.json();
                if (result.data && result.data.products) {
                    products.value = result.data.products;
                } else {
                    console.error("Error al obtener productos:", result.errors);
                }
            } catch (error) {
                console.error("Error de red al obtener productos:", error);
            }
        };

        const updateStock = async (id, change) => {
            const product = products.value.find(p => p.id === id);
            if (!product) return;

            try {
                const response = await fetch(API_URL, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        query: `mutation ModifyStock($id: Int!, $stock: Int!) { modifyStock(id: $id, stock: $stock) { product { id stock available }}}`,
                        variables: {
                            id,
                            stock: change
                        }
                    })
                });

                const result = await response.json();
                if (result.data && result.data.modifyStock) {
                    const updated = result.data.modifyStock.product;
                    const index = products.value.findIndex(p => p.id === updated.id);
                    if (index !== -1) {
                        products.value[index].stock = updated.stock;
                        products.value[index].available = updated.available;
                    }
                } else {
                    console.error("Error al modificar stock:", result.errors);
                }
            } catch (error) {
                console.error("Error de red al modificar stock:", error);
            }
        };

        onMounted(() => {
            fetchProducts();
        });

        watch(
            () => products.value.map(p => p.stock),
            () => {
                products.value.forEach(p => {
                    p.available = p.stock > 0;
                });
            },
            { deep: true }
        );

        return {
            products,
            updateStock
        };
    }
};
</script>


<style>
label {
    width: 100%;
    display: block;
    margin-bottom: 10px;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    gap: 12px;
}

input {
    flex-grow: 1;
    padding: 5px;
    margin-top: 5px;
    border-radius: 4px;
    border: 1px solid #ccc;
}
</style>
