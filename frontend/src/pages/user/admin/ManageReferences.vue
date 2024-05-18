<script setup lang="ts">
import {inject, onMounted, ref} from "vue";
import {useRouter} from "vue-router";
import {useUserStore} from "@/stores/user-store";
import type {Reference} from "@/lib/models";
import {referencesApi} from "@/lib/apiHelpers";
import Pencil from "vue-material-design-icons/Pencil.vue";
import Delete from "vue-material-design-icons/Delete.vue";

const loading = ref<boolean>(false)
const user = useUserStore()
const router = useRouter()
const notificationStore: any = inject('notificationStore')

const references = ref<Reference[]>([])

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

const deleteReference = async (id: string) => {
  const confirm = window.confirm("Are you sure you want to delete this reference?")

  if (confirm) {
    try {
      const response = await referencesApi.deleteReference(id)
      if (response.status === 200) {
        notificationStore.addNotification({type: 'success', message: "Reference deleted"})
        await loadReferences()
      }
    } catch (error: any) {
      notificationStore.addNotification({type: 'error', message: "Failed to delete reference: " + error.response.data.detail})
    }
  }
}

onMounted(() => {
  loadReferences()
})

</script>

<template>
  <Container>
    <Heading>Manage References</Heading>
    <p>References displayed in carousel.</p>
    <div class="hr"></div>
    <Loader v-if="loading"/>
    <div class="table" v-else>
      <div class="table__row" v-for="reference in references" :key="reference.id">
        <div class="table--1">
          <p>{{reference.id}}</p>
        </div>
        <div class="table--6">
          <router-link :to="'/admin/references/detail/' + reference.id">{{reference.name}}</router-link>
        </div>
        <div class="table--1">

        </div>
        <div class="table__toolbar">
          <router-link :to="'/admin/references/edit/' + reference.id"><Pencil :size="24" /></router-link>
          <a @click="deleteReference(reference.id)"><Delete :size="24" /></a>
        </div>
      </div>
    </div>
  </Container>
</template>

<style>

</style>