<script setup lang="ts">
// @ts-ignore
import Cookie from 'vue-material-design-icons/Cookie.vue';

</script>

<template>
  <div class="footer-container">
    <footer class="footer">
      <div>
        <a href="https://www.linkedin.com/in/vojtechhulinsky/" target="blank"><LinkedIn/></a>
        <p>
          Mgr. Vojtěch Hulinský, Nebeského 1583/29, 470 01 Česká Lípa, IČ: 06849857.
          Jsem zapsaný v živnostenském rejstříku u Městského úřadu Česká Lípa.
        </p>
      </div>
      <br/>
      <div>
        <router-link to="/cookies/details">
          <Cookie />
        </router-link>
        <p>
          Prohlášení o ochraně osobních údajů a souborech cookie
        </p>
      </div>
      <br/>
      <div class="footer__reference">
        <p>
          A vo-vo-vod koho to je?
          <a target="_blank" href="https://www.linkedin.com/in/samuel-sl%C3%A1vik-93404316a/">Samuel Slávik</a>
        </p>
      </div>
    </footer>
  </div>
</template>

<style>
.footer-container {
  border-top: 1px solid var(--tertiary);
  width: 100%;

  footer {
    padding: 2rem;
    width: 100%;
    max-width: var(--breakpoint);
    margin: 0 auto;

    > div {
      width: 100%;
      display: flex;
      align-items: center;
      gap: 2rem;

      * {
        margin-top: auto;
        margin-bottom: auto;
      }
    }

    .footer__reference {
      display: block;
      width: 100%;
      text-align: center;
    }
  }
}
</style>