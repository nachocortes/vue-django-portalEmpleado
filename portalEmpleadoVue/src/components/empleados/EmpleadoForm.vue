<script setup>
import {onMounted, reactive, ref} from 'vue';
import {useEmpleadoStore} from "@/stores/empleados.js";
import {integer, minLength, required} from "@vuelidate/validators";
import useVuelidate from "@vuelidate/core";
import {useDepartamentoStore} from "@/stores/departamentos.js";
import MiSelectDepartamentos from "@/components/departamentos/DepatamentoSelector.vue";
import {useAuthStore} from "@/stores/auth.js";

const empleados = useEmpleadoStore();
const departamentos = useDepartamentoStore();
const auth = useAuthStore()

const selectedDepartamentoUrl = ref(null);

onMounted(() => {
    departamentos.fetch();
});

const handleItemSelected = (item) => {
    selectedDepartamentoUrl.value = item.url;
};

const nuevoEmpleado = reactive({
    nombre: '',
    apellido: '',
    edad: 0,
    dni: '',
    departamento: selectedDepartamentoUrl,
});

const reglasValidacion = {
    nombre: {
        required,
        minLength: minLength(3)
    },
    apellido: {
        required,
        minLength: minLength(3)
    },
    edad: {
        required,
        integer
    },
    dni: {
        required,
    },

    departamento: {
        required,
    },
}

const v$ = useVuelidate(reglasValidacion, nuevoEmpleado, {$autoDirty: true})

function botonPulsado() {
    const result = v$.value.$validate();
    result.then((valid) => {
        if (valid) {
            empleados.save(nuevoEmpleado);
            limpiar();
        }
    }).catch((error) => {
        console.log(error);
    })
}

function limpiar() {
    nuevoEmpleado.nombre = '';
    nuevoEmpleado.apellido = '';
    nuevoEmpleado.edad = 0;
    nuevoEmpleado.dni = '';
    selectedDepartamentoUrl.value = '';
    v$.value.$reset();
}
</script>

<template>
    <div class="row p-3">
        <div class="card p-3 col-12">
            <div class="mb-3 me-1">
                <MiSelectDepartamentos :departamentos="departamentos.items" @item-selected="handleItemSelected"/>
            </div>
            <div v-if="selectedDepartamentoUrl !== null">
                <div class="mb-3">
                    <label class="form-label" for="nombre">Nombre</label>
                    <input class="form-control" placeholder="Nombre" id="nombre" type="text"
                           @keyup.enter="botonPulsado()"
                           v-model="nuevoEmpleado.nombre"/>
                    <p class="alert alert-warning mt-3" v-for="error of v$.nombre.$errors" :key="error.$uid">
                        {{ error.$message }}
                    </p>
                </div>
                <div class="mb-3">
                    <label class="form-label" for="apellido">Apellido</label>
                    <input class="form-control" placeholder="Apellido" id="apellido" type="text"
                           @keyup.enter="botonPulsado()"
                           v-model="nuevoEmpleado.apellido"/>
                    <p class="alert alert-warning mt-3" v-for="error of v$.apellido.$errors" :key="error.$uid">
                        {{ error.$message }}
                    </p>
                </div>
                <div class="mb-3">
                    <label class="form-label" for="dni">DNI</label>
                    <input class="form-control" placeholder="DNI" id="dni" type="text"
                           @keyup.enter="botonPulsado()"
                           v-model="nuevoEmpleado.dni"/>
                    <p class="alert alert-warning mt-3" v-for="error of v$.dni.$errors" :key="error.$uid">
                        {{ error.$message }}
                    </p>
                </div>
                <div class="mb-3">
                    <label class="form-label" for="edad">Edad</label>
                    <input class="form-control" placeholder="Edad" id="edad" type="text"
                           @keyup.enter="botonPulsado()"
                           v-model="nuevoEmpleado.edad"/>
                    <p class="alert alert-warning mt-3" v-for="error of v$.edad.$errors" :key="error.$uid">
                        {{ error.$message }}
                    </p>
                </div>

                <div>
                    <button class="btn btn-primary" :disabled="v$.$invalid" @click="botonPulsado()">Guardar</button>
                    <button class="btn btn-link link-dark" :disabled="!v$.$anyDirty" @click="limpiar()">Cancelar
                    </button>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
</style>
