<script setup>
import {ref} from 'vue';
import {defineProps, defineEmits} from 'vue';

const props = defineProps({
    departamentos: Array
});

const emit = defineEmits(['item-selected']);

const selectedDepartamento = ref()

const selectItem = () => {
    emit('item-selected', selectedDepartamento.value);
};
</script>

<template>
    <div class="select-container">
        <select class="form-select form-select-sm bg-body-tertiary"
                v-model="selectedDepartamento" @change="selectItem">
            <option value="" disabled>Seleccione un departamento</option>
            <option v-for="departamento in departamentos" :key="departamento" :value="departamento">
                {{ departamento.nombre }}
            </option>
        </select>
    </div>
</template>

<style scoped>
.select-container {
    width: 150px;
}
</style>
