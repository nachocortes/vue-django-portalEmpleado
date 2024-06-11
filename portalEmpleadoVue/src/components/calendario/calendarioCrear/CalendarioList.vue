<script setup>
import moment from "moment/min/moment-with-locales";
import {onMounted} from "vue";
import {useCalendarioStore} from "@/stores/calendarios.js";
import {useAuthStore} from "@/stores/auth.js";
import CalendarioMenuAdminCrearCalendario from "@/components/calendario/calendarioCrear/CalendarioMenuAdminCrearCalendario.vue";

moment.locale('es');

const calendarios = useCalendarioStore();
const auth = useAuthStore();

onMounted(() => {
    calendarios.fetch();
});

function goToDetail(calendario) {
    router.push({ name: 'CalendarioDetail', params: { id: calendario.id } });
}
</script>

<template>
    <div class="row mt-3">
        <div class="col col-10">
            <table v-if="calendarios.length" class="table table-responsive table-striped">
                <thead>
                <tr class="table-secondary">
                    <th>#</th>
                    <th>Ref</th>
                    <th>Nombre empleado</th>
                    <th>Año</th>
                    <th>Fecha de alta</th>
                    <th>Actualizado</th>
                    <th>Opciones</th>
                </tr>
                </thead>
                <tbody class="align-middle">
                <tr v-for="calendario in calendarios.items" :key="calendario.id">
                    <td>{{ calendario.id }}</td>
                    <td>{{ calendario.nombre }}</td>
                    <td>{{ calendario.empleado_nombre }}</td>
                    <td>{{ calendario.anio }}</td>
                    <td>{{ moment(calendario.created).format('LL, LTS') }}</td>
                    <td :title="moment(calendario.updated).format('LL, LTS')">
                        {{ moment(calendario.updated).fromNow() }}
                    </td>
                    <td>
                        <button class="btn btn-sm btn-success me-1" title="Ver"
                                @click="goToDetail(calendario)">
                            <i class="bi bi-eye-fill"></i>
                        </button>
                        <button class="btn btn-sm btn-danger" title="Borrar"
                                @click="calendarios.delete(calendario.id)">
                            <i class="bi bi-trash"></i>
                        </button>
                    </td>
                </tr>
                </tbody>
            </table>
            <p v-else class="alert alert-warning">No hay datos, comprueba la consola para ver posibles errores.</p>
        </div>
        <div class="col col-2">
            <div class="col">
                <div class="row">
                    <CalendarioMenuAdminCrearCalendario/>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
</style>
