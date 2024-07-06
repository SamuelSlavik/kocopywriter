<script setup lang="ts">
import {inject, onMounted, ref} from "vue";
import {useUserStore} from "@/stores/user-store";
import {useRouter} from "vue-router";
import type {NewProject, Project} from "@/lib/models";
import {projectsApi} from "@/lib/apiHelpers";

const loading = ref<boolean>(false)
const user = useUserStore()
const router = useRouter()
const notificationStore: any = inject('notificationStore')

const projects = ref<Project[]>([])
const newProject = ref<NewProject>({
  order: 0,
  name: '',
  url: '',
  task: '',
  description: "",
  images: []
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

const submitProject = async () => {
  const formData = new FormData()
  formData.append("order", newProject.value.order.toString())
  formData.append("name", newProject.value.name)
  formData.append("url", newProject.value.url || "")
  formData.append("task", newProject.value.task)
  formData.append("description", newProject.value.description)
  for (let i = 0; i < newProject.value.images.length; i++) {
    formData.append("image", newProject.value.images[i]);
  }

  try {
    const response = await projectsApi.createProject(formData)
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

const addImage = () => {
  newProject.value.images.push("")
}

onMounted(() => {
  loadProjects()
})

</script>

<template>
  <Container>
    <Heading>Create new Project Showcase</Heading>
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
        <div>
          <label>Images</label>
          <div class="file-input-wrapper" v-for="(image, index) in newProject.images">
            <input
                name="image"
                type="file"
                placeholder="Image"
                accept="image/*"
                @change="(event: any) => {newProject.images[index] = event.target.files[0]}"
                required
            />
            <button
                class="button"
                type="button"
                @click="() => newProject.images.splice(index, 1)"
            >Remove Image</button>
          </div>
        </div>
        <button
          class="button"
          type="button"
          @click="addImage"
        >
          Add new image
        </button>
        <br/>
        <button type="submit" class="button">Create new Project</button>
      </form>
    </div>
  </Container>
</template>

<style>

</style>