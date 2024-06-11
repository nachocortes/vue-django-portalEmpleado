<script setup>
import moment from "moment/min/moment-with-locales";
import {onMounted, provide, reactive, ref} from 'vue';
import useVuelidate from "@vuelidate/core";
import {useAuthStore} from "@/stores/auth.js";
import {required} from "@vuelidate/validators";
import {usePermisoStore} from "@/stores/permisos.js";
import PermisoAdmin from "@/components/permisos/PermisoAdmin.vue";

moment.locale('es');

const auth = useAuthStore();
const permisos = usePermisoStore();
const isEditing = ref(false);

onMounted(() => {
    permisos.fetch();
});

function manejarGuardadoPermiso(permiso) {
    permisos.save(permiso);
}

provide('guardarPermiso', manejarGuardadoPermiso);

const editarPermiso = reactive({
    id: 1,
    empleado: null,
    fecha: '',
    causa: '',
    estado: false,
});

const reglasValidacion = {
    fecha: {
        required,
    },
    causa: {
        required,
    }
}

const v$ = useVuelidate(reglasValidacion, editarPermiso)

function botonPulsado() {
    const result = v$.value.$validate();
    result.then((valid) => {
        if (valid) {
            permisos.update(editarPermiso);
            limpiar();
        }
    }).catch((error) => {
        console.log(error);
    })
}

function limpiar() {
    isEditing.value = false;
    editarPermiso.causa = '';
    editarPermiso.fecha = '';
    editarAusencia.estado = false;
    v$.value.$reset();
}

function startEditing(permiso) {
    editarPermiso.id = permiso.id
    editarPermiso.fecha = permiso.fecha
    editarPermiso.causa = permiso.causa
    editarPermiso.estado = permiso.estado
    editarPermiso.empleado = permiso.empleado
    isEditing.value = true;
}
</script>

<template>
    <div class="row mt-3">
        <div class="col col-10">
            <table v-if="permisos.items.length" class="table table-responsive table-striped">
                <thead>
                <tr class="table-secondary">
                    <th>#</th>
                    <th>Nombre empleado</th>
                    <th>fecha</th>
                    <th>Causa</th>
                    <th>Estado</th>
                    <th>Creado</th>
                    <th>Actualizado</th>
                    <th v-if="auth.isAuthenticated">Opciones</th>
                </tr>
                </thead>
                <tbody class="align-middle">
                <tr v-for="permiso in permisos.items" :key="permiso.id">
                    <td>{{ permiso.id }}</td>
                    <td>{{ permiso.empleado_nombre }}</td>
                    <td>{{ permiso.fecha }}</td>
                    <td>{{ permiso.causa }}</td>
                    <td>{{ permiso.estado ? "Concedido" : "No Concedido" }}</td>
                    <td>{{ moment(permiso.created).format('LL, LTS') }}</td>
                    <td :title="moment(permiso.updated).format('LL, LTS')">
                        {{ moment(permiso.updated).fromNow() }}
                    </td>
                    <td v-if="auth.isAuthenticated">
                        <button class="btn btn-sm btn-warning me-1" title="Ver"
                                @click="startEditing(permiso)">
                            <i class="bi bi-pencil-square"></i>
                        </button>
                        <button class="btn btn-sm btn-danger" title="Borrar"
                                @click="permisos.delete(permiso)">
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
                <h5>Editar permiso</h5>
                <div class="row p-3">
                    <div class="card p-3 col-12">
                        <form @submit.prevent="saveChanges">
                            <div class="mb-3">
                                <label class="form-label" for="fecha">Fecha</label>
                                <input class="form-control" placeholder="fecha" id="fecha" type="text"
                                       @keyup.enter="botonPulsado()"
                                       v-model="editarPermiso.fecha"/>
                                <p class="alert alert-warning mt-3" v-for="error of v$.fecha.$errors"
                                   :key="error.$uid">
                                    {{ error.$message }}
                                </p>
                            </div>
                            <div class="mb-3">
                                <label class="form-label" for="causa">Causa</label>
                                <input class="form-control" placeholder="cuasa" id="causa"
                                       type="text"
                                       @keyup.enter="botonPulsado()"
                                       v-model="editarPermiso.causa"/>
                                <p class="alert alert-warning mt-3" v-for="error of v$.causa.$errors"
                                   :key="error.$uid">
                                    {{ error.$message }}
                                </p>
                            </div>
                            <div class="mb-3">
                                <input class="form-check-input" type="checkbox" id="estado"
                                       v-model="editarPermiso.estado">
                                <label class="form-check-label" for="estado">Estado</label>
                            </div>
                            <div class="mb-3">
                                <button class="btn btn-primary" :disabled="v$.$invalid" @click="botonPulsado()">Guardar
                                </button>
                                <button class="btn btn-link link-dark" @click="limpiar()">Cancelar</button>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
            <div v-if="!isEditing">
                <div class="col">
                    <div class="row" v-if="auth.isAuthenticated">
                        <PermisoAdmin/>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
</style>
