<script setup lang="ts">

</script>

<template>
  <Container id="section-offer">
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
          A tím pádem i konkurenční výhodu – od namingu až po pitch drafty pro investory.
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
<!--        <p>-->
<!--          Každý projekt naceňuju individuálně na základě sazby 1818 Kč/hod.<br/>-->
<!--          U dlouhodobé spolupráce nad 10 hodin měsíčně nabízím slevu 20 %.<br/>-->
<!--          <router-link to="/pricing">Orientační ceník</router-link>-->
<!--        </p>-->
      </div>
<!--      <div>-->
<!--        <h3>Chcete je?</h3>-->
<!--        <p>Napište mi na <a href="mailto:ko@kocopywriter.cz">ko@kocopywriter.cz</a></p>-->
<!--      </div>-->
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