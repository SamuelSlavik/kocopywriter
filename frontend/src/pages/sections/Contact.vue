<script setup lang="ts">

</script>

<template>
  <Container id="section-contact" class="section-contact">
    <div class="section-contact__content">
      <h2>
        Chcete originální prodejní texty,<br/>
        než řeknu š-š-švec?
      </h2>
      <p>Napište mi na <a href="mailto:ko@kocopywriter.cz">ko@kocopywriter.cz</a></p>
    </div>
    <div class="contact-wallpaper">
      <img src="../../assets/images/wallpapers/w-4.jpg" alt="Logo" />
    </div>
  </Container>
</template>

<style>
.section-contact {
  overflow-x: hidden;
}
.section-contact__content {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  height: auto;
  gap: 2rem;
  width: 50%;
  margin-left: 0;
  text-align: left;
  justify-content: center;
}
.contact-wallpaper {
  img {
    width: 100%;
    left: 25%;
    height: auto;
    position: absolute;
    z-index: -1;
    top: 50%;
    transform: translateY(-50%);
  }
}
</style>