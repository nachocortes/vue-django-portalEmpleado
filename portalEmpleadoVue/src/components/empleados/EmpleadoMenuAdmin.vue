<script setup>
import {ref} from "vue";
import EmpleadoForm from "@/components/empleados/EmpleadoForm.vue";

const mostrarFormulario = ref(false);

</script>

<template>
    <nav class="d-flex flex-column flex-shrink-0 p-1 bg-body-tertiary ancho-navegacion">
        <ul class="nav nav-pills flex-column mb-auto">
            <li class="nav-item">
                <button @click="mostrarFormulario = !mostrarFormulario"
                        class="nav-link nav-link{{ mostrarFormulario ? '-primary' : '' }} text-start ">
                    <i class="bi bi-house me-2"></i>
                    <span>{{ mostrarFormulario ? 'Ocultar Formulario' : 'Crear Empleado' }}</span>
                </button>
            </li>
        </ul>
    </nav>
    <div v-if="mostrarFormulario" class="mt-3">
        <EmpleadoForm/>
    </div>
</template>

<style scoped>
.ancho-navegacion {
    width: 15em;
}
</style>
