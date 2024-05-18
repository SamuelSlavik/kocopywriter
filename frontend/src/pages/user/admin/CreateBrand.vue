<script setup lang="ts">
import {inject, ref} from "vue";
import {useRouter} from "vue-router";
import {useUserStore} from "@/stores/user-store";
import type {Brand, NewBrand} from "@/lib/models";
import {brandsApi} from "@/lib/apiHelpers";

const loading = ref<boolean>(false)
const user = useUserStore()
const router = useRouter()
const notificationStore: any = inject('notificationStore')

const newBrand = ref<NewBrand>({
  name: '',
  image: ''
})

const submitBrand = async () => {
 const formData = new FormData()

  formData.append("name", newBrand.value.name)
  formData.append("image", newBrand.value.image)

  try {
   const response = await brandsApi.createBrand(formData);

   if (response.status === 200) {
     notificationStore.addNotification({ type: "success", message: "Brand created successfully" });
     await router.push("/admin/brands")
   } else {
      notificationStore.addNotification({ type: "error", message: `Failed to create brand: ${response.statusText}` });
   }
  } catch (error: any) {
    notificationStore.addNotification({ type: "error", message: `Failed to create brand: ${error.response.data.detail}` });
  } finally {
    loading.value = false
  }
}

</script>

<template>
  <Container>
    <Heading>Add new Brand logo</Heading>
    <p>As brand logo you can choose both colorized or grayscale image.</p>
    <p>Best are .png or .jpeg/.jpg images. Svg format will be rendered as normal image.</p>
    <Loader v-if="loading"/>
    <div class="form-block" v-else>
      <form @submit.prevent="submitBrand">
        <div>
          <label>Brand name</label>
          <input
              name="name"
              type="text"
              placeholder="Brand name"
              v-model="newBrand.name"
              required
          />
        </div>
        <div>
          <label>Brand logo</label>
          <input
              name="image"
              type="file"
              placeholder="Brand image"
              accept="image/*"
              @change="(event: any) => {newBrand.image = event.target.files[0]}"
              required
          />
        </div>
        <button type="submit" class="button">Submit new brand logo</button>
      </form>
    </div>
  </Container>
</template>

<style>

</style>