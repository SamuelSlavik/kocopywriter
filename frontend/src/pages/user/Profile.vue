<script setup lang="ts">
import {useUserStore} from "@/stores/user-store";
import {useRouter} from "vue-router";
import {inject, onMounted, ref} from "vue";
import {userApi} from "@/lib/apiHelpers";
import Dashboard from "@/pages/user/Dashboard.vue";

const router = useRouter()
const notificationStore: any = inject('notificationStore')
const user = useUserStore()
const loading = ref<boolean>(false)

const newEmail = ref<string>("")
const newPassword = ref<string>("")
const newPasswordRepeated = ref<string>("")

const logout = () => {
  try {
    user.logOut()
    localStorage.setItem("token", "")
    router.push('/')
    notificationStore.addNotification({type: "success", message: "Logged out successfully"})
  } catch (error) {
    notificationStore.addNotification({type: "error", message: "Could not log out"})
  }
}
</script>

<template>
  <Loader v-if="loading"/>
  <div class="section-logout" v-else>
    <p>Docs: <a target="_blank" href="">documentation</a></p>
    <br/>
    <p>Greetings from Samuel :)</p>
  </div>
  </template>

<style>
.section-logout {
  * {
    margin: auto;
  }
}
</style>