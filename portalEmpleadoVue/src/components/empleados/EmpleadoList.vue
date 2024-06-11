<script setup>
import moment from "moment/min/moment-with-locales";
import useVuelidate from "@vuelidate/core";
import {integer, minLength, required} from "@vuelidate/validators";
import {ref, onMounted, reactive} from "vue";
import {useEmpleadoStore} from "@/stores/empleados.js";
import {useAuthStore} from "@/stores/auth.js";
import EmpleadoMenuAdmin from "@/components/empleados/EmpleadoMenuAdmin.vue";

moment.locale('es');

const empleados = useEmpleadoStore();
const auth = useAuthStore();
const isEditing = ref(false);
const selectedDepartamento = ref(null);

onMounted(() => {
    empleados.fetch();
});


const editarEmpleado = reactive({
    id: 1,
    nombre: '',
    apellido: '',
    edad: 0,
    dni: '',
    departamento: null,
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
}

const v$ = useVuelidate(reglasValidacion, editarEmpleado)

function botonPulsado() {
    const result = v$.value.$validate();
    result.then((valid) => {
        if (valid) {
            empleados.update(editarEmpleado);
            limpiar();
        }
    }).catch((error) => {
        console.log(error);
    })
}

function limpiar() {
    isEditing.value = false;
    editarEmpleado.nombre = '';
    editarEmpleado.apellido = '';
    editarEmpleado.edad = 0;
    editarEmpleado.dni = '';
    editarEmpleado.id = 1;
    selectedDepartamento.value = '';
    v$.value.$reset();
}

function startEditing(empleado) {
    editarEmpleado.id = empleado.id
    selectedDepartamento.value = empleado.departamento
    editarEmpleado.departamento = selectedDepartamento
    editarEmpleado.nombre = empleado.nombre
    editarEmpleado.apellido = empleado.apellido
    editarEmpleado.dni = empleado.dni
    editarEmpleado.edad = empleado.edad
    isEditing.value = true;
}
</script>

<template>
    <div class="row">
        <div class="col col-10 ">
            <table v-if="empleados.length" class="table table-responsive table-striped">
                <thead>
                <tr class="table-secondary">
                    <th>#</th>
                    <th>Nombre</th>
                    <th>Apellido</th>
                    <th>DNI</th>
                    <th>Fecha de nacimiento</th>
                    <th>Departamento</th>
                    <th>Fecha de alta</th>
                    <th>Actualizado</th>
                    <th>Opciones</th>
                </tr>
                </thead>
                <tbody class="align-middle">
                <tr v-for="empleado in empleados.items" :key="empleado.id">
                    <td>{{ empleado.id }}</td>
                    <td>{{ empleado.nombre }}</td>
                    <td>{{ empleado.apellido }}</td>
                    <td>{{ empleado.dni }}</td>
                    <td>{{ empleado.edad }}</td>
                    <td>{{ empleado.departamento_nombre }}</td>
                    <td>{{ moment(empleado.created).format('LL, LTS') }}</td>
                    <td :title="moment(empleado.updated).format('LL, LTS')">
                        {{ moment(empleado.updated).fromNow() }}
                    </td>
                    <td>
                        <button class="btn btn-sm btn-warning me-1" title="Actualizar"
                                @click="startEditing(empleado)">
                            <i class="bi bi-pencil-square"></i>
                        </button>
                        <button class="btn btn-sm btn-danger" title="Borrar"
                                @click="empleados.delete(empleado)">
                            <i class="bi bi-trash"></i>
                        </button>
                    </td>
                </tr>
                </tbody>
            </table>
            <p v-else class="alert alert-warning">No hay datos, comprueba la consola para ver posibles errores.</p>
        </div>
        <div class="col col-2">
            <div v-if="isEditing">
                <h5>Editar Empleado</h5>
                <div class="row p-3">
                    <div class="card p-3 col-12">
                        <form @submit.prevent="saveChanges">
                            <div class="mb-3">
                                <label class="form-label" for="nombre">Nombre</label>
                                <input class="form-control" placeholder="nombre" id="nombre" type="text"
                                       @keyup.enter="botonPulsado()"
                                       v-model="editarEmpleado.nombre"/>
                                <p class="alert alert-warning mt-3" v-for="error of v$.nombre.$errors"
                                   :key="error.$uid">
                                    {{ error.$message }}
                                </p>
                            </div>
                            <div class="mb-3">
                                <label class="form-label" for="apellido">Apellido</label>
                                <input class="form-control" placeholder="apellido" id="apellido" type="text"
                                       @keyup.enter="botonPulsado()"
                                       v-model="editarEmpleado.apellido"/>
                                <p class="alert alert-warning mt-3" v-for="error of v$.apellido.$errors"
                                   :key="error.$uid">
                                    {{ error.$message }}
                                </p>
                            </div> <div class="mb-3">
                                <label class="form-label" for="dni">DNI</label>
                                <input class="form-control" placeholder="dni" id="dni" type="text"
                                       @keyup.enter="botonPulsado()"
                                       v-model="editarEmpleado.dni"/>
                                <p class="alert alert-warning mt-3" v-for="error of v$.dni.$errors"
                                   :key="error.$uid">
                                    {{ error.$message }}
                                </p>
                            </div>
                            <div class="mb-3">
                                <label class="form-label" for="edad">Edad</label>
                                <input class="form-control" placeholder="edad" id="edad" type="text"
                                       @keyup.enter="botonPulsado()"
                                       v-model="editarEmpleado.edad"/>
                                <p class="alert alert-warning mt-3" v-for="error of v$.edad.$errors" :key="error.$uid">
                                    {{ error.$message }}
                                </p>
                            </div>
                            <button class="btn btn-primary" :disabled="v$.$invalid" @click="botonPulsado()">Guardar
                            </button>
                            <button class="btn btn-link link-dark"  @click="limpiar()">
                                Cancelar
                            </button>
                        </form>
                    </div>
                </div>
            </div>
            <div v-if="!isEditing">
                <div class="col">
                    <div class="row">
                        <EmpleadoMenuAdmin/>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
</style>

