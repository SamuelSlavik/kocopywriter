<script setup lang="ts">

</script>

<template>
  <Container id="section-offer">
    <div class="section-offer">
      <h2>
        Píšu #kokotsky dobré texty
      </h2>
      <br/>

      <div>
        <h3>Jak?</h3>
        <p>
          Zapojuji kreativitu, psychologii prodeje a emoce. Pokaždé jinak, ale vždy se stejným výsledkem – zvýšením tržeb.
          Mé texty svou rozmanitostí připomínají seriál M*A*S*H.
          Jednou jsou neodolatelně pompézní jako major Winchester, podruhé okouzlí dětskou hravostí Hawkeyho Pierce a jindy si po vzoru Margaret neberou servítky.
          Nikdy jim ovšem nechybí jiskra, styl a lidskost plukovníka Pottera.
          A stejně jako parta z mobilní nemocnice dokážou zachránit i zdánlivě ztracené případy.
        </p>
      </div>

      <div>
        <h3>Kam?</h3>
        <p>
          Na weby, blogy, prodejní stránky i do kreativ, e-mailů a reklamních kampaní.
        </p>
      </div>

      <div>
        <h3>Za kolik?</h3>
        <p>
          Každý projekt naceňuji individuálně na základě sazby 1515 Kč/hod.<br/>
          <router-link to="/pricing">Orientační ceník</router-link>
        </p>
      </div>

      <div>
        <h3>Chcete je?</h3>
        <p>Napište mi na <a href="mailto:ko@kocopywriter.cz">ko@kocopywriter.cz</a></p>
      </div>
    </div>
  </Container>
</template>

<style>
#section-offer {
  margin-top: 6rem;
  margin-bottom: 3rem;
}

.section-offer {
  text-align: center;
  width: 100%;
  margin: auto;
  margin-top: 6rem;
  @media (max-width: 1024px) {
    margin-top: 0;
  }

  > div {
    margin-bottom: 1.5rem;
  }
}
</style>