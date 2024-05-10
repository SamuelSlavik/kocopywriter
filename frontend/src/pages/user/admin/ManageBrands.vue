<script setup lang="ts">
import {inject, onMounted, ref} from "vue";
import {useRouter} from "vue-router";
import {useUserStore} from "@/stores/user-store";
import { Brand } from "@/lib/models";
import {brandsApi} from "@/lib/apiHelpers";
import Pencil from "vue-material-design-icons/Pencil.vue";
import Delete from "vue-material-design-icons/Delete.vue";

const loading = ref<boolean>(false)
const user = useUserStore()
const router = useRouter()
const notificationStore: any = inject('notificationStore')

const brands = ref<Brand[]>([])

const loadBrands = async () => {
  loading.value = true
  try {
    const response = await brandsApi.getBrands()
    brands.value = response.data
  } catch (error: any) {
    notificationStore.addNotification({type: 'error', message: 'Failed to load brands'})
  } finally {
    loading.value = false
  }
}

const deleteBrand = async (id: string) => {
  const confirm = window.confirm("Are you sure you want to delete this brand?")

  if (confirm) {
    try {
      const response = await brandsApi.deleteBrand(id)
      if (response.status === 200) {
        notificationStore.addNotification({type: 'success', message: "Brand deleted"})
        await loadBrands()
      }
    } catch (error: any) {
      notificationStore.addNotification({type: 'error', message: "Failed to delete brand: " + error.message})
    }
  }
}

onMounted(() => {
  loadBrands()
})

</script>

<template>
  <Container>
    <Heading>Brands</Heading>
    <p>Brands displayed on the landing page with grayscale filter.</p>
    <div class="hr"></div>
    <Loader v-if="loading"/>
    <div class="table" v-else>
      <div class="table__row" v-for="brand in brands" :key="brand.id">
        <div class="table--1">
          <p >{{brand.id}}</p>
        </div>
        <div class="table--6">
          <router-link :to="'/admin/brands/detail/' + brand.id">{{brand.name}}</router-link>
        </div>
        <div class="table--1">

        </div>
        <div class="table__toolbar">
          <router-link :to="'/admin/brands/edit/' + brand.id"><Pencil :size="24" /></router-link>
          <a @click="deleteBrand(brand.id)"><Delete :size="24" /></a>
        </div>
      </div>
    </div>
  </Container>
</template>

<style>

</style>