<script setup>
import moment from "moment/min/moment-with-locales";
import {onMounted, provide, reactive, ref} from 'vue';
import {required} from "@vuelidate/validators";
import useVuelidate from "@vuelidate/core";
import {useAuthStore} from "@/stores/auth.js";
import {useAusenciaStore} from "@/stores/ausencias.js";
import AusenciaAdmin from "@/components/ausencias/AusenciaAdmin.vue";

moment.locale('es');

const auth = useAuthStore();
const ausencias = useAusenciaStore();
const isEditing = ref(false);

onMounted(() => {
    ausencias.fetch();
});

function manejarGuardadoAusencia(ausencia) {
    ausencias.save(ausencia);
}

provide('guardarAusencia', manejarGuardadoAusencia);

const editarAusencia = reactive({
    id: 1,
    empleado: null,
    fecha: '',
    motivo: '',
    justificada: false,
});

const reglasValidacion = {
    fecha: {
        required,
    },
    motivo: {
        required,
    }
}

const v$ = useVuelidate(reglasValidacion, editarAusencia)

function botonPulsado() {
    const result = v$.value.$validate();
    result.then((valid) => {
        if (valid) {
            ausencias.update(editarAusencia);
            limpiar();
        }
    }).catch((error) => {
        console.log(error);
    })
}

function limpiar() {
    isEditing.value = false;
    editarAusencia.motivo = '';
    editarAusencia.fecha = '';
    editarAusencia.justificada = false;
    v$.value.$reset();
}

function startEditing(ausencia) {
    editarAusencia.id = ausencia.id
    editarAusencia.fecha = ausencia.fecha
    editarAusencia.motivo = ausencia.motivo
    editarAusencia.justificada = ausencia.justificada
    editarAusencia.empleado = ausencia.empleado
    isEditing.value = true;
}
</script>

<template>
    <div class="row mt-3">
        <div class="col col-10">
            <table v-if="ausencias.items.length" class="table table-responsive table-striped">
                <thead>
                <tr class="table-secondary">
                    <th>#</th>
                    <th>Nombre empleado</th>
                    <th>fecha</th>
                    <th>motivo</th>
                    <th>justificante</th>
                    <th>Creado</th>
                    <th>Actualizado</th>
                    <th v-if="auth.isAuthenticated">Opciones</th>

                </tr>
                </thead>
                <tbody class="align-middle">
                <tr v-for="ausencia in ausencias.items" :key="ausencia.id">
                    <td>{{ ausencia.id }}</td>
                    <td>{{ ausencia.empleado_nombre }}</td>
                    <td>{{ ausencia.fecha }}</td>
                    <td>{{ ausencia.motivo }}</td>
                    <td>{{ ausencia.justificada ? "Sí" : "No" }}</td>
                    <td>{{ moment(ausencia.created).format('LL, LTS') }}</td>
                    <td :title="moment(ausencia.updated).format('LL, LTS')">
                        {{ moment(ausencia.updated).fromNow() }}
                    </td>
                    <td v-if="auth.isAuthenticated">
                        <button class="btn btn-sm btn-warning me-1" title="Ver"
                                @click="startEditing(ausencia)">
                            <i class="bi bi-pencil-square"></i>
                        </button>
                        <button class="btn btn-sm btn-danger" title="Borrar"
                                @click="ausencias.delete(ausencia)">
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
                <h5>Editar ausencia</h5>
                <div class="row p-3">
                    <div class="card p-3 col-12">
                        <form @submit.prevent="saveChanges">
                            <div class="mb-3">
                                <label class="form-label" for="fecha">Fecha</label>
                                <input class="form-control" placeholder="fecha" id="fecha" type="text"
                                       @keyup.enter="botonPulsado()"
                                       v-model="editarAusencia.fecha"/>
                                <p class="alert alert-warning mt-3" v-for="error of v$.fecha.$errors"
                                   :key="error.$uid">
                                    {{ error.$message }}
                                </p>
                            </div>
                            <div class="mb-3">
                                <label class="form-label" for="motivo">Motivo</label>
                                <input class="form-control" placeholder="motivo" id="motivo"
                                       type="text"
                                       @keyup.enter="botonPulsado()"
                                       v-model="editarAusencia.motivo"/>
                                <p class="alert alert-warning mt-3" v-for="error of v$.motivo.$errors"
                                   :key="error.$uid">
                                    {{ error.$message }}
                                </p>
                            </div>
                            <div class="mb-3">
                                <input class="form-check-input" type="checkbox" id="justificada"
                                       v-model="editarAusencia.justificada">
                                <label class="form-check-label" for="justificada">Justificante</label>
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
                <AusenciaAdmin/>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
</style>
