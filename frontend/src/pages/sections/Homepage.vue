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
const brands = ref<Brand[]>()

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

const loadBrands = async () => {
  try {
    loading.value = true
    const response = await brandsApi.getBrands()
    brands.value = response.data
  } catch (error: any) {
    notificationStore.addNotification({type: "error", message: "Failed to load brands: " + error.response.data.detail})
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  loadHeadline()
  loadBrands()
})

</script>

<template>
  <div id="section-homepage">
    <div class="homepage">
      <Container class="homepage-content">
        <div class="homepage-wallpaper">
          <img src="../../assets/images/wallpapers/w-1.jpg" alt="Logo" />
        </div>
        <div class="homepage-header">
          <div>
            <Loader v-if="loading"/>
            <h1 v-else >
              {{headline?.text || "Mluvit moc neumím, přesto vaši cílovou skupinu zaručeně oslovím"}}
            </h1>
            <a @click="() => scrollToTarget('section-contact', 0)" class="button">Dávej, Beru!</a>
          </div>
        </div>
      </Container>
      <Loader v-if="loading"/>
      <div class="brands" v-else>
        <div>
          <img v-for="brand in brands" :key="brand.id" :src="backend_url + brand.image" :alt="brand.name" />
        </div>
      </div>
    </div>
  </div>
</template>

<style>
.homepage {
  width: 100%;
  height: 100vh;
  position: relative;
}
.homepage-content {
  position: relative;
  height: 100%;
}
.homepage-header {
  display: flex;
  flex-direction: column;
  height: auto;
  top: 50%;
  position: relative;
  transform: translateY(-50%);
  gap: 2rem;
  width: 50%;
  margin-left: 50%;
  text-align: right;

  div {
    margin-top: auto;
    margin-bottom: auto;
    display: flex;
    justify-content: flex-end;
    align-content: flex-end;
    flex-wrap: wrap;
  }
  h1 {
    width: 100%;
    font-size: 2.2rem;
    color: var(--primary);
    font-family: "Times New Roman ", serif;
    font-weight: normal;
    line-height: 3rem;
  }
  .button {
    margin-top: 4rem;
  }
}

.homepage-wallpaper {
  img {
    width: 80%;
    left: -10%;
    height: auto;
    position: absolute;
    z-index: -1;
    top: 50%;
    transform: translateY(-50%);
  }
}

.brands {
  width: 100%;
  background-color: var(--background);
  height: 3rem;
  position: absolute;
  bottom: 0;
  padding: .2rem 3rem;
  @media (max-width: 1024px) {
    display: none;
  }

  > div {
    display: flex;
    justify-content: space-between;
    gap: 1rem;
    width: 100%;
    height: 100%;
    flex-wrap: wrap;
  }

  img {
    height: 100%;
    width: auto;
    filter: grayscale(100%);
  }
}
</style>