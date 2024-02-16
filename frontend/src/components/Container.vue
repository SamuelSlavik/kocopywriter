<script setup lang="ts">

</script>

<template>
  <div class="container">
    <slot />
  </div>
</template>

<style>
.container {
  width: 100%;
  max-width: var(--breakpoint);
  margin: 0 auto;
  padding: 1rem 1rem;
  font-weight: normal;
  position: relative;
}
</style>
