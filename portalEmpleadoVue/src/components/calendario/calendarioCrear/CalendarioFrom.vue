<script setup>
import {onMounted, reactive, ref} from 'vue';
import useVuelidate from "@vuelidate/core";
import {useEmpleadoStore} from '@/stores/empleados.js';
import {useDepartamentoStore} from '@/stores/departamentos.js';
import {useCalendarioStore} from '@/stores/calendarios.js';
import {required} from "@vuelidate/validators";
import MiSelectDepartamentos from "@/components/departamentos/DepatamentoSelector.vue";
import EmpleadoSelector from "@/components/empleados/EmpleadoSelector.vue";
import CalendarioYearSelect from "@/components/calendario/calendarioComponentes/CalendarioYearSelect.vue";

const calendarios = useCalendarioStore();
const departamentos = useDepartamentoStore();
const empleados = useEmpleadoStore();

onMounted(() => {
    departamentos.fetch();
    calendarios.fetch();
    empleados.fetch();
});

const selectedDepartamentoId = ref(null);
const selectedEmpleadoId = ref(null);
const empleado = ref({})

const handleDeparatmentoSelected = (item) => {
    selectedDepartamentoId.value = item.url;
};
const handleEmpleadoSelected = (item) => {
    selectedEmpleadoId.value = item.url;
};

const nuevoCalendario = reactive({
    url: "",
    nombre: "",
    anio: 2024,
    empleado: selectedEmpleadoId
});

const reglasValidacion = {
    anio: {
        required,
    },
    nombre: {
        required,
    },
    empleado: {
        required,
    },
}

const v$ = useVuelidate(reglasValidacion, nuevoCalendario, {$autoDirty: true});

function botonPulsado() {
    const result = v$.value.$validate();
    result.then((valid) => {
        if (valid) {
            calendarios.save(nuevoCalendario);
            limpiar();
        }
    }).catch((error) => {
        console.log(error);
    })
}

function limpiar() {
    nuevoCalendario.anio = '';
    nuevoCalendario.nombre = '';
    empleados.items = null;
    selectedDepartamentoId.value = null;
    v$.value.$reset();
}
</script>

<template>
    <div class="row p-3">
        <div class="card p-3 col-12">
            <div class="mb-3 me-1">
                <MiSelectDepartamentos :departamentos="departamentos.items"
                                       @item-selected="handleDeparatmentoSelected"/>
            </div>
            <div v-if="selectedDepartamentoId" class="mb-3">
                <CalendarioYearSelect/>
            </div>
            <div class="mb-3 me-1" v-if="selectedDepartamentoId">
                <EmpleadoSelector :empleados="empleados.items" @item-selected="handleEmpleadoSelected"/>
            </div>
            <div class="mb-3 me-1" v-if="selectedDepartamentoId">
                <label class="form-label" for="nombre">nombre</label>
                <input class="form-control" placeholder="Empleado y año..." id="nombre" type="text"
                       @keyup.enter="botonPulsado()"
                       v-model="nuevoCalendario.nombre"/>
                <p class="alert alert-warning mt-3" v-for="error of v$.nombre.$errors" :key="error.$uid">
                    {{ error.$message }}
                </p>
            </div>
            <div v-if="selectedDepartamentoId" class="mb-3">
                <button class="btn btn-primary" :disabled="v$.$invalid" @click="botonPulsado">Guardar</button>
                <button class="btn btn-link link-dark" :disabled="!v$.$anyDirty" @click="limpiar">Cancelar</button>
            </div>
        </div>
    </div>
</template>

<style scoped>
</style>
