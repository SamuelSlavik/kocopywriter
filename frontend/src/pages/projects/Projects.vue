<script setup lang="ts">
import {inject, onMounted, ref} from "vue";
import {useUserStore} from "@/stores/user-store";
import {useRouter} from "vue-router";
import type {Project} from "@/lib/models";
import {projectsApi} from "@/lib/apiHelpers";
import ImageSlider from "@/pages/projects/ImageSlider.vue";

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

const selectedImages = ref<string[]>([]);
const selectedImageIndex = ref(0);
const isSliderOpen = ref(false);

const openImageSlider = (projectImages: string[], index: number) => {
  selectedImages.value = projectImages;
  selectedImageIndex.value = index;
  isSliderOpen.value = true;
};

const closeImageSlider = () => {
  isSliderOpen.value = false;
};

</script>

<template>
  <Container :global="true">
    <Heading>Ukázky prací</Heading>
    <div class="hr"></div>
    <Loader v-if="loading" />
    <div v-else class="projects-wrapper">
      <div v-for="(project, index) in projects">
        <div class="project" :key="project.id">
          <Heading><img class="project__logo" alt="logo" src="@/assets/images/logos/logo.png"/> {{ project.name }}</Heading>
          <p class="project__task"><img class="project__logo" alt="logo" src="@/assets/images/logos/logo.png"/> {{ project.task }}</p>
          <p class="project__description"><img class="project__logo" alt="logo" src="@/assets/images/logos/logo.png"/> {{ project.description }}</p>
          <div class="project__image-wrapper">
            <img
                v-for="(image, imageIndex) in project.images"
                :key="imageIndex"
                :src="image"
                alt="project image"
                @click="openImageSlider(project.images, imageIndex)"
            />
          </div>
        </div>
        <div class="hr" v-if="index + 1 < projects.length"></div>
      </div>
    </div>
    <ImageSlider
        v-if="isSliderOpen"
        :images="selectedImages"
        :initialIndex="selectedImageIndex"
        @close="closeImageSlider"
    />
  </Container>
</template>

<style>
.projects-wrapper {
  width: 100%;
}
.project {
  text-align: left;
  width: 60%;
  margin: auto;
  display: flex;
  flex-direction: column;
  padding: 2rem 0;

  .project__logo {
    position: absolute;
    left: -100%;
    width: 1em;
    height: auto;
  }
  heading {
    margin-bottom: 0;
  }
  .project__task {
    color: var(--primary);
    margin-bottom: 1rem;
    span {
      color: var(--secondary);
    }
  }
  .project__description {
    color: var(--secondary);
    white-space: pre-line;
  }
  .project__image-wrapper {
    width: 100%;
    display: flex;
    justify-content: left;
    gap: 3%;
    flex-wrap: wrap;
    margin-top: 2rem;

    img {
      height: auto;
      width: 47%;

      &:hover {
        cursor: pointer;
      }
    }
  }
}
</style>