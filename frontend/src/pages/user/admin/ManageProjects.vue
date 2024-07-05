<script setup lang="ts">
import {inject, onMounted, ref} from "vue";
import {useUserStore} from "@/stores/user-store";
import {useRouter} from "vue-router";
// @ts-ignore
import Pencil from "vue-material-design-icons/Pencil.vue";
// @ts-ignore
import Delete from "vue-material-design-icons/Delete.vue";
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

const deleteProject = async (id: string) => {
  const confirm = window.confirm("Are you sure you want to delete this project?")

  if (confirm) {
    try {
      const response = await projectsApi.deleteProject(id)
      if (response.status === 200) {
        notificationStore.addNotification({type: 'success', message: "Project deleted"})
        await loadProjects()
      }
    } catch (error: any) {
      notificationStore.addNotification({type: 'error', message: "Failed to delete project: " + error.response.data.detail})
    }
  }
}

onMounted(() => {
  loadProjects()
})

</script>

<template>
  <Container>
    <Heading>Manage Project Showcases</Heading>
    <p>Project showcases displayed in "Ukázky prací".</p>
    <div class="hr"></div>
    <Loader v-if="loading"/>
    <div class="table" v-else>
      <div class="table__row" v-for="project in projects" :key="project.id">
        <div class="table--1">
          <p>{{project.id}}</p>
        </div>
        <div class="table--6">
          <router-link :to="'/admin/projects/detail/' + project.id">{{project.name}}</router-link>
        </div>
        <div class="table--1">

        </div>
        <div class="table__toolbar">
          <router-link :to="'/admin/projects/edit/' + project.id"><Pencil :size="24" /></router-link>
          <a @click="deleteProject(project.id)"><Delete :size="24" /></a>
        </div>
      </div>
    </div>
  </Container>
</template>

<style>

</style>