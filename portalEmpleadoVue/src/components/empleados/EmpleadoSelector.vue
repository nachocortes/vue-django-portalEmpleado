<script setup>
import { ref } from 'vue';
import { defineProps, defineEmits } from 'vue';

const props = defineProps({
    empleados: Array
});

const emit = defineEmits(['item-selected']);

const selectedEmpleado = ref()

const selectItem = () => {
    emit('item-selected', selectedEmpleado.value);
};
</script>

<template>
    <div class="select-container">
        <select class="form-select form-select-sm bg-body-tertiary"
                v-model="selectedEmpleado" @change="selectItem">
            <option value="" disabled>Seleccione un empleado</option>
            <option v-for="empleado in empleados" :key="empleado" :value="empleado">
                {{ empleado.nombre }}
            </option>
        </select>
    </div>
</template>

<style scoped>
.select-container {
    width: 170px;
}
</style>
