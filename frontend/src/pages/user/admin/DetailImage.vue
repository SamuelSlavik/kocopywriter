<script setup lang="ts">
import {inject, onMounted, ref} from "vue";
import {useRouter} from "vue-router";
import {useUserStore} from "@/stores/user-store";
import {imagesApi} from "@/lib/apiHelpers";
import type {Image} from "@/lib/models";
import {backend_url} from "@/lib/constants";
// @ts-ignore
import Pencil from "vue-material-design-icons/Pencil.vue";
// @ts-ignore
import Delete from "vue-material-design-icons/Delete.vue";

const loading = ref<boolean>(false)
const user = useUserStore()
const router = useRouter()
const notificationStore: any = inject('notificationStore')

const imageId = router.currentRoute.value.params.id.toString() || ""

const image = ref<Image>({
  id: "",
  url: "",
  name: ""
})

onMounted(() => {
  loadImage()
})

const loadImage = async () => {
  try {
    loading.value = true
    const response = await imagesApi.getImage(imageId)
    image.value.id = imageId
    image.value.url = response.data.url
    image.value.name = response.data.name
  } catch (e) {
    notificationStore.addNotification({
      type: 'error',
      message: 'Failed to load image',
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
        await router.push("/admin/images")
      }
    } catch (error: any) {
      notificationStore.addNotification({type: 'error', message: "Failed to delete image: " + error.message})
    }
  }
}

onMounted(() => {
  loadImage()
})

</script>

<template>
  <Container>
    <Loader v-if="loading"/>
    <div v-else v-if="image.name">
      <Heading>{{image.name}}</Heading>
      <div class="toolbar">
        <router-link :to="'/admin/images/edit/' + image.id"><Pencil :size="24" /></router-link>
        <a @click="deleteImage(image.id)"><Delete :size="24" /></a>
      </div>
      <div class="hr"></div>
      <p><b>Url: </b>{{backend_url + image.url}}</p>
      <img class="image-detail" :src="backend_url + image.url" alt="Current image"/>
    </div>
  </Container>
</template>

<style>
.toolbar {
  display: flex;
  justify-content: left;
  gap: 1rem;
  width: 100%;

  a:hover {
    fill: var(--orange);
    cursor: pointer;
  }

  svg:hover {
    fill: var(--orange);
    cursor: pointer;
  }
}
.image-detail {
  width: 100%;
  height: auto;
  margin: 2rem 0;
}
</style>