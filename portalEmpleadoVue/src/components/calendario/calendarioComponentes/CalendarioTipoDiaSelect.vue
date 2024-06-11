<script setup>
import {inject,ref} from "vue";

const opciones = ref(['Laborables', 'Festivos', 'Vacaciones', 'ILT', 'Libre disposicion',
    'Ausencias justificadas', 'Ausencias sin justificar', 'Otros']);

const tipoDia = inject('tipoDia');
const updateTipoDia = inject('updateTipoDia');

function emitTipoDiaSeleccionado() {
    if (tipoDia.value) {
        updateTipoDia(tipoDia.value);
    }
}
</script>

<template>
    <div class="select-container">
        <label for="empleado-select">Tipo de dia:</label>
        <select class="form-select form-select-sm bg-body-tertiary" aria-label=".form-select-sm example"
                v-model="tipoDia" @change="emitTipoDiaSeleccionado">
            <option>Selecione el tipo de dia</option>
            <option v-for="(tipo) in opciones" :key="tipo" :value="tipo">
                {{ tipo }}
            </option>
        </select>
    </div>
</template>

<style scoped>
.select-container {
    width: 170px;
}
</style>
