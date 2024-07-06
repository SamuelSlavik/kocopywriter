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
    <Heading>Ukázky prací</Heading>
    <div class="hr"></div>
    <Loader v-if="loading"/>
    <div class="projects-wrapper" v-else>
      <div class="project" v-for="(project, index) in projects" :key="project.id">
        <Heading>{{project.name}}</Heading>
        <p class="project__task">{{project.task}}</p>
        <p class="project__description">{{project.description}}</p>
        <img
            v-for="(image, index) in project.images"
            :key="index"
            :src="image"
            alt="project image"
        />
        <div class="hr" v-if="index + 1 < projects.length"></div>
      </div>
    </div>
  </Container>
</template>

<style>
.projects-wrapper {
  width: 100%;
}
.project {
  text-align: left;
  width: 100%;
  display: flex;
  flex-direction: column;

  heading {
    margin-bottom: 0;
  }
  .project__task {
    color: var(--primary);
    margin-bottom: 1rem;
  }
  .project__description {
    color: var(--secondary);
  }
  img {
    width: 80%;
    height: auto;
    margin: 1rem auto;
  }
}
</style>