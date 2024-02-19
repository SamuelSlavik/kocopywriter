<script setup lang="ts">
import {ref} from "vue";
import {useRouter} from "vue-router";
import { inject } from 'vue'
import axios from "axios";
import {Endpoints} from "@/lib/endpoints";
import type {User} from "@/lib/models";
import {useUserStore} from "@/stores/user-store";


const router = useRouter()
const notificationStore: any = inject('notificationStore')
const loading = ref<boolean>(false)
const user = useUserStore()

const email = ref<string>("")
const password = ref<string>("")

const login = async () => {
  try {
    const response = await axios.post(
      Endpoints.login,
      {email: email.value, password: password.value}
    )
    localStorage.setItem("token", response.data.access_token)

    if (response.status === 200) {
      try {
        const response = await axios.get<User>(
          Endpoints.retrieveCurrentUser,
          {headers: {Authorization: `Bearer ${localStorage.getItem("token") || ""}`}}
        )
        console.log(response.data)
        user.setUserData(response.data)
        if (response.status === 200) {
          await router.push('/');
        }
      } catch (error: any) {
        notificationStore.addNotification({type: "error", message: "Failed to get user: " + error.message})
      }
    }

  } catch (error: any) {
    notificationStore.addNotification({type: "error", message: "Failed to log in: " + error.message})
  } finally {
    loading.value = false
  }
}

</script>

<template>
  <Container class="section-login">
    <form @submit.prevent="login" class="login-form">
      <input
          type="email"
          name="email"
          placeholder="Email"
          v-model="email"
          required
      />
      <input
          type="password"
          name="password"
          placeholder="Password"
          v-model="password"
          required
      />
      <button
          class="button"
          type="submit"
      >Log in</button>
    </form>
  </Container>
</template>

<style>
.section-login {
  min-height: 100vh;
  display: flex;
  justify-content: center;
  flex-direction: column;
}
.login-form {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  width: 100%;
  max-width: 400px;
  margin: auto;
}
input, select, textarea {
  width: 100%;
  padding: 1rem;
  outline: none;
  border: 1px solid var(--tertiary);
}
input:invalid, select:invalid, textarea:invalid {
  border: 1px solid #ff453a;
}
input:hover, input:focus, select:hover, select:focus, textarea:focus, textarea:hover {
  border: 1px solid var(--orange);
}
</style>