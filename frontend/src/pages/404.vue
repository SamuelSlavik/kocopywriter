<script lang="ts" setup>

</script>

<template>
  <Container class="section-404">
    <div>
      <h2>Tato stránka neexistuje</h2>
      <p>Přejděte na <router-link to="/">homepage</router-link>, ze které se snadno dostanete tam, kam budete chtít.</p>
    </div>
  </Container>
</template>

<style>
.section-404 {
  min-height: 100vh;
  display: flex;
  justify-content: center;
  flex-direction: column;
}
</style>