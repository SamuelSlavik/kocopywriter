<script setup lang="ts">

</script>

<template>
  <Container id="section-offer">
    <div class="section-offer">
      <h2>
        Píšu fakt dobré texty
      </h2>
      <br/>

      <div>
        <h3>Jak?</h3>
        <p>
          Zapojuju kreativitu, psychologii prodeje a emoce. Pokaždé jinak, ale vždy se stejným výsledkem – zvýšením tržeb.
          Mé texty svou rozmanitostí připomínají seriál M*A*S*H.
          Jednou jsou neodolatelně pompézní jako major Winchester, podruhé okouzlí dětskou hravostí Hawkeyho Pierce a jindy si po vzoru Margaret neberou servítky.
          Nikdy jim ovšem nechybí lidskost plukovníka Pottera.
          A stejně jako parta z mobilní nemocnice dokážou zachránit i zdánlivě ztracené případy.
        </p>
      </div>

      <div>
        <h3>Kam?</h3>
        <p>
          Na weby, blogy, prodejní stránky, sítě i do kreativ, e-mailů a reklamních kampaní.
        </p>
      </div>

      <div>
        <h3>Za kolik?</h3>
        <p>
          Každý projekt naceňuju individuálně na základě sazby 1818 Kč/hod.<br/>
          U dlouhodobé spolupráce nad 10 hodin měsíčně nabízím slevu 20 %.<br/>
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
  margin-top: 1rem;
  margin-bottom: 3rem;
}

.section-offer {
  text-align: center;
  width: 60%;
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