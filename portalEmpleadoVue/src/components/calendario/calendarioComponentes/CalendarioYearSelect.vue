<script setup>
import { ref, computed } from 'vue';
const emit = defineEmits(['update:selectedYear']);
const anio = ref(new Date().getFullYear());

const years = computed(() => {
    const startYear = 2020;
    const endYear = 2050;
    const yearsArray = [];
    for (let year = startYear; year <= endYear; year++) {
        yearsArray.push(year);
    }
    return yearsArray;
});

function emitSelectedYear() {
    emit('update:selectedYear', anio.value);
}
</script>

<template>
    <div class="select-container">
        <label for="year-select">Año:</label>
        <select id="year-select" class="form-select form-select-sm bg-body-tertiary"
                v-model="anio" @change="emitSelectedYear">
            <option value="" disabled>Seleccione un año</option>
            <option v-for="year in years" :key="year" :value="year">
                {{ year }}
            </option>
        </select>
    </div>
</template>


<style scoped>
.select-container {
    width: 170px;
}
</style>
