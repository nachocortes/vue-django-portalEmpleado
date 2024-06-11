<script setup>
import {ref} from "vue";

const emit = defineEmits(['update:modoOscuro']);
const isDark = ref(true);

function emitModoOscuro() {
        emit('update:modoOscuro', isDark.value);
}
</script>

<template>
    <div class="flex items-center">
        <input id="modoOscuro" type="checkbox" v-model="isDark"  @change="emitModoOscuro"/>
        <label class="ms-1" for="modoOscuro">  <span>{{ isDark ? 'Modo claro' : 'Modo oscuro' }}</span> </label>
    </div>
</template>

<style scoped>

</style>
