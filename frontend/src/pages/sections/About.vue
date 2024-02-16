<script setup lang="ts">

</script>

<template>
  <Container id="section-about" class="section-about">
    <div class="section-about__content">
      <div>
        <h2>
          Čau-čau
        </h2>
        <br/>
        <p>
          Jsem kreativec, balbutik a člověk, který se nebere vážně.
          A postavil na tom byznys. Blbě mluvím, ale i díky tomu fakt dobře píšu.
          Moje HLPčko najdete třeba v rozhovoru pro časopis Finmag, takže zde ho vynechám.
        </p>
        <br/>
        <p>
          Bydlím v Sudetech, fandím Slavii, čtu knížky o sériových vrazích, chodím do sauny, miluju humor
          Rickyho Gervaise, buduju #kokotbrand na LinkedInu a od roku 2017
          jsem svými (dů)vtipnými texty obšťastnil & obohatil už více než 100 klientů.
        </p>
        <br/>
        <h3>
          Chcete taky #kokotsky dobré copy?
        </h3>
        <p>Napište mi na <a href="mailto:ko@kocopywriter.cz">ko@kocopywriter.cz</a></p>
      </div>
    </div>
    <div class="about-wallpaper">
      <img src="../../assets/images/wallpapers/w-2.jpg" alt="Logo" />
    </div>
  </Container>
</template>

<style>
.section-about {
  overflow-x: hidden;
}
.section-about__content {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  gap: 2rem;
  width: 50%;
  margin-left: 0;
  text-align: center;
  justify-content: center;
}
.about-wallpaper {
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