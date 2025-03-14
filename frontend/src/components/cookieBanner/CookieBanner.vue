<script setup lang="ts">
import {useCookieConsentStore} from "@/stores/cookie-consent-store";

const cookies = useCookieConsentStore()

</script>

<template>
  <div class="cookie-banner">
    <div class="cookie-banner__content">
      <div class="cookie-banner__text">
        <p>Pracuju s cookies, abych věděl, jak web funguje. Je to v cajku?
          <router-link to="/cookies/details">Nastavím si co je cajk.</router-link>
        </p>
      </div>
      <div class="cookie-banner__buttons button-group">
        <a @click="() => cookies.setCookieConsent(true)" class="button">Cajk</a>
        <a @click="() => cookies.setCookieConsent(false)" class="button">Necajk</a>
      </div>
    </div>
  </div>
</template>

<style>
.cookie-banner {
  position: fixed;
  bottom: 0;
  right: 0;
  left: 0;
  width: 100%;
  background-color: var(--background);
  box-shadow: 1px 0px 0px 2px rgba(0,0,0,0.11);
  padding: 2rem 1rem;

  .cookie-banner__content {
    max-width: var(--breakpoint);
    margin: 0 auto;
    display: flex;
    gap: 3rem;
    justify-content: space-between;

    @media (max-width: 1024px) {
      display: block;
    }

    .cookie-banner__text {
      width: auto;
      display: flex;

      @media (max-width: 1024px) {
        width: 100%;
        margin-bottom: 1rem;
      }

      * {
        margin-top: auto;
        margin-bottom: auto;
      }
    }

    .cookie-banner__buttons {
      line-height: normal;
      margin-top: auto;
      margin-bottom: auto;
    }
  }
}
</style>