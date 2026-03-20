<script setup lang="ts">

import Container from "@/components/Container.vue";
import {scrollToTarget} from "@/lib/utils.js";
import {useUserStore} from "@/stores/user-store";
import {brandsApi, headlineApi} from "@/lib/apiHelpers";
import {inject, onMounted, ref} from "vue";
import type {Brand, Headline} from "@/lib/models";
import {backend_url} from "@/lib/constants";

const user = useUserStore()
const loading = ref<boolean>(false)
const notificationStore: any = inject('notificationStore')

const headline = ref<Headline>()

const loadHeadline = async () => {
  try {
    loading.value = true
    const response = await headlineApi.getHeadline()
    headline.value = response.data
  } catch (error: any) {
    notificationStore.addNotification({type: "error", message: "Failed to get headline: " + error.response.data.detail})
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  loadHeadline()
})

</script>

<template>
  <div id="section-homepage">
    <div class="homepage">
      <Container class="homepage-content">
        <div class="homepage-header">
          <div>
            <h1>Vtisknu vám účelnou jinakost</h1>
            <h2>Strategické texty a nápady pro firmy, <br/>které chtějí být ko-<span class="accent">kontrastní</span></h2>
            <p>
              Ne proto, aby byly za každou cenu kreativní a originální – ale
              aby jejich komunikace nebyla zaměnitelná a přitom dávala byznysově smysl.
            </p>
            <a @click="() => scrollToTarget('section-contact', 0)" class="button">Dávej, Beru!</a>
          </div>
        </div>
        <div class="homepage-wallpaper">
          <img src="../../assets/images/wallpapers/w-dark-1.jpg" alt="Huli" />
        </div>
      </Container>
    </div>
  </div>
</template>

<style>
.homepage {
  width: 100%;
  height: 100vh;
  position: relative;
  @media (max-width: 1024px) {
    height: auto;
  }
}
.homepage-content {
  position: relative;
  height: 100%;
  @media (max-width: 1024px) {
    padding-top: 12rem;
    padding-bottom: 6rem;
  }
}
.homepage-header {
  display: flex;
  flex-direction: column;
  height: auto;
  top: 50%;
  position: relative;
  transform: translateY(-50%);
  gap: 2rem;
  width: 60%;
  margin-left: 0;
  text-align: left;

  @media (max-width: 1024px) {
    width: 100%;
    transform: none;
    margin-left: 0;
    top: 0;
    text-align: center;
  }

  div {
    margin-top: auto;
    margin-bottom: auto;
    display: flex;
    justify-content: flex-start;
    align-content: flex-start;
    flex-wrap: wrap;
  }

  h1 {
    width: 100%;
    font-size: 2.5rem;
    color: var(--primary);
    font-weight: bold;
    line-height: 3rem;
    @media (max-width: 1024px) {
      font-size: 1.8rem;
      line-height: 2rem;
    }
  }

  h2 {
    width: 100%;
    color: var(--primary);
    margin-top: 4rem;
    font-size: 1.5rem;
    font-weight: bold;
  }

  p {
    margin-top: 4rem;
  }

  .button {
    margin-top: 4rem;
    margin-left: 0;
    margin-right: auto;

    @media (max-width: 1024px) {
      margin-left: auto;
    }
  }
}

.homepage-wallpaper {
  img {
    width: 60%;
    right: -15%;
    height: auto;
    position: absolute;
    z-index: -1;
    top: 50%;
    transform: translateY(-50%);
    @media (max-width: 1024px) {
      position: relative;
      bottom: 0;
      transform: none;
      left: 0;
      width: 100%;
      margin-top: 4rem;
    }
  }
}
</style>