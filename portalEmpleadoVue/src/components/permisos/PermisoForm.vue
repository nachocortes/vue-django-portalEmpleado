<script setup>
import { onMounted, reactive, ref, inject } from 'vue';
import { required } from "@vuelidate/validators";
import useVuelidate from "@vuelidate/core";
import { useEmpleadoStore } from "@/stores/empleados.js";
import {useAuthStore} from "@/stores/auth.js";
import {usePermisoStore} from "@/stores/permisos.js";
import EmpleadoSelector from "@/components/empleados/EmpleadoSelector.vue";


const permisos = usePermisoStore()
const empleados = useEmpleadoStore();
const auth = useAuthStore()

const empleado = ref(null);
const guardarPermiso = inject('guardarPermiso');

onMounted(() => {
    empleados.fetch();
});

const handleEmpleadoSelected = (item) => {
    empleado.value = item;
};

const nuevoPermiso = reactive({
    empleado: null,
    fecha: '',
    causa: '',
    estado: false,
});

const reglasValidacion = {
    causa: {
        required,
    },
    fecha: {
        required,
    },
};

const v$ = useVuelidate(reglasValidacion, nuevoPermiso, { $autoDirty: true });

function botonPulsado() {
    const result = v$.value.$validate();
    result.then((valid) => {
        if (valid) {
            nuevoPermiso.empleado = empleado.value.url;
            guardarPermiso(nuevoPermiso);
            limpiar();
        }
    }).catch((error) => {
        console.log(error);
    });
}

function limpiar() {
    nuevoPermiso.empleado = null;
    nuevoPermiso.fecha = '';
    nuevoPermiso.causa = '';
    nuevoPermiso.estado = false;
    empleado.value = null;
    v$.value.$reset();
}
</script>

<template>
    <h6>Registro permisos</h6>
    <div class="row p-3">
        <div class="card p-3 col-12">
            <div class="mb-3 me-1">
                <EmpleadoSelector :empleados="empleados.items" @item-selected="handleEmpleadoSelected"/>
            </div>
            <div class="mb-3">
                <label class="form-label" for="fecha">Fecha</label>
                <input class="form-control" type="date" v-model="nuevoPermiso.fecha">
                <p class="alert alert-warning mt-3" v-for="error in v$.fecha.$errors" :key="error.$uid">
                    {{ error.$message }}
                </p>
            </div>
            <div class="mb-3">
                <label class="form-label" for="causa">Causa</label>
                <input class="form-control" placeholder="Escribe algo..." id="causa" type="text"
                       @keyup.enter="botonPulsado()"
                       v-model="nuevoPermiso.causa"/>
                <p class="alert alert-warning mt-3" v-for="error in v$.causa.$errors" :key="error.$uid">
                    {{ error.$message }}
                </p>
            </div>
            <div class="mb-3 form-check">
                <input class="form-check-input" type="checkbox" id="estado" v-model="nuevoPermiso.estado">
                <label class="form-check-label" for="estado">cocedido</label>
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
