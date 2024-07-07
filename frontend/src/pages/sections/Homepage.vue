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
        <div class="homepage-wallpaper">
          <img src="../../assets/images/wallpapers/w-1.jpg" alt="Logo" />
        </div>
        <div class="homepage-header">
          <div>
            <Loader v-if="loading"/>
            <div v-else>
              <h1>
                {{headline?.text || "Mluvit moc neumím, přesto vaši cílovou skupinu zaručeně oslovím"}}
              </h1>
              <a @click="() => scrollToTarget('section-contact', 0)" class="button">Dávej, Beru!</a>
            </div>
          </div>
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
  width: 50%;
  margin-left: 50%;
  text-align: right;
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
    @media (max-width: 1024px) {
      font-size: 1.8rem;
      line-height: 2rem;
    }
  }
  .button {
    margin-top: 4rem;
    @media (max-width: 1024px) {
      margin-top: 2rem;
      position: relative;
      right: 50%;
      transform: translateX(50%);
    }
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
    @media (max-width: 1024px) {
      position: relative;
      bottom: 0;
      transform: none;
      left: 0;
      width: 100%;
    }
  }
}
</style>