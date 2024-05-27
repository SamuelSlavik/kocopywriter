<script setup lang="ts">
import {inject, onMounted, ref} from "vue";
import {useRouter} from "vue-router";
import {useUserStore} from "@/stores/user-store";
import type {NewBrand} from "@/lib/models";
import {brandsApi} from "@/lib/apiHelpers";
import {backend_url} from "@/lib/constants";

const loading = ref<boolean>(false)
const user = useUserStore()
const router = useRouter()
const notificationStore: any = inject('notificationStore')

const brandId = router.currentRoute.value.params.id.toString() || ""

const currentImageUrl = ref<string>("")
const newBrand = ref<NewBrand>(
    {
      image: null,
      name: ""
    }
)

const loadBrand = async () => {
  try {
    loading.value = true
    const response = await brandsApi.getBrand(brandId)
    newBrand.value.name = response.data.name
    currentImageUrl.value = response.data.image
  } catch (e: any) {
    notificationStore.addNotification({
      type: 'error',
      message: 'Failed to load brand: ' + e.response.data.detail,
    })
  } finally {
    loading.value = false
  }
}

const onFileChange = (event: any) => {
  newBrand.value.image = event.target.files[0]
}

const submitNewBrand = async () => {
  const formData = new FormData();
  if (newBrand.value.image) {
    formData.append("image", newBrand.value.image);
  }
  formData.append("name", newBrand.value.name);

  try {
    const response = await brandsApi.updateBrand(brandId, formData);
    if (response.status === 200) {
      notificationStore.addNotification({ type: "success", message: "Brand updated successfully" });
      await router.push('/admin/brands');
    } else {
      notificationStore.addNotification({ type: "error", message: `Failed to update brand: ${response.statusText}` });
    }
  } catch (error: any) {
    notificationStore.addNotification({ type: "error", message: `Failed to update brand: ${error.response.data.detail}` });
  }
}

onMounted(() => {
  loadBrand()
})

</script>

<template>
  <Container>
    <Heading>Edit Brand</Heading>
    <p>As brand logo you can choose both colorized or grayscale image.</p>
    <p>Best are .png or .jpeg/.jpg images. Svg format will be rendered as normal image.</p>
    <Loader v-if="loading"/>
    <div v-else class="form-block">
      <form @submit.prevent="submitNewBrand">
        <div>
          <label>Brand name</label>
          <input
              type="text"
              name="name"
              placeholder="brand name"
              v-model="newBrand.name"
              required
          />
        </div>
        <img :src="backend_url + currentImageUrl" alt="Current image" class="image-detail"/>
        <div>
          <label>Upload new image if you want to change it</label>
          <input
            type="text"
            name="image"
            placeholder="Brand image"
            v-model="newBrand.image"
          />
          <!--
          <input
              type="file"
              name="image"
              accept="image/*"
              @change="onFileChange($event)"
          />
          -->
        </div>
        <button
            class="button"
            type="submit"
        >Submit new brand</button>
      </form>
    </div>
  </Container>
</template>

<style>

</style>