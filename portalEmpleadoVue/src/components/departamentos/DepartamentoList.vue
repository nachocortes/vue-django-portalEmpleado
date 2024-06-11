<script setup>
import moment from "moment/min/moment-with-locales";
import useVuelidate from "@vuelidate/core";
import {integer, minLength, required} from "@vuelidate/validators";
import {ref, onMounted, reactive} from "vue";
import {useDepartamentoStore} from "@/stores/departamentos.js";
import {useAuthStore} from "@/stores/auth.js";
import DepartamentoMenuAdmin from "@/components/departamentos/DepartamentoMenuAdmin.vue";

moment.locale('es');

const departamentos = useDepartamentoStore()
const auth = useAuthStore();
const isEditing = ref(false);


onMounted(() => {
    departamentos.fetch();
});

const editarDepartamento = reactive({
    id: 1,
    nombre: '',
    telefono: 1,
});

const reglasValidacion = {
    nombre: {
        required,
        minLength: minLength(3),
    },
    telefono: {
        required,
        minLength: minLength(3),
        integer,
    }
}

const v$ = useVuelidate(reglasValidacion, editarDepartamento)

function botonPulsado() {
    const result = v$.value.$validate();
    result.then((valid) => {
        if (valid) {
            departamentos.update(editarDepartamento);
            limpiar();
        }
    }).catch((error) => {
        console.log(error);
    })
}

function limpiar() {
    isEditing.value = false;
    editarDepartamento.nombre = '';
    editarDepartamento.telefono = 1;
    editarDepartamento.id = 1;
    v$.value.$reset();
}

function startEditing(departamento) {
    editarDepartamento.id = departamento.id
    editarDepartamento.nombre = departamento.nombre
    editarDepartamento.telefono = departamento.telefono
    isEditing.value = true;
}
</script>

<template>
    <div class="row">
        <div class="col col-10">
            <table v-if="departamentos.length" class="table table-responsive table-striped">
                <thead>
                <tr class="table-secondary">
                    <th>#</th>
                    <th>Nombre</th>
                    <th>Teléfono</th>
                    <th>Fecha de alta</th>
                    <th>Actualizado</th>
                    <th>Opciones</th>
                    <th v-if="auth.isAuthenticated"></th>
                </tr>
                </thead>
                <tbody class="align-middle">
                <tr v-for="departamento in departamentos.items" :key="departamento.id">
                    <td>{{ departamento.id }}</td>
                    <td>{{ departamento.nombre }}</td>
                    <td>{{ departamento.telefono }}</td>
                    <td>{{ moment(departamento.created).format('LL, LTS') }}</td>
                    <td :title="moment(departamento.updated).format('LL, LTS')">
                        {{ moment(departamento.updated).fromNow() }}
                    </td>
                    <td>
                        <button class="btn btn-sm btn-warning me-1" title="Actualizar"
                                @click="startEditing(departamento)">
                            <i class="bi bi-pencil-square"></i>
                        </button>
                        <button class="btn btn-sm btn-danger" title="Borrar"
                                @click="departamentos.delete(departamento)">
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
                <h5>Editar Departamento</h5>
                <div class="row p-3">
                    <div class="card p-3 col-12">
                        <form @submit.prevent="saveChanges">
                            <div class="mb-3">
                                <label class="form-label" for="nombre">Nombre</label>
                                <input class="form-control" placeholder="nombre" id="nombre" type="text"
                                       @keyup.enter="botonPulsado()"
                                       v-model="editarDepartamento.nombre"/>
                                <p class="alert alert-warning mt-3" v-for="error of v$.nombre.$errors"
                                   :key="error.$uid">
                                    {{ error.$message }}
                                </p>
                            </div>
                            <div class="mb-3">
                                <label class="form-label" for="telefono">Telefono</label>
                                <input class="form-control" placeholder="telefono" id="telefono" type="text"
                                       @keyup.enter="botonPulsado()"
                                       v-model="editarDepartamento.telefono"/>
                                <p class="alert alert-warning mt-3" v-for="error of v$.telefono.$errors"
                                   :key="error.$uid">
                                    {{ error.$message }}
                                </p>
                            </div>
                            <button class="btn btn-primary" :disabled="v$.$invalid" @click="botonPulsado()">Guardar</button>
                            <button class="btn btn-link link-dark" @click="limpiar()">Cancelar</button>
                        </form>
                    </div>
                </div>
            </div>
            <div v-if="!isEditing">
                <div class="col">
                    <div class="row">
                        <DepartamentoMenuAdmin/>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
</style>

