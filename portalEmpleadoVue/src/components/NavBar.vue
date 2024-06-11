<script setup>
import Login from "@/components/Login.vue";
</script>

<template>
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary pt-2 px-2">
        <div class="container-fluid">
            <RouterLink class="navbar-brand" to="/">
                <i class="bi bi-house me-2"></i>
                <span>Home</span>
            </RouterLink>
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <li class="nav-item">
                <RouterLink class="nav-link" to="/calendarios">
                    <i class="bi bi-building me-2"></i>
                    <span>calendarios</span>
                </RouterLink>
            </li>
            <li class="nav-item">
                <RouterLink class="nav-link" to="/departamentos">
                    <i class="bi bi-hand-thumbs-up me-2"></i>
                    <span>departamentos</span>
                </RouterLink>
            </li>
            <li class="nav-item">
                <RouterLink class="nav-link" to="/empleados">
                    <i class="bi bi-hand-thumbs-up me-2"></i>
                    <span>empleados</span>
                </RouterLink>
            </li>
            <li class="nav-item">
                <RouterLink class="nav-link" to="/ausencias">
                    <i class="bi bi-person me-2"></i>
                    <span>Ausencias</span>
                </RouterLink>
            </li>
            <li class="nav-item">
                <RouterLink class="nav-link" to="/permisos">
                    <i class="bi bi-person me-2"></i>
                    <span>Permisos</span>
                </RouterLink>
            </li>
        </ul>
        <button class="navbar-toggler border-0 text-light" type="button"
                data-bs-toggle="collapse"
                data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent"
                aria-expanded="false" aria-label="Navegación">
            <i class="bi bi-list"></i>
        </button>
        <div class="collapse navbar-collapse mx-3" id="navbarSupportedContent">
            <ul class="navbar-nav ms-auto">
                <Login/>
            </ul>
        </div>
        </div>
    </nav>
</template>

<style scoped>

</style>
