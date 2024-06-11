<script setup>
import { onMounted, reactive, ref, inject } from 'vue';
import { required } from "@vuelidate/validators";
import useVuelidate from "@vuelidate/core";
import {useAuthStore} from "@/stores/auth.js";
import { useEmpleadoStore } from "@/stores/empleados.js";
import { useAusenciaStore } from "@/stores/ausencias.js";
import EmpleadoSelector from "@/components/empleados/EmpleadoSelector.vue";


const ausencias = useAusenciaStore();
const empleados = useEmpleadoStore();
const auth = useAuthStore()

const empleado = ref(null);
const guardarAusencia = inject('guardarAusencia');

onMounted(() => {
    empleados.fetch();
});

const handleEmpleadoSelected = (item) => {
    empleado.value = item;
};

const nuevaAusencia = reactive({
    empleado: null,
    fecha: '',
    motivo: '',
    justificada: false,
});

const reglasValidacion = {
    motivo: {
        required,
    },
    fecha: {
        required,
    },
};

const v$ = useVuelidate(reglasValidacion, nuevaAusencia, { $autoDirty: true });

function botonPulsado() {
    const result = v$.value.$validate();
    result.then((valid) => {
        if (valid) {
            nuevaAusencia.empleado = empleado.value.url;
            guardarAusencia(nuevaAusencia);
            limpiar();
        }
    }).catch((error) => {
        console.log(error);
    });
}

function limpiar() {
    nuevaAusencia.empleado = null;
    nuevaAusencia.fecha = '';
    nuevaAusencia.motivo = '';
    nuevaAusencia.justificada = false;
    empleado.value = null;
    v$.value.$reset();
}
</script>

<template>
    <h6>Registro ausencias</h6>
    <div class="row p-3">
        <div class="card p-3 col-12">
            <div class="mb-3 me-1">
                <EmpleadoSelector :empleados="empleados.items" @item-selected="handleEmpleadoSelected"/>
            </div>
            <div class="mb-3">
                <label class="form-label" for="fecha">Fecha</label>
                <input class="form-control" type="date" v-model="nuevaAusencia.fecha">
                <p class="alert alert-warning mt-3" v-for="error in v$.fecha.$errors" :key="error.$uid">
                    {{ error.$message }}
                </p>
            </div>
            <div class="mb-3">
                <label class="form-label" for="motivo">Motivo</label>
                <input class="form-control" placeholder="Escribe algo..." id="motivo" type="text"
                       @keyup.enter="botonPulsado()"
                       v-model="nuevaAusencia.motivo"/>
                <p class="alert alert-warning mt-3" v-for="error in v$.motivo.$errors" :key="error.$uid">
                    {{ error.$message }}
                </p>
            </div>
            <div class="mb-3 form-check">
                <input class="form-check-input" type="checkbox" id="justificada" v-model="nuevaAusencia.justificada">
                <label class="form-check-label" for="justificada">Justificante</label>
            </div>
            <div>
                <button class="btn btn-primary" :disabled="v$.$invalid" @click="botonPulsado">Guardar</button>
                <button class="btn btn-link link-dark" :disabled="!v$.$anyDirty" @click="limpiar">Cancelar</button>
            </div>
        </div>
    </div>
</template>

<style scoped>
</style>
