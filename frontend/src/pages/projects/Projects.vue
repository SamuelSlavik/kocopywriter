<script setup lang="ts">
import {inject, onMounted, ref} from "vue";
import {useUserStore} from "@/stores/user-store";
import {useRouter} from "vue-router";
import type {Project} from "@/lib/models";
import {projectsApi} from "@/lib/apiHelpers";

const loading = ref<boolean>(false)
const user = useUserStore()
const router = useRouter()
const notificationStore: any = inject('notificationStore')

const projects = ref<Project[]>([])

const loadProjects= async () => {
  loading.value = true
  try {
    const response = await projectsApi.getProjects()
    projects.value = response.data
  } catch (error: any) {
    notificationStore.addNotification({
      type: 'error',
      message: 'Failed to load projects: ' + error.response.data.detail,
    })
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  loadProjects()
})

</script>

<template>
  <Container :global="true">
    <Header>Ukázky prací</Header>
    <div class="hr"></div>
    <Loader v-if="loading"/>
    <div class="projects-wrapper" v-else>
      <div class="project" v-for="(project, index) in projects" :key="project.id">

      </div>
    </div>
  </Container>
</template>

<style>

</style>