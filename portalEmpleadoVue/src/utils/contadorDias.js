import { ref } from 'vue';

const laborables = ref(0);
const festivos = ref(0);
const vacaciones = ref(0);
const ilt = ref(0);
const libreDisposicion = ref(0);
const ausenciasJustificadas = ref(0);
const ausenciasSinJustificadas = ref(0);
const otros = ref(0);
const totales = ref(0);

function sumarDia(tipo) {
    if (tipo === "Laborables") {
        laborables.value++;
    } else if (tipo === "Festivos") {
        festivos.value++;
    } else if (tipo === "Vacaciones") {
        vacaciones.value++;
    } else if (tipo === "ILT") {
        ilt.value++;
    } else if (tipo === "Libre disposicion") {
        libreDisposicion.value++;
    } else if (tipo === "Ausencias justificadas") {
        ausenciasJustificadas.value++;
    } else if (tipo === "Ausencias sin justificar") {
        ausenciasSinJustificadas.value++;
    } else if (tipo === "Otros") {
        otros.value++;
    }
    totales.value++;
}

function restarDia(tipo) {
    if (tipo === "Laborables") {
        laborables.value--;
    } else if (tipo === "Festivos") {
        festivos.value--;
    } else if (tipo === "Vacaciones") {
        vacaciones.value--;
    } else if (tipo === "ILT") {
        ilt.value--;
    } else if (tipo === "Libre disposicion") {
        libreDisposicion.value--;
    } else if (tipo === "Ausencias justificadas") {
        ausenciasJustificadas.value--;
    } else if (tipo === "Ausencias sin justificar") {
        ausenciasSinJustificadas.value--;
    } else if (tipo === "Otros") {
        otros.value--;
    }
    totales.value--;
}

function limpiarContadores() {
    laborables.value = 0;
    festivos.value = 0;
    vacaciones.value = 0;
    ilt.value = 0;
    libreDisposicion.value = 0;
    ausenciasJustificadas.value = 0;
    ausenciasSinJustificadas.value = 0;
    otros.value = 0;
    totales.value = 0;
}

export {
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
};
