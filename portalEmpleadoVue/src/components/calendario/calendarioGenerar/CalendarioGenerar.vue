<script setup>
import 'v-calendar/style.css';
import {ref, provide, watchEffect} from 'vue';
import {useScreens} from 'vue-screen-utils';
import {useCalendarioItemStore} from "@/stores/calendarioItems.js";
import CalendarBotonNumMeses from "@/components/calendario/calendarioComponentes/CalendarBotonNumMeses.vue";
import MiDarkMode from "@/components/calendario/calendarioComponentes/CalendarioDarkMode.vue";
import CalendarioTipoDiaSelect from "@/components/calendario/calendarioComponentes/CalendarioTipoDiaSelect.vue";
import CalendarioFromGenerar from "@/components/calendario/calendarioGenerar/CalendarioFromGenerar.vue";
import {
    laborables,
    festivos,
    vacaciones,
    ilt,
    libreDisposicion,
    ausenciasJustificadas,
    ausenciasSinJustificadas,
    otros,
    totales,
    sumarDia,
    restarDia,
    limpiarContadores,
} from '@/utils/contadorDias.js';

const calendarioItems = useCalendarioItemStore();

const {mapCurrent} = useScreens({
    xs: '0px',
    sm: '640px',
    md: '768px',
    lg: '1024px',
});


const expanded = mapCurrent({lg: true}, true);
const isDark = ref(true);
const calendar = ref(null);
const mesesVerBotones = ref(1);
const columns = ref(1);
const rows = ref(1);
const tipoDia = ref("Laborables");
const miCalendario = ref(null);
const calendarioUrl = ref("");
const calendariohighlight = ref("");
const calendarioEmpleadoNombre = ref("");
const calendarAttrs = ref([]);
const fechasSeleccionadas = ref([]);
const tipoDia_fechaList = ref([]);
const mostrarFormulario = ref(false);
const mostrarFormularioItems = ref(false);
const seleccionandoYear = ref(true);
const mostrarCalendarioForm = ref(false);
const mostrarTipoDiaSelectForm = ref(false);

const tipoDia_colorMap = {
    'Laborables': "blue",
    'Festivos': 'red',
    'Vacaciones': 'yellow',
    'ILT': 'green',
    'Libre disposicion': 'orange',
    'Ausencias justificadas': 'purple',
    'Ausencias sin justificar': 'gray',
    'Otros': 'pink',
};

provide('tipoDia', tipoDia);
provide('updateTipoDia', updateTipoDia);

function updateTipoDia(newTipoDia) {
    tipoDia.value = newTipoDia;
}

function seleccionarDias() {
    mostrarFormularioItems.value = true;
}

function moverAHoy() {
    calendar.value.move(new Date());
}

watchEffect(() => {
    if (mesesVerBotones.value === 4) {
        columns.value = 2;
        rows.value = 2;
    } else if (mesesVerBotones.value === 6) {
        columns.value = 3;
        rows.value = 3;
    } else if (mesesVerBotones.value === 12) {
        columns.value = 3;
        rows.value = 4;
    } else if (mesesVerBotones.value === 24) {
        columns.value = 3;
        rows.value = 8;
    } else {
        columns.value = mesesVerBotones.value;
        rows.value = 1;
    }
});

async function actuarEnDia(day) {
    const tipo = tipoDia.value || 'Laborables';
    const color = tipoDia_colorMap[tipo];
    const dateStr = day.date.toISOString().split('T')[0];
    const dateIndex = fechasSeleccionadas.value.findIndex(attr => attr.dates.toISOString().split('T')[0] === dateStr);

    if (dateIndex === -1) {
        fechasSeleccionadas.value.push({
            dates: day.date,
            highlight: {
                color: color,
                backgroundColor: color,
                borderRadius: '50%',
            },
        });

        tipoDia_fechaList.value.push({fecha: dateStr, tipoDia: tipo});
        sumarDia(tipo);

    } else {

        const tipoDiaIndex = tipoDia_fechaList.value.findIndex(item => item.fecha === dateStr);
        if (tipoDiaIndex !== -1) {
            const oldTipo = tipoDia_fechaList.value[tipoDiaIndex].tipoDia;
            fechasSeleccionadas.value.splice(dateIndex, 1);
            tipoDia_fechaList.value.splice(tipoDiaIndex, 1);
            restarDia(oldTipo);
        }
    }

    calendarAttrs.value = fechasSeleccionadas.value.map(attr => ({
        key: `highlight-${attr.dates.toISOString().split('T')[0]}`,
        ...attr,
    }));
}

function botonPulsado() {
    const validItems = tipoDia_fechaList.value.filter(item => item.fecha && item.tipoDia);

    for (const item of validItems) {
        const nuevoCalendarioItem = {
            fecha: item.fecha,
            tipo_dia: item.tipoDia,
            calendario: calendarioUrl.value
        };

        calendarioItems.save(nuevoCalendarioItem);
    }
    limpiar();
}

function limpiar() {
    tipoDia.value = "Laborables";
    miCalendario.value = null;
    calendarioUrl.value = "";
    calendariohighlight.value = "";
    calendarAttrs.value = [];
    fechasSeleccionadas.value = [];
    tipoDia_fechaList.value = [];
    mostrarFormulario.value = false;
    seleccionandoYear.value = true;
    mostrarCalendarioForm.value = false;
    mostrarTipoDiaSelectForm.value = false;
    limpiarContadores();

}
</script>

<template>
    <div class="row mt-3">
        <div class="col-9 text-center">
            <div class="row">
                <div class="col-10 d-flex justify-content-center mt-2">
                    <CalendarBotonNumMeses @update:numeroMeses="mesesVerBotones = $event"/>
                </div>
                <div class="col-2 text-center mt-3">
                    <MiDarkMode @update:modoOscuro="isDark = $event"/>
                </div>
            </div>
            <VCalendar class="my-5"
                       :columns="columns"
                       :rows="rows"
                       :is-dark="isDark"
                       :attributes="calendarAttrs"
                       ref="calendar"
                       @dayclick="actuarEnDia">
                <template #footer>
                    <div class="w-full px-4 pb-3 items-center">
                        <button class="diaActual bg-secondary hover:bg-blue text-white w-full px-3 pt-1 rounded-md"
                                @click="moverAHoy">
                            Hoy
                        </button>
                    </div>
                </template>
            </VCalendar>
        </div>
        <div class="col-3">
            <nav class="d-flex flex-column flex-shrink-0 p-1 bg-body-tertiary ancho-navegacion">
                <ul class="nav nav-pills flex-column mb-auto">
                    <li class="nav-item">
                        <button @click="mostrarCalendarioForm = true; mostrarTipoDiaSelectForm = false"
                                class="nav-link nav-link{{ mostrarCalendarioForm ? '-primary' : '' }} text-start">
                            <i class="bi bi-house me-2"></i>
                            <span>{{ mostrarCalendarioForm ? 'Ocultar Formulario' : 'Generar calendario' }}</span>
                        </button>
                    </li>
                </ul>
            </nav>
            <div v-if="mostrarCalendarioForm" class="mt-3">
                <div class="row p-3">
                    <div class="card p-3 col-12">
                        <CalendarioFromGenerar @updateDias="seleccionarDias"
                                               @calendario-seleccionado="calendarioUrl = $event"/>
                        <div class="row mb-3 me-2 text-center">
                            <button class="btn btn-link link-dark"
                                    @click="mostrarCalendarioForm = false; mostrarTipoDiaSelectForm = true">Siguiente
                            </button>
                        </div>
                    </div>
                </div>
            </div>
            <div v-if="mostrarTipoDiaSelectForm" class="mt-3">
                <div class="row p-3">
                    <div class="card p-3 col-12">
                        <div class="row mb-3">
                            <CalendarioTipoDiaSelect :miCalendario="miCalendario"/>
                        </div>
                        <div class="row mb-3 me-2 text-center">
                            <button class="btn btn-primary" @click="botonPulsado">Guardar</button>
                            <button class="btn btn-link link-dark" @click="limpiar">Cancelar</button>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col-12">
                <div class="row row-12 p-3">
                    <div class="card p-3 col-12">
                        <div class="row mb-3">
                            <h5 class="text-black">Totales {{ totales }}</h5>
                        </div>
                        <div class="row mb-3">
                            <h5 class="text-primary">Laborables {{ laborables }}</h5>
                        </div>
                        <div class="mb-3">
                            <h5 class="text-danger">festivos {{ festivos }}</h5>
                        </div>
                        <div class="mb-3">
                            <h5 class="text-warning">Vacaciones {{ vacaciones }}</h5>
                        </div>
                        <div class="mb-3">
                            <h5 class="text-success">ILT {{ ilt }}</h5>
                        </div>
                        <div class="mb-3">
                            <h5 class="text-danger">Libre disposicion {{ libreDisposicion }}</h5>
                        </div>
                        <div class="mb-3">
                            <h5 class="text-danger">Ausencias justificadas {{ ausenciasJustificadas }}</h5>
                        </div>
                        <div class="mb-3">
                            <h5 class="text-black-50">Ausencias sin justificar {{ ausenciasSinJustificadas }}</h5>
                        </div>
                        <div class="mb-3">
                            <h5 class="text-info">Otros {{ otros }}</h5>
                        </div>
                    </div>
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
