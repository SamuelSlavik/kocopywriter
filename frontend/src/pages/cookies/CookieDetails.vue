<script lang="ts" setup>
import { useCookieConsentStore } from "@/stores/cookie-consent-store";
import { onMounted, ref } from 'vue';

const cookies = useCookieConsentStore();

// Create reactive variables for checkbox states
const technicalChecked = ref(cookies.technical);
const analyticalChecked = ref(cookies.analytical);

const loadCookiesConsent = async () => {
  try {
    const analytical = localStorage.getItem("cookieConsentAnalytical")
    const technical = localStorage.getItem("cookieConsentTechnical")

    console.log('analytical', analytical)
    console.log('technical', technical)

    if (!analytical && !technical) {
      cookies.setSet(false)
    } else {
      cookies.setSet(true)
      cookies.setTechnicalOnly(!!technical)
      cookies.setAnalyticalOnly(!!analytical)
    }
  } catch (error) {
    console.log(error)
  }
}

// Set checkboxes to current state on mount
onMounted(() => {
  loadCookiesConsent()

  technicalChecked.value = cookies.technical;
  analyticalChecked.value = cookies.analytical;
});

// Methods to handle checkbox changes immediately
const handleTechnicalChange = () => {
  cookies.setSet(true);
  cookies.setTechnical(technicalChecked.value);
};

const handleAnalyticalChange = () => {
  cookies.setSet(true);
  cookies.setAnalytical(analyticalChecked.value);
};
</script>

<template>
  <Container :global="true">
    <div class="cookies-details">
      <h2>Co jsou cookies?</h2>
      <br/>
      <p>
        Cookies představují krátké textové soubory,
        které můj web pošle do vašeho prohlížeče.
        Díky tomu mohou tyto stránky správně fungovat a já mám zpětnou vazbu,
        která mi je pomáhá průběžně vylepšovat. Zjistím také, s čím vás nemám otravovat. A nebudu.
      </p>
    </div>
    <br/>
    <div class="cookies-options">
      <h2>Nastavím si co je cajk</h2>
      <br/>
      <div class="cookies-details__row">
        <input
          type="checkbox"
          id="technicalCookies"
          v-model="technicalChecked"
          @change="handleTechnicalChange"
        />
        <label for="technicalCookies"><b>Tachnické</b> - aby můj web fungoval</label>
      </div>
      <div class="cookies-details__row">
        <input
            type="checkbox"
            id="analyticalCookies"
            v-model="analyticalChecked"
            @change="handleAnalyticalChange"
        />
        <label for="analyticalCookies"><b>Analytické</b> - abych viděl, jak je web uživatelsky přívětivý a mohl ho vylepšovat</label>
      </div>
    </div>
    <br/>
    <div class="cookies-details">
      <h2>OOOZ aneb zásady ochrany osobních údajů</h2>
      <br/>
      <a href="/prohlaseni.pdf" target="_blank">
        Prohlášení o ochraně osobních údajů a souborech cookie
      </a>
    </div>
  </Container>
</template>

<style>
.cookies-options {
  text-align: left;
  margin-bottom: 2rem;

  .cookies-details__row {
    display: flex;
    gap: 1rem;
    justify-content: left;

    input {
      width: auto;
      cursor: pointer;
    }

    label {
      cursor: pointer;
    }
  }
}

.cookies-details {
  text-align: left;
  margin-bottom: 2rem;
}
</style>