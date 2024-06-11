<script>

</script>

<template>
  <nav class="d-flex flex-column flex-shrink-0 p-3 bg-body-tertiary ancho-navegacion">
    <ul class="nav nav-pills flex-column mb-auto ">
      <li class="nav-item">
          <RouterLink class="nav-link" to="/">
              <i class="bi bi-house me-2"></i>
              <span>Home</span>
          </RouterLink>
        <RouterLink class="nav-link text-start" to="/departamentos">
          <i class="bi bi-building me-2"></i>
          <span>Departamentos</span>
        </RouterLink>
        <RouterLink class="nav-link text-start" to="/empleados">
          <i class="bi bi-person me-2"></i>
          <span>Empleados</span>
        </RouterLink>
        <RouterLink class="nav-link text-start" to="/calendarios">
          <i class="bi bi-person me-2"></i>
          <span>Calendarios</span>
        </RouterLink>
        <RouterLink class="nav-link text-start" to="/calendarioVer">
          <i class="bi bi-person me-2"></i>
          <span>Ver calendario</span>
        </RouterLink>
        <RouterLink class="nav-link text-start" to="/calendarioGenerar">
          <i class="bi bi-person me-2"></i>
          <span>Generar calendario</span>
        </RouterLink>
        <RouterLink class="nav-link text-start" to="/calendarioEditar">
          <i class="bi bi-person me-2"></i>
          <span>Editar calendario</span>
        </RouterLink>
        <RouterLink class="nav-link text-start" to="/permisos">
          <i class="bi bi-person me-2"></i>
          <span>Permisos</span>
        </RouterLink>
        <RouterLink class="nav-link text-start" to="/ausencias">
          <i class="bi bi-person me-2"></i>
          <span>Ausencias</span>
        </RouterLink>
      </li>
    </ul>
  </nav>
</template>

<style scoped>
.ancho-navegacion {
  width: 15em;
}
</style>
