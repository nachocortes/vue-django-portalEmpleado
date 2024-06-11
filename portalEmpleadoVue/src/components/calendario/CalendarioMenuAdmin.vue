<script setup>
import {ref} from "vue";
import CalendarioTipoDiaSelect from "@/components/calendario/calendarioComponentes/CalendarioTipoDiaSelect.vue";
import CalendarioSelector from "@/components/calendario/calendarioComponentes/CalendarioSelector.vue";

const mostrarFormulario = ref(false);
const emit = defineEmits(['guardar', 'cancelar']);
</script>

<template>
    <nav class="d-flex flex-column flex-shrink-0 p-1 bg-body-tertiary ancho-navegacion">
        <ul class="nav nav-pills flex-column mb-auto">
            <li class="nav-item">
                <button @click="mostrarFormulario = !mostrarFormulario"
                        class="nav-link nav-link{{ mostrarFormulario ? '-primary' : '' }} text-start ">
                    <i class="bi bi-house me-2"></i>
                    <span>{{ mostrarFormulario ? 'Ocultar Formulario' : 'Crear calendario' }}</span>
                </button>
            </li>
        </ul>
    </nav>
    <div v-if="mostrarFormulario" class="mt-3">
        <div class="row p-3">
            <div class="card p-3 col-12">
                <div class="row mb-3" v-if="seleccionandoCalendario">
                    <CalendarioSelector/>
                </div>
                <div class="row mb-3" v-if="!seleccionandoCalendario">
                    <CalendarioTipoDiaSelect/>
                </div>
                <div class="row mb-3 me-2 text-center" v-if="!seleccionandoCalendario">
                    <button class="btn btn-primary" @click="$emit('guardar')">Guardar</button>
                    <button class="btn btn-link link-dark" @click="$emit('cancelar')">Cancelar</button>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
.ancho-navegacion {
    width: 15em;
}
</style>
