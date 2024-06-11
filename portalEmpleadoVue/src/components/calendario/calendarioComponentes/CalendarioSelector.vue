<script setup>
import { onMounted, ref, inject } from 'vue';
import { useCalendarioStore } from "@/stores/calendarios.js";

const calendarios = useCalendarioStore();
const calendario = ref(null);
const updateCalendario = inject('updateCalendario');

onMounted(() => {
    calendarios.fetch();
});

function emitCalendarioSeleccionado() {
    if (calendario.value && updateCalendario) {
        updateCalendario(calendario.value);
    }
}
</script>

<template>
    <div class="select-container">
        <select class="form-select form-select-sm bg-body-tertiary"
                v-model="calendario" @change="emitCalendarioSeleccionado">
            <option value="" disabled>Seleccione un calendario</option>
            <option v-for="calendarioItem in calendarios.items" :key="calendarioItem.id" :value="calendarioItem">
                {{ calendarioItem.nombre }}
            </option>
        </select>
    </div>
</template>

<style scoped>
.select-container {
    width: 150px;
}
</style>
