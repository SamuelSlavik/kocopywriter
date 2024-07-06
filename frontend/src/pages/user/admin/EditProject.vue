<script setup lang="ts">
import {inject, onMounted, ref} from "vue";
import type {NewProject, Project} from "@/lib/models";
import {projectsApi} from "@/lib/apiHelpers";
import {useUserStore} from "@/stores/user-store";
import {useRouter} from "vue-router";
import {backend_url} from "@/lib/constants";

const loading = ref<boolean>(false)
const user = useUserStore()
const router = useRouter()
const notificationStore: any = inject('notificationStore')
const projectId = ref<string>(router.currentRoute.value.params.id.toString() || "")

const currentImageUrl = ref<string>("")
const projects = ref<Project[]>([])
const newProject = ref<NewProject>({
  order: 0,
  name: '',
  url: '',
  task: '',
  description: "",
  images:[]
})

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

const loadProject = async () => {
  try {
    loading.value = true
    const response = await projectsApi.getProject(projectId.value)
    newProject.value.name = response.data.name
    newProject.value.url = response.data.url
    newProject.value.task = response.data.task
    newProject.value.order = response.data.order
    newProject.value.description = response.data.description
    currentImageUrl.value = response.data.images
  } catch (e: any) {
    notificationStore.addNotification({
      type: 'error',
      message: 'Failed to load project',
    })
  } finally {
    loading.value = false
  }
}

const submitProject = async () => {
  const formData = new FormData()
  formData.append("order", newProject.value.order.toString())
  formData.append("name", newProject.value.name)
  formData.append("url", newProject.value.url || "")
  formData.append("task", newProject.value.task)
  formData.append("description", newProject.value.description)
  if (newProject.value.images) {
    formData.append("image", newProject.value.images[0])
  }

  try {
    const response = await projectsApi.updateProject(projectId.value, formData)
    if (response.status === 200) {
      notificationStore.addNotification({type: 'success', message: "Project created successfully"})
      await router.push("/admin/projects")
    } else {
      notificationStore.addNotification({type: 'error', message: "Failed to create project: " + response.statusText})
    }
  } catch (error: any) {
    notificationStore.addNotification({type: 'error', message: "Failed to create project: " + error.response.data.detail})
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  loadProjects()
  loadProject()
})
</script>

<template>
  <Container>
    <Heading>Edit Project Showcase</Heading>
    <p>As url put whole url, example: https://kocopywriter.cz</p>
    <Loader v-if="loading"/>
    <div class="form-block" v-else>
      <form @submit.prevent="submitProject">
        <div>
          <label>Order</label>
          <select v-model="newProject.order" required >
            <option :value="projects.length+1">{{projects.length+1}}.</option>
            <option v-for="(project, index) in projects" :value="index + 1">
              {{index + 1}}.
            </option>
          </select>
        </div>
        <div>
          <label>Name</label>
          <input
              name="name"
              type="text"
              placeholder="Name"
              v-model="newProject.name"
              required
          />
        </div>
        <div>
          <label>Url</label>
          <input
              name="url"
              type="text"
              placeholder="Url"
              v-model="newProject.url"
          />
        </div>
        <div>
          <label>Task Description</label>
          <input
              name="task"
              type="text"
              placeholder="Task"
              v-model="newProject.task"
              required
          />
        </div>
        <div>
          <label>Description</label>
          <textarea
              name="description"
              v-model="newProject.description"
              placeholder="Description"
              required
          ></textarea>
        </div>
        <img :src="backend_url + currentImageUrl" alt="Current image" class="image-detail"/>
        <div>
          <label>Upload new image if you want to change it</label>
          <input
              name="image"
              type="file"
              placeholder="Image"
              accept="image/*"
              @change="(event: any) => {newProject.images = event.target.files[0]}"
              required
          />
        </div>
        <button type="submit" class="button">Create new Project</button>
      </form>
    </div>
  </Container>
</template>

<style>

</style>