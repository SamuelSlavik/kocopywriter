<script setup lang="ts"></script>

<template>
  <div class="contact-background" id="section-contact">
    <Container
        class="section-contact"
    >
      <div class="section-contact__content">
        <div class="section-contact__text">
          <h2>
            Buďte kontrastní <br/><br/>Buďte vidět <br/><br/>Buďte první volbou
          </h2>
          <div class="section-contact__email">
            <a href="mailto:ko@kocopywriter.cz">
              <img class="section-contact__logo" alt="logo" src="@/assets/images/logos/logo-white.png" />
            </a>
            <a href="mailto:ko@kocopywriter.cz">
              ko@kocopywriter.cz
            </a>
          </div>
        </div>
      </div>
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
  opacity: 0.1;
}
.section-contact {
  overflow-x: hidden;
}
.section-contact__content {
  display: flex;
  min-height: 100vh;
  height: auto;
  gap: 2rem;
  width: fit-content;
  text-align: left;
  flex-direction: column;
  justify-content: center;
  margin-bottom: 0;
  flex-wrap: wrap;
  margin-left: auto;
  margin-right: auto;

  .section-contact__text {
    display: flex;
    flex-direction: column;
    justify-content: center;
    text-align: left;
    width: fit-content;
    gap: 2rem;
    @media (max-width: 1024px) {
      width: 100%;
    }
  }
  .section-contact__email {
    display: flex;
    gap: 1rem;
    margin-top: 2rem;

    * {
      margin-top: auto;
      margin-bottom: auto;
    }
  }
  .section-contact__logo {
    height: 24px;
    width: auto;
  }
}
</style>