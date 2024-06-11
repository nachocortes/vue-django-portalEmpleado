<script setup>
import CalendarioList from "@/components/calendario/calendarioCrear/CalendarioList.vue";
import { useAuthStore } from "@/stores/auth.js";

const auth = useAuthStore();
</script>

<template>
    <h1>Calendario</h1>
    <CalendarioList/>
</template>

<style scoped>
</style>
