<script setup>
import NavBar from "@/components/NavBar.vue";
import Menu from "@/components/Menu.vue";
import Footer from "@/components/Footer.vue";
</script>

<template>
  <NavBar/>
  <div class="container-fluid" id="fondo1">
    <div class="row" id="fondo">
      <div class="col-auto">
        <Menu class="my-3 ms-1"/>
      </div>
      <div class="col">
        <RouterView class="my3"/>
      </div>
    </div>
  </div>
  <Footer/>
</template>

<style scoped>
#fondo1 {
    background-color: #edebe8;
  margin: 0;
}
</style>
