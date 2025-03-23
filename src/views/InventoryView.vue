<template>
    <div>
        <ProductList :products="products" @update-stock="updateStock" @show-dialog="showDialog = true" />

        <div v-if="showDialog" class="dialog-overlay">
            <div class="dialog">
                <h3>Añadir Producto</h3>
                <form @submit.prevent="submitProduct">
                    <label>
                        Nombre:
                        <input v-model="newProduct.name" required />
                    </label>
                    <label>
                        Precio:
                        <input type="number" v-model="newProduct.price" required />
                    </label>
                    <label>
                        Stock:
                        <input type="number" v-model="newProduct.stock" required />
                    </label>
                    <div class="dialog-buttons">
                        <button type="button" @click="onCancel"
                            style="background-color: rgb(200, 200, 200);">Cancelar</button>
                        <button type="submit" style="background-color: #3298ff;">Guardar</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
import { reactive, ref, watch } from 'vue';
import ProductList from '../components/ProductList.vue';

export default {
    components: {
        ProductList
    },
    setup() {
        /**
         * @type {Array<{ id: number, name: string, price: number, stock: number, available: boolean }>}
         */
        const products = reactive([
            { id: 1, name: "Laptop", price: 1200, stock: 5, available: true },
            { id: 2, name: "Teléfono", price: 800, stock: 3, available: true },
            { id: 3, name: "Tablet", price: 500, stock: 0, available: false }
        ]);

        const showDialog = ref(false);
        const newProduct = reactive({ name: '', price: 0, stock: 0 });

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

        const submitProduct = () => {
            if (newProduct.name.trim() && newProduct.price > 0 && newProduct.stock >= 0) {
                products.push({
                    id: products.length + 1,
                    name: newProduct.name,
                    price: newProduct.price,
                    stock: newProduct.stock,
                    available: newProduct.stock > 0
                });

                Object.assign(newProduct, { name: '', price: 0, stock: 0 });
                showDialog.value = false;
            }
        };

        const onCancel = () => {
            showDialog.value = false;
            Object.assign(newProduct, { name: '', price: 0, stock: 0 });
            form.reset();
        };

        return {
            products,
            showDialog,
            newProduct,
            updateStock,
            submitProduct,
            onCancel
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

button {
    flex-grow: 1;
}

.dialog-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.5);
    display: flex;
    justify-content: center;
    align-items: center;
}

.dialog {
    background: white;
    padding: 20px;
    border-radius: 8px;
    width: 300px;
}

.dialog-buttons {
    display: flex;
    justify-content: space-between;
    margin-top: 10px;
}
</style>
