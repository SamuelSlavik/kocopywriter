<script setup lang="ts">
import {useUserStore} from "@/stores/user-store";
import {inject, onMounted, ref} from "vue";
import type {Headline} from "@/lib/models";
import {headlineApi} from "@/lib/apiHelpers";
import {useRouter} from "vue-router";

const router = useRouter()
const loading = ref<boolean>(false)
const notificationStore: any = inject('notificationStore')

const headline = ref<Headline>()
const newHeadline = ref<Headline>(
    {
      text: headline.value?.text || ""
    }
)

const loadHeadline = async () => {
  try {
    loading.value = true
    const response = await headlineApi.getHeadline()
    newHeadline.value = response.data
  } catch (error: any) {
    notificationStore.addNotification({type: "error", message: "Failed to get headline: " + error.message})
  } finally {
    loading.value = false
  }
}

const updateHeadline = async () => {
  try {
    const response = await headlineApi.updateHeadline(newHeadline.value)
    if (response.status === 200) {
      await router.push('/')
      notificationStore.addNotification({type: "success", message: "Headline updated successfully"})
    }
  } catch (error: any) {
    notificationStore.addNotification({type: "error", message: "Failed to update headline: " + error.message})
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  loadHeadline()
})


</script>

<template>
  <Container>
    <Heading>Edit Headline</Heading>
    <Loader v-if="loading"/>
    <div v-else>
      <p>Edit the main headline on the top most front page.</p>
      <div class="form-block">
        <form @submit.prevent="updateHeadline">
          <div>
            <label>Headline text</label>
            <input
                type="text"
                name="text"
                placeholder="Headline text"
                v-model="newHeadline.text"
                required
            />
          </div>
          <button
              class="button"
              type="submit"
          >Submit new headline</button>
        </form>
      </div>
    </div>
  </Container>
</template>

<style>

</style>