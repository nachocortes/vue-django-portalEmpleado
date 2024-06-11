<script setup>
import {ref} from "vue";

const emit = defineEmits(['update:moverAHoy']);
const diaActual = ref(null);

function moverAHoy() {
    diaActual.value.move(new Date());
}

function emitMoverAHoy() {
    emit('update:moverAHoy', isDark.value);
}
</script>

<template>
    <button
        class="diaActual bg-secondary hover:bg-blue text-white  w-full px-3 pt-1 rounded-md"
        @click="moverAHoy">
        Hoy
    </button>
</template>

<style scoped>
</style>
