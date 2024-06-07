<script setup lang="ts">

</script>

<template>
  <Container id="section-about" class="section-about">
    <div class="about-wallpaper">
      <img src="../../assets/images/wallpapers/w-2.jpg" alt="Logo" />
    </div>
    <div class="section-about__content">
      <div>
        <h2>
          Čau-čau
        </h2>
        <br/>
        <p>
          Jsem kreativec, balbutik a člověk, který se nebere vážně.
          A postavil na tom byznys. Blbě mluvím, ale i díky tomu výborně píšu.
          Moje HLPčko najdete třeba v <a target="_blank" href="https://www.finmag.cz/inspirace/439170-koktam-no-a-co-copywriter-si-na-nedostatku-postavil-uspesnou-karieru">rozhovoru</a> pro časopis Finmag, takže zde ho vynechám.
        </p>
        <br/>
        <p>
          Miluju černobílé filmy, brakovou literaturu, čínské psy a americký fotbal. Ve volném čase provozuju smažákovou turistiku, buduju #kokotbrand na
          <a href="https://www.linkedin.com/in/vojtechhulinsky/" target="_blank">LinkedInu</a> a vyhlížím comeback Oasis.
        </p>
        <br/>
        <p>Jo a od roku 2017 jsem svými (dů)vtipnými texty obohatil už více než 100 klientů. Přidejte se k nim.</p>
      </div>
    </div>
  </Container>
</template>

<style>
.section-about {
  @media (max-width: 1024px) {
    display: flex;
    flex-direction: column;
    margin: 3rem 0;
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
    @media (max-width: 1024px) {
      width: 100%;
      min-height: auto;
    }
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
      @media (max-width: 1024px) {
        position: relative;
        width: 100%;
        left: auto;
        top: auto;
        transform: none;
      }
    }
  }
}
</style>