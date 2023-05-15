<script setup>
import { RouterLink, RouterView } from "vue-router";
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.bundle.min.js';
import 'bootstrap-icons/font/bootstrap-icons.css';

document.title = "KahootClone Game"
</script>

<template class="min-vh-100">
  <audio controls loop autoplay hidden>
    <source src="/lobby.mp3" type="audio/mpeg">
    Your browser does not support the audio element.
  </audio>
  <RouterView />
</template>

<style scoped>
</style>
