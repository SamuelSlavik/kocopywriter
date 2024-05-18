<script setup lang="ts">
import {inject, onMounted, ref} from "vue";
import {useRouter} from "vue-router";
import {useUserStore} from "@/stores/user-store";
import type {NewReference, Reference} from "@/lib/models";
import {referencesApi} from "@/lib/apiHelpers";
import {backend_url} from "@/lib/constants";

const loading = ref<boolean>(false)
const user = useUserStore()
const router = useRouter()
const notificationStore: any = inject('notificationStore')

const referenceId = ref<string>(router.currentRoute.value.params.id.toString()) || ""

const currentImageUrl = ref<string>("")
const newReference = ref<NewReference>({
  order: 0,
  name: '',
  position: "",
  url: "",
  description: "",
  image: ""
})

const references = ref<Reference[]>([])


const loadReference = async () => {
  try {
    loading.value = true
    const response = await referencesApi.getReference(referenceId.value)
    newReference.value.order = response.data.order
    newReference.value.name = response.data.name
    newReference.value.position = response.data.position
    newReference.value.url = response.data.url
    newReference.value.description = response.data.description
    currentImageUrl.value = response.data.image
  } catch (e: any) {
    notificationStore.addNotification({
      type: 'error',
      message: 'Failed to load reference',
    })
  } finally {
    loading.value = false
  }
}

const submitReference = async () => {
  const formData = new FormData();
  if (newReference.value.image) {
    formData.append("image", newReference.value.image);
  }
  formData.append("order", newReference.value.order.toString());
  formData.append("name", newReference.value.name);
  formData.append("position", newReference.value.position);
  formData.append("url", newReference.value.url);
  formData.append("description", newReference.value.description);

  try {
    const response = await referencesApi.updateReference(referenceId.value, formData);
    if (response.status === 200) {
      notificationStore.addNotification({ type: "success", message: "Reference updated successfully" });
      await router.push('/admin/references');
    } else {
      notificationStore.addNotification({ type: "error", message: `Failed to update reference: ${response.statusText}` });
    }
  } catch (error: any) {
    notificationStore.addNotification({ type: "error", message: `Failed to update reference: ${error.response.data.detail}` });
  }
}

const loadReferences = async () => {
  loading.value = true
  try {
    const response = await referencesApi.getReferences()
    references.value = response.data
  } catch (error: any) {
    notificationStore.addNotification({
      type: 'error',
      message: 'Failed to load references: ' + error.response.data.detail,
    })
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  loadReference()
  loadReferences()
})

</script>

<template>
  <Container>
    <Heading>Edit Reference</Heading>
    <p>As url put whole url, example: https://kocopywriter.cz</p>
    <p>For best quality upload square images.</p>
    <Loader v-if="loading"/>
    <div class="form-block" v-else>
      <form @submit.prevent="submitReference">
        <div>
          <label>Order</label>
          <select v-model="newReference.order" required >
            <option v-for="(reference, index) in references" :value="index + 1">
              {{index + 1}}.
            </option>
          </select>
        </div>
        <div>
          <label>Firstname + Surname</label>
          <input
              name="name"
              type="text"
              placeholder="Name"
              v-model="newReference.name"
              required
          />
        </div>
        <div>
          <label>Position</label>
          <input
              name="position"
              type="text"
              placeholder="Position"
              v-model="newReference.position"
              required
          />
        </div>
        <div>
          <label>Url of their website</label>
          <input
              name="url"
              type="text"
              placeholder="URL"
              v-model="newReference.url"
              required
          />
        </div>
        <div>
          <label>Description</label>
          <input
              name="description"
              type="text"
              placeholder="Description"
              v-model="newReference.description"
              required
          />
        </div>
        <img :src="backend_url + currentImageUrl" alt="Current image" class="image-detail"/>
        <div>
          <label>Upload new image if you want to change it</label>
          <input
              name="image"
              type="file"
              placeholder="Image"
              accept="image/*"
              @change="(event: any) => {newReference.image = event.target.files[0]}"
          />
        </div>
        <button type="submit" class="button">Update reference</button>
      </form>
    </div>
  </Container>
</template>

<style>

</style>