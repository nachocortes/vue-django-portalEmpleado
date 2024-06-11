<script setup>
import { ref, inject, provide } from 'vue';
import AusenciasForm from "@/components/ausencias/AusenciasForm.vue";

const mostrarFormulario = ref(false);
const guardarAusencia = inject('guardarAusencia');

provide('guardarAusencia', guardarAusencia);
</script>

<template>
    <nav class="d-flex flex-column flex-shrink-0 p-1 bg-body-tertiary ancho-navegacion">
        <ul class="nav nav-pills flex-column mb-auto">
            <li class="nav-item">
                <button @click="mostrarFormulario = !mostrarFormulario"
                        class="nav-link nav-link{{ mostrarFormulario ? '-primary' : '' }} text-start ">
                    <i class="bi bi-house me-2"></i>
                    <span>{{ mostrarFormulario ? 'Ocultar Formulario' : 'Crear Ausencia' }}</span>
                </button>
            </li>
        </ul>
    </nav>
    <div v-if="mostrarFormulario" class="mt-3">
        <AusenciasForm/>
    </div>
</template>

<style scoped>
.ancho-navegacion {
    width: 15em;
}
</style>
