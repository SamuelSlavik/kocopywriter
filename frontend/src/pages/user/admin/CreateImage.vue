<script setup lang="ts">
import {inject, ref} from "vue";
import {useRouter} from "vue-router";
import {useUserStore} from "@/stores/user-store";
import type {NewImage} from "@/lib/models";
import {imagesApi} from "@/lib/apiHelpers";

const loading = ref<boolean>(false)
const user = useUserStore()
const router = useRouter()
const notificationStore: any = inject('notificationStore')

const image = ref<NewImage>(
  {
    image: "",
    name: ""
  },
)


const onFileChange = (event: any) => {
  image.value.image = event.target.files[0]
}

const submitAllImages = async () => {
  const formData = new FormData();

    formData.append(`image`, image.value.image);
    formData.append(`name`, image.value.name);

  try {
    const response = await imagesApi.createImage(formData);

    if (response.status === 200) {
      notificationStore.addNotification({ type: "success", message: "Images uploaded successfully" });
      await router.push('/admin/images');
    } else {
      notificationStore.addNotification({ type: "error", message: `Failed to upload images: ${response.statusText}` });
    }
  } catch (error: any) {
    notificationStore.addNotification({ type: "error", message: `Failed to upload images: ${error.response.data.detail}` });
  } finally {
    loading.value = false;
  }
}

</script>

<template>
  <Heading>Add images</Heading>
  <p>Add images to use them later in the posts by returned URL.</p>
  <p>The images will be sorted by name, so advicing to start each image with some group name.</p>
  <p>E.g. "blog-name-followed-by-som-image-name", "blog-name-with-another-image-name2"</p>
  <div class="form-block">
    <form @submit.prevent="submitAllImages">
      <div>
        <label>Image name</label>
        <div class="file-input-wrapper">
          <input
              type="text"
              name="name"
              placeholder="Name"
              v-model="image.name"
              required
          />
          <input
              type="file"
              name="image"
              accept="image/*"
              @change="onFileChange($event)"
              required
          />
        </div>
      </div>
      <button
          class="button"
          type="submit"
          disabled
      >Submit new image</button>
    </form>
  </div>
</template>

<style>

</style>