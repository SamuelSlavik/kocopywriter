<script setup lang="ts">
import {computed, inject, onMounted, ref} from "vue";
import {useRouter} from "vue-router";
import {useUserStore} from "@/stores/user-store";
import type {NewReference, Reference} from "@/lib/models";
import {referencesApi} from "@/lib/apiHelpers";

const loading = ref<boolean>(false)
const user = useUserStore()
const router = useRouter()
const notificationStore: any = inject('notificationStore')

const references = ref<Reference[]>([])

const newReference = ref<NewReference>({
  order: 0,
  name: '',
  position: "",
  url: "",
  description: "",
  image: ""
})

const submitReference = async () => {
  const formData = new FormData()

  formData.append("order", newReference.value.order.toString())
  formData.append("name", newReference.value.name)
  formData.append("position", newReference.value.position)
  formData.append("url", newReference.value.url)
  formData.append("description", newReference.value.description)
  formData.append("image", newReference.value.image)

  try {
    const response = await referencesApi.createReference(formData);

    if (response.status === 200) {
      notificationStore.addNotification({ type: "success", message: "Reference created successfully" });
      await router.push("/admin/references")
    } else {
      notificationStore.addNotification({ type: "error", message: `Failed to create reference: ${response.statusText}` });
    }
  } catch (error: any) {
    notificationStore.addNotification({ type: "error", message: `Failed to create reference: ${error.response.data.detail}` });
  } finally {
    loading.value = false
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
      message: 'Failed to load references',
    })
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  loadReferences()
})

</script>

<template>
  <Container>
    <Heading>Create new Reference</Heading>
    <p>As url put whole url, example: https://kocopywriter.cz</p>
    <p>For best quality upload square images.</p>
    <Loader v-if="loading"/>
    <div class="form-block" v-else>
      <form @submit.prevent="submitReference">
        <div>
          <label>Order</label>
          <select v-model="newReference.order" required >
            <option :value="references.length+1">{{references.length+1}}.</option>
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
          <textarea
              name="description"
              placeholder="Description"
              v-model="newReference.description"
              required
          ></textarea>
        </div>
        <div>
          <label>Profile image</label>
          <!--
          <input
              name="image"
              type="text"
              placeholder="Image"
              v-model="newReference.image"
              required
          />
          -->
          <input
              name="image"
              type="file"
              placeholder="Image"
              accept="image/*"
              @change="(event: any) => {newReference.image = event.target.files[0]}"
              required
          />
        </div>
        <button type="submit" class="button">Submit new reference</button>
      </form>
    </div>
  </Container>
</template>

<style>

</style>