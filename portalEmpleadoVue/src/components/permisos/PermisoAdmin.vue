<script setup>
import { ref, inject, provide } from 'vue';
import PermisoForm from "@/components/permisos/PermisoForm.vue";

const mostrarFormulario = ref(false);
const guardarPermiso = inject('guardarPermiso');

provide('guardarPermiso', guardarPermiso);
</script>

<template>
    <nav class="d-flex flex-column flex-shrink-0 p-1 bg-body-tertiary ancho-navegacion">
        <ul class="nav nav-pills flex-column mb-auto">
            <li class="nav-item">
                <button @click="mostrarFormulario = !mostrarFormulario"
                        class="nav-link nav-link{{ mostrarFormulario ? '-primary' : '' }} text-start ">
                    <i class="bi bi-house me-2"></i>
                    <span>{{ mostrarFormulario ? 'Ocultar Formulario' : 'Crear permiso' }}</span>
                </button>
            </li>
        </ul>
    </nav>
    <div v-if="mostrarFormulario" class="mt-3">
        <PermisoForm/>
    </div>
</template>

<style scoped>
.ancho-navegacion {
    width: 15em;
}
</style>
