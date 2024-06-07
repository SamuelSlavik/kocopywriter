<script setup lang="ts">
import {inject, onMounted, ref} from "vue";
import {useRouter} from "vue-router";
import {useUserStore} from "@/stores/user-store";
import type {NewImage} from "@/lib/models";
import {imagesApi} from "@/lib/apiHelpers";
import {backend_url} from "@/lib/constants";

const loading = ref<boolean>(false)
const user = useUserStore()
const router = useRouter()
const notificationStore: any = inject('notificationStore')

const imageId = router.currentRoute.value.params.id.toString() || ""

const imageUrl = ref<string>("")
const newImage = ref<NewImage>(
    {
      image: null,
      name: ""
    }
)

const loadImage = async () => {
  try {
    loading.value = true
    const response = await imagesApi.getImage(imageId)
    newImage.value.name = response.data.name
    imageUrl.value = response.data.url
  } catch (e: any) {
    notificationStore.addNotification({
      type: 'error',
      message: 'Failed to load image: ' + e.response.data.detail,
    })
  } finally {
    loading.value = false
  }
}

const onFileChange = (event: any) => {
  newImage.value.image = event.target.files[0]
}

const submitImage = async () => {
  const formData = new FormData();
  if (newImage.value.image) {
    formData.append("image", newImage.value.image);
  }
  formData.append("name", newImage.value.name);

try {
  const response = await imagesApi.updateImage(imageId, formData);
  if (response.status === 200) {
    notificationStore.addNotification({ type: "success", message: "Image updated successfully" });
    await router.push('/admin/images');
  } else {
    notificationStore.addNotification({ type: "error", message: `Failed to update image: ${response.statusText}` });
  }
} catch (error: any) {
  notificationStore.addNotification({ type: "error", message: `Failed to update image: ${error.response.data.detail}` });
}
}

onMounted(() => {
  loadImage()
})

</script>

<template>
  <Container>
    <Heading>Edit Image</Heading>
    <p>Add images to use them in the blog later by returned URL.</p>
    <p>The images will be sorted by name, so advicing to start each image with some group name.</p>
    <p>E.g. "blog-name-followed-by-som-image-name", "blog-name-with-another-image-name2"</p>
    <Loader v-if="loading"/>
    <div v-else class="form-block">
      <form @submit.prevent="submitImage">
        <div>
          <label>Image name</label>
          <input
              type="text"
              name="name"
              placeholder="Name"
              v-model="newImage.name"
              required
          />
        </div>
        <img :src="backend_url + imageUrl" alt="Current image" class="image-detail"/>
        <div>
          <label>Upload new image if you want to change it</label>
          <input
              type="file"
              name="image"
              accept="image/*"
              @change="onFileChange($event)"
          />
        </div>
        <button
            class="button"
            type="submit"
        >Update image</button>
      </form>
    </div>
  </Container>
</template>

<style>

</style>