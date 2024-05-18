<script setup lang="ts">
import {inject, onMounted, ref} from "vue";
import {useRouter} from "vue-router";
import {useUserStore} from "@/stores/user-store";
import {brandsApi} from "@/lib/apiHelpers";
import type {Brand, NewBrand} from "@/lib/models";
import Container from "@/components/Container.vue";
import {backend_url} from "@/lib/constants";
// @ts-ignore
import Pencil from "vue-material-design-icons/Pencil.vue";
// @ts-ignore
import Delete from "vue-material-design-icons/Delete.vue";

const loading = ref<boolean>(false)
const user = useUserStore()
const router = useRouter()
const notificationStore: any = inject('notificationStore')

const brandId = router.currentRoute.value.params.id.toString() || ""

const brand = ref<Brand>(
    {
      id: "",
      image: null,
      name: ""
    }
)

const loadBrand = async () => {
  try {
    loading.value = true
    const response = await brandsApi.getBrand(brandId)
    brand.value = response.data
  } catch (e: any) {
    notificationStore.addNotification({
      type: 'error',
      message: 'Failed to load brand',
    })
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
        await router.push("/admin/brands")
      }
    } catch (error: any) {
      notificationStore.addNotification({type: 'error', message: "Failed to delete brand: " + error.response.data.detail})
    }
  }
}

onMounted(() => {
  loadBrand()
})

</script>

<template>
  <Container>
    <Loader v-if="loading"/>
    <div v-else v-if="brand.name">
      <Heading>{{brand.name}}</Heading>
      <div class="toolbar">
        <router-link :to="'/admin/brands/edit/' + brand.id"><Pencil :size="24" /></router-link>
        <a @click="deleteBrand(brand.id)"><Delete :size="24" /></a>
      </div>
      <div class="hr"></div>

      <img :src="backend_url + brand.image" alt="Current image" class="image-detail"/>
    </div>
  </Container>
</template>

<style>

</style>