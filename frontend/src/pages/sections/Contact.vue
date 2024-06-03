<script setup lang="ts">
</script>

<template>
  <div class="contact-background" id="section-contact">
    <!--<img src="@/assets/images/wallpapers/contact-background.jpeg" class="contact-background"/>-->
    <Container
        class="section-contact"
    >
      <!--style="background-image: url('src/assets/images/logos/logo.png')"-->
      <div class="section-contact__content">
        <h2>
          Chcete originální prodejní texty,<br/>
          než řeknu š-š-švec?
        </h2>
        <p>Napište mi na <a href="mailto:ko@kocopywriter.cz">ko@kocopywriter.cz</a></p>
      </div>
      <!--
      <div class="section-contact__background">
        <img src="../../assets/images/logos/logo.png" alt="Logo" />
      </div>
      -->
      <!--
      <div class="contact-wallpaper">
        <img src="../../assets/images/wallpapers/w-4.jpg" alt="Logo" />
      </div>
      -->
    </Container>
  </div>
</template>

<style>
.contact-background {
  position: relative;
  width: 100%;
  height: 100%;
}
.contact-background::before {
  content: "";
  position: absolute;
  top: 0; left: 0;
  width: 100%;
  height: 100%;
  background-image: url('@/assets/images/wallpapers/contact-background.jpeg');
  background-repeat: no-repeat;
  background-position: center;
  background-size: cover;
  opacity: 0.2;
}
.section-contact {
  overflow-x: hidden;
}
.section-contact__background {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-30%, -50%);
  z-index: -1;
  opacity: 0.1;

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
  margin-bottom: 0;
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