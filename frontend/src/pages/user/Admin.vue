<script setup lang="ts">

import {inject, onMounted, ref} from "vue";
import {userApi} from "@/lib/apiHelpers";
import {useRouter} from "vue-router";
import Dashboard from "@/pages/user/Dashboard.vue";

const loading = ref<boolean>(false)
const router = useRouter()
const notificationStore: any = inject('notificationStore')

onMounted(async () => {
  try {
    loading.value = true
    const response: any = await userApi.retrieveCurrentUser()
    if (response.status != 200) {
      await router.push('/login')
    }
  } catch (error: any) {
    notificationStore.addNotification({type: "error", message: "Failed to get user: " + error.message})
  } finally {
    loading.value = false
  }
})

</script>

<template>
  <div class="profile-wrapper">
    <Dashboard/>
    <div class="profile">
      <Loader v-if="loading"/>
      <div class="profile-content">
        <router-view></router-view>
      </div>
    </div>
  </div>
</template>

<style>
.profile-wrapper {
  display: flex;
  min-height: 100vh;
  padding-top: 7rem;
}
.profile {
  width: calc((100% - (1280px - 64px)) / 2 + 930px - 32px);
}
.profile-content {
  width: 930px;
  margin-right: auto;
  margin-left: 0;
  padding: 2rem 1rem 2rem 2rem;
}
</style>