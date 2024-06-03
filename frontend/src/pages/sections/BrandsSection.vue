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

const brands = ref<Brand[]>()

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
  loadBrands()
})
</script>

<template>
  <Loader v-if="loading"/>
  <div class="brands" v-else>
    <div>
      <img v-for="brand in brands" :key="brand.id" :src="backend_url + brand.image" :alt="brand.name" />
    </div>
  </div>
</template>

<style>
.brands {
  width: 100%;
  background-color: var(--background);
  height: 3rem;
  position: relative;
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