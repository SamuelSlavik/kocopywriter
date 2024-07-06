<script setup lang="ts">
import {inject, onMounted, ref} from "vue";
import {useUserStore} from "@/stores/user-store";
import {useRouter} from "vue-router";
// @ts-ignore
import Delete from "vue-material-design-icons/Delete.vue";
// @ts-ignore
import Pencil from "vue-material-design-icons/Pencil.vue";
import type {Project} from "@/lib/models";
import {projectsApi} from "@/lib/apiHelpers";
import {backend_url} from "@/lib/constants";

const loading = ref<boolean>(false)
const user = useUserStore()
const router = useRouter()
const notificationStore: any = inject('notificationStore')

const project = ref<Project>({
  id: "",
  order: 0,
  name: "",
  url: "",
  task: "",
  description: "",
  images: [],
})

const loadProject = async () => {
  try {
    loading.value = true
    const response = await projectsApi.getProject(router.currentRoute.value.params.id.toString())
    project.value = response.data
  } catch (e: any) {
    notificationStore.addNotification({
      type: 'error',
      message: 'Failed to load project',
    })
  } finally {
    loading.value = false
  }
}

const deleteProject = async (id: string) => {
  const confirm = window.confirm("Are you sure you want to delete this project?")

  if (confirm) {
    try {
      const response = await projectsApi.deleteProject(id)
      if (response.status === 200) {
        notificationStore.addNotification({type: 'success', message: "Project deleted"})
        await router.push("/admin/projects")
      }
    } catch (error: any) {
      notificationStore.addNotification({type: 'error', message: "Failed to delete project: " + error.response.data.detail})
    }
  }
}

onMounted(() => {
  loadProject()
})

</script>

<template>
  <Container>
    <Loader v-if="loading"/>
    <div v-else v-if="project.name">
      <Heading>{{project.name}}</Heading>
      <div class="toolbar">
        <router-link :to="'/admin/projects/edit/' + project.id"><Pencil :size="24" /></router-link>
        <a @click="deleteProject(project.id)"><Delete :size="24" /></a>
      </div>
      <div class="hr"></div>
      <p><b>Order: </b>{{project.order}}</p>
      <p><b>Url: </b>{{project.url}}</p>
      <p><b>Task: </b>{{project.task}}</p>
      <p><b>Descriptions: </b></p>
      <p style="white-space: pre-line">{{project.description}}</p>
      <img class="image-detail" :src="backend_url + project.images" alt="Current image"/>
    </div>
  </Container>
</template>

<style>

</style>