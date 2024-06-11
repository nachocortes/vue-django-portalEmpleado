<script setup>
import CalendarioEditar from "@/components/calendario/calendarioEditar/CalendarioEditar.vue";
import { useAuthStore } from "@/stores/auth.js";

const auth = useAuthStore();
</script>

<template>
    <CalendarioEditar/>
</template>

<style scoped>

</style>
