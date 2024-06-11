<script setup>
import EmpleadoList from "@/components/empleados/EmpleadoList.vue";
import {useAuthStore} from "@/stores/auth.js";

const auth = useAuthStore();
</script>

<template>
    <div class="w-100">
    <h1>Empleados</h1>
    <EmpleadoList/>
    </div>
</template>

<style scoped>

</style>
