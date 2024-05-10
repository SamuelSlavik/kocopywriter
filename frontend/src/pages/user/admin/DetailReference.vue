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

const reference = ref<Reference>({
  id: "",
  name: '',
  url: "",
  description: "",
  image: ""
})

const loadReference = async () => {
  try {
    loading.value = true
    const response = await referencesApi.getReference(referenceId.value)
    reference.value = response.data
  } catch (e: any) {
    notificationStore.addNotification({
      type: 'error',
      message: 'Failed to load reference',
    })
  } finally {
    loading.value = false
  }
}

const deleteReference = async (id: string) => {
  const confirm = window.confirm("Are you sure you want to delete this reference?")

  if (confirm) {
    try {
      const response = await referencesApi.deleteReference(id)
      if (response.status === 200) {
        notificationStore.addNotification({type: 'success', message: "Reference deleted"})
        await router.push("/admin/references")
      }
    } catch (error: any) {
      notificationStore.addNotification({type: 'error', message: "Failed to delete reference: " + error.message})
    }
  }
}

onMounted(() => {
  loadReference()
})

</script>

<template>
  <Container>
    <Loader v-if="loading"/>
    <div v-else v-if="reference.name">
      <Heading>{{reference.name}}</Heading>
      <div class="toolbar">
        <router-link :to="'/admin/references/edit/' + reference.id"><Pencil :size="24" /></router-link>
        <a @click="deleteReference(reference.id)"><Delete :size="24" /></a>
      </div>
      <div class="hr"></div>
      <p><b>Url: </b><a target="_blank" :href="reference.url">{{reference.url}}</a></p>
      <p><b>Description: </b>{{reference.description}}</p>
      <img class="image-detail" :src="backend_url + reference.image" alt="Current image"/>
    </div>
  </Container>
</template>

<style>

</style>