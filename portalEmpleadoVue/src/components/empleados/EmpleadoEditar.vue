<script setup>

</script>

<template>
    <h3>Editar Empleado</h3>
    <form @submit.prevent="saveChanges">
        <div class="mb-3">
            <label for="nombre" class="form-label">Nombre</label>
            <input type="text" class="form-control" id="nombre" v-model="selectedEmpleado.nombre">
        </div>
        <div class="mb-3">
            <label for="apellido" class="form-label">Apellido</label>
            <input type="text" class="form-control" id="apellido" v-model="selectedEmpleado.apellido">
        </div>
        <div class="mb-3">
            <label for="edad" class="form-label">Edad</label>
            <input type="number" class="form-control" id="edad" v-model="selectedEmpleado.edad">
        </div>
        <div class="mb-3">
            <label for="departamento_nombre" class="form-label">Departamento</label>
            <input type="text" class="form-control" id="departamento_nombre"
                   v-model="selectedEmpleado.departamento_nombre">
        </div>
        <button type="submit" class="btn btn-primary">Guardar cambios</button>
        <button type="button" class="btn btn-secondary" @click="cancelEditing">Cancelar</button>
    </form>
</template>

<style scoped>

</style>
