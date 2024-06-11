<script setup>
import 'v-calendar/style.css';
import {ref, provide, watchEffect} from 'vue';
import {useScreens} from 'vue-screen-utils';
import MiBotoneraNumeroMesesVer from "@/components/calendario/calendarioComponentes/CalendarBotonNumMeses.vue";
import MiDarkMode from "@/components/calendario/calendarioComponentes/CalendarioDarkMode.vue";
import CalendarioTipoDiaSelect from "@/components/calendario/calendarioComponentes/CalendarioTipoDiaSelect.vue";
import CalendarioSelector from "@/components/calendario/calendarioComponentes/CalendarioSelector.vue";
import {useCalendarioItemStore} from "@/stores/calendarioItems.js";
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
const calendarioId = ref(0)
const calendariohighlight = ref("");
const calendarioEmpleadoNombre = ref("");
const calendarAttrs = ref([]);
const fechasSeleccionadas = ref([]);
const tipoDia_fechaList = ref([]);
const mostrarFormulario = ref(false);
const seleccionandoCalendario = ref(true);

provide('tipoDia', tipoDia);
provide('updateTipoDia', updateTipoDia);
provide('miCalendario', miCalendario);
provide('updateCalendario', updateCalendario);

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

function mostrarCrearCalendario() {
    mostrarFormulario.value = true;
    seleccionandoCalendario.value = true;
}

function updateTipoDia(newTipoDia) {
    tipoDia.value = newTipoDia;
}

function updateCalendario(newCalendario) {
    miCalendario.value = newCalendario;
    calendarioId.value = newCalendario.id
    calendarioUrl.value = newCalendario.url;
    calendariohighlight.value = newCalendario.highlight;
    calendarioEmpleadoNombre.value = newCalendario.empleado.nombre;

    cargarDiasSeleccionados(newCalendario.id);

    seleccionandoCalendario.value = false;
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

async function cargarDiasSeleccionados(calendarioId) {
    if (!calendarioId) return;

        try {
            await calendarioItems.fetchItemsByCalendario(calendarioId);
            const items = calendarioItems.items;

            fechasSeleccionadas.value = [];
            calendarAttrs.value = [];
            tipoDia_fechaList.value = [];

            items.forEach(item => {
                const date = new Date(item.fecha);
                fechasSeleccionadas.value.push({
                    dates: date,
                    highlight: {
                        color: tipoDia_colorMap[item.tipo_dia] || 'gray',
                        backgroundColor: tipoDia_colorMap[item.tipo_dia] || 'gray',
                        borderRadius: '50%',
                    },
                });
                tipoDia_fechaList.value.push({fecha: item.fecha, tipoDia: item.tipo_dia});
                sumarDia(item.tipo_dia);
            });

            calendarAttrs.value = fechasSeleccionadas.value.map(attr => ({
                key: `highlight-${attr.dates.toISOString().split('T')[0]}`,
                ...attr,
            }));
        } catch (error) {
    }
}


function actuarEnDia(day) {
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
        fechasSeleccionadas.value.splice(dateIndex, 1);
        const tipoDiaIndex = tipoDia_fechaList.value.findIndex(item => item.fecha === dateStr);

        if (tipoDiaIndex !== -1) {
            const oldTipo = tipoDia_fechaList.value[tipoDiaIndex].tipoDia;
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
            id: calendarioId.value,
            fecha: item.fecha,
            tipo_dia: item.tipoDia,
            calendario: calendarioUrl.value
        };
        calendarioItems.update(nuevoCalendarioItem);
    }
    limpiar();
}

function limpiar() {
    isDark.value = true;
    mesesVerBotones.value = 1;
    columns.value = 1;
    rows.value = 1;
    tipoDia.value = "Laborables";
    miCalendario.value = null;
    calendarioUrl.value = "";
    calendariohighlight.value = "";
    calendarAttrs.value = [];
    fechasSeleccionadas.value = [];
    tipoDia_fechaList.value = [];
    mostrarFormulario.value = false;
    seleccionandoCalendario.value = true;
    limpiarContadores();
}

</script>

<template>
    <div class="row mt-3">
        <div class="col-9 text-center" v-if="!miCalendario">
        </div>
        <div class="col-9 text-center" v-if="miCalendario">
            <div class="row">
                <div class="col-10 d-flex justify-content-center mt-2">
                    <MiBotoneraNumeroMesesVer @update:numeroMeses="mesesVerBotones = $event"/>
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
        <div class="col col-3">
            <div class="col-12">
                <nav class="d-flex flex-column flex-shrink-0 p-1 bg-body-tertiary ancho-navegacion">
                    <ul class="nav nav-pills flex-column mb-auto">
                        <li class="nav-item">
                            <button @click="mostrarCrearCalendario"
                                    class="nav-link nav-link{{ mostrarFormulario ? '-primary' : '' }} text-start">
                                <i class="bi bi-house me-2"></i>
                                <span>{{ mostrarFormulario ? 'Ocultar Formulario' : 'Editar calendario' }}</span>
                            </button>
                        </li>
                    </ul>
                </nav>
                <div v-if="mostrarFormulario" class="mt-3">
                    <div class="row p-3 m-3">
                        <div class="card p-3 col-12">
                            <div class="row mb-3" v-if="seleccionandoCalendario">
                                <CalendarioSelector @updateCalendario="updateCalendario"/>
                            </div>
                            <div class="row mb-3 ms-3 me-3" v-if="!seleccionandoCalendario">
                                <CalendarioTipoDiaSelect @updateTipoDia="updateTipoDia"/>
                            </div>
                            <div class="row my-4 ms-4 me-4 text-center" v-if="!seleccionandoCalendario">
                                <button class="btn btn-primary" @click="botonPulsado">Guardar</button>
                                <button class="btn btn-link link-dark" @click="limpiar">Cancelar</button>
                            </div>
                        </div>
                    </div>
                    <div class="col-12" v-if="miCalendario">
                        <div class="row row-12 p-3 m-3">
                            <div class="card p-3 col-12 ">
                                <div class="row mb-3">
                                    <h6 class="text-black">Totales: {{ totales }}</h6>
                                </div>
                                <div class="row mb-3">
                                    <h6 class="text-primary">Laborables: {{ laborables }}</h6>
                                </div>
                                <div class="row mb-3">
                                    <h6 class="text-danger">Festivos: {{ festivos }}</h6>
                                </div>
                                <div class="row mb-3">
                                    <h6 class="text-warning">Vacaciones: {{ vacaciones }}</h6>
                                </div>
                                <div class="row mb-3">
                                    <h5 class="text-success">ILT: {{ ilt }}</h5>
                                </div>
                                <div class="row mb-3">
                                    <h6 class="text-danger">Libre disposicion: {{ libreDisposicion }}</h6>
                                </div>
                                <div class="row mb-3">
                                    <h6 class="text-danger">Ausencias justificadas: {{ ausenciasJustificadas }}</h6>
                                </div>
                                <div class="row mb-3">
                                    <h6 class="text-black-50">Ausencias sin justificar: {{
                                            ausenciasSinJustificadas
                                        }}</h6>
                                </div>
                                <div class="row mb-3">
                                    <h6 class="text-info">Otros: {{ otros }}</h6>
                                </div>
                            </div>
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
