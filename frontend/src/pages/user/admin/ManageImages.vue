<script setup lang="ts">
import {inject, onMounted, ref} from "vue";
import {useRouter} from "vue-router";
import {useUserStore} from "@/stores/user-store";
import type {Image} from "@/lib/models";
import {imagesApi, pricingApi} from "@/lib/apiHelpers";
// @ts-ignore
import Pencil from "vue-material-design-icons/Pencil.vue";
// @ts-ignore
import Delete from "vue-material-design-icons/Delete.vue";
import {backend_url} from "@/lib/constants";

const loading = ref<boolean>(false)
const user = useUserStore()
const router = useRouter()
const notificationStore: any = inject('notificationStore')

const images = ref<Image[]>([])

const searchQuery = ref<string>("")

const loadImages = async () => {
  loading.value = true
  try {
    const response = await imagesApi.getImages(searchQuery.value || "")
    images.value = response.data
  } catch (error: any) {
    notificationStore.addNotification({
      type: 'error',
      message: 'Failed to load images: ' + error.response.data.detail,
    })
  } finally {
    loading.value = false
  }
}

const deleteImage = async (id: string) => {
  const confirm = window.confirm("Are you sure you want to delete this image?")

  if (confirm) {
    try {
      const response = await imagesApi.deleteImage(id)
      if (response.status === 200) {
        notificationStore.addNotification({type: 'success', message: "Image deleted"})
        await loadImages()
      }
    } catch (error: any) {
      notificationStore.addNotification({type: 'error', message: "Failed to delete image: " + error.response.data.detail})
    }
  }
}

onMounted(() => {
  loadImages()
})

</script>

<template>
  <Container>
    <Heading>Manage images</Heading>
    <p>Images that should be used in posts (no other usage) by copying the url.</p>
    <p>Use the search bar to filter images that contain the query in their names.</p>
    <div class="hr"></div>
    <form @submit.prevent="loadImages">
      <div class="form-row">
        <input type="text" v-model="searchQuery" placeholder="Search images" />
        <button class="button">Search Images</button>
      </div>
    </form>
    <Loader v-if="loading"/>
    <div v-else>
      <div class="table">
        <div class="table__row" v-for="image in images" :key="image.id">
          <div class="table--1">
            <router-link :to="'/admin/images/detail/' + image.id">{{image.id}}</router-link>
          </div>
          <div class="table--3">
            <router-link :to="'/admin/images/detail/' + image.id">{{image.name}}</router-link>
          </div>
          <div class="table--4">
            <p>{{backend_url + image.url}}</p>
          </div>
          <div class="table--1">

          </div>
          <div class="table__toolbar">
            <router-link :to="'/admin/images/edit/' + image.id"><Pencil :size="24" /></router-link>
            <a @click="deleteImage(image.id)"><Delete :size="24" /></a>
          </div>
        </div>
      </div>
    </div>
  </Container>
</template>

<style>

</style>