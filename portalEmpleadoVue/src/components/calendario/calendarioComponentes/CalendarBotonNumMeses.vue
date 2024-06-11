<script setup>
import {ref} from "vue";

const emit = defineEmits(['update:numeroMeses']);
const mesesVerBotones = ref(1);


function numeroMeses(month) {
    mesesVerBotones.value = month;
    emit('update:numeroMeses', mesesVerBotones.value);
}
</script>

<template>
    <div class="button-group-vertical bg-body-tertiary ">
        <div class="btn-group" role="group" aria-label="Basic radio toggle button group">
            <input type="radio" class="btn-check" name="btnradio" id="btnradio1" autocomplete="off" checked
                   @click="numeroMeses(1)">
            <label class="btn btn-outline-primary" for="btnradio1">1 mes</label>

            <input type="radio" class="btn-check" name="btnradio" id="btnradio2" autocomplete="off"
                   @click="numeroMeses(2)">
            <label class="btn btn-outline-primary" for="btnradio2">2 meses</label>

            <input type="radio" class="btn-check" name="btnradio" id="btnradio3" autocomplete="off"
                   @click="numeroMeses(3)">
            <label class="btn btn-outline-primary" for="btnradio3">3 meses</label>

            <input type="radio" class="btn-check" name="btnradio" id="btnradio4" autocomplete="off"
                   @click="numeroMeses(4)">
            <label class="btn btn-outline-primary" for="btnradio4">4 meses</label>

            <input type="radio" class="btn-check" name="btnradio" id="btnradio6" autocomplete="off"
                   @click="numeroMeses(6)">
            <label class="btn btn-outline-primary" for="btnradio6">6 meses</label>

            <input type="radio" class="btn-check" name="btnradio" id="btnradio12" autocomplete="off"
                   @click="numeroMeses(12)">
            <label class="btn btn-outline-primary" for="btnradio12">12 meses</label>

            <input type="radio" class="btn-check" name="btnradio" id="btnradio24" autocomplete="off"
                   @click="numeroMeses(24)">
            <label class="btn btn-outline-primary" for="btnradio24">24 meses</label>
        </div>
    </div>
</template>

<style scoped>
.button-group-vertical {
    display: flex;
    gap: 10px;
    margin-bottom: 20px;
}
</style>
