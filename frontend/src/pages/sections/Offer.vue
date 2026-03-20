<script setup lang="ts">

</script>

<template>
  <div class="offer-background" id="section-offer">
    <Container>
      <div class="section-offer">
        <h2>
          Tři cesty k vaší účelné jinakosti
        </h2>
        <br/>

        <div>
          <h3><span class="accent">1.</span> Idea making a business storytelling</h3>
          <p>
            Vymýšlení příběhů, komunikačních konceptů a insighty podložených nápadů, které vašemu produktu,
            službě nebo celé značce dají neotřelý úhel pohledu.
            A tím pádem i konkurenční výhodu – od namingu až po pitch deck pro investory.
            Žádná samoúčelnost, pouze „samo, že účelnost“.
          </p>
        </div>

        <div>
          <h3><span class="accent">2.</span> Copywriting</h3>
          <p>
            Textace webů, psaní blogových a PR článků, tvorba sloganů, příprava newsletterů a obsahu na LinkedIn či pro online kampaně.
            Prostě vše, co potřebujete sdělit slovem – srozumitelně a s lehkostí.
          </p>
        </div>

        <div>
          <h3><span class="accent">3.</span> Automatizace tvorby obsahu</h3>
          <p>
            Příprava AI aplikace pro generování textů ve vašem autorském stylu. NEJDE o běžný odkaz do ChatGPT,
            ale o komplexní nástroj s pokročilým nastavením v pozadí,
            který hlídá kvalitu i odbornou správnost na výrazně vyšší kvalitě než u běžných AI nástrojů.
          </p>
        </div>
      </div>
    </Container>
    <div class="offer-wallpaper">
      <img src="../../assets/images/wallpapers/w-dark-2.jpg" alt="Logo" />
    </div>
  </div>
</template>

<style>

.offer-background {
  margin-top: 1rem;
  margin-bottom: 3rem;

  position: relative;
  width: 100%;
  height: 100%;
}

.offer-wallpaper {
  img {
    width: 800px;
    right: -400px;
    height: auto;
    position: absolute;
    z-index: -1;
    top: 50%;
    transform: translateY(-50%);
    @media (max-width: 1024px) {
      display: none;
    }
  }
}

.section-offer {
  text-align: left;
  width: 70%;
  margin-left: 5%;
  margin-top: 6rem;
  @media (max-width: 1024px) {
    margin-top: 0;
  }

  > div {
    margin-bottom: 1.5rem;
  }
}
</style>