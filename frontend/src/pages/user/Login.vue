<script setup lang="ts">
import {ref} from "vue";
import {useRouter} from "vue-router";
import { inject } from 'vue'
import {useUserStore} from "@/stores/user-store";
import {userApi} from "@/lib/apiHelpers";


const router = useRouter()
const notificationStore: any = inject('notificationStore')
const loading = ref<boolean>(false)
const user = useUserStore()

const email = ref<string>("")
const password = ref<string>("")

const login = async () => {
  try {
    const response: any = await userApi.login({email: email.value, password: password.value})
    localStorage.setItem("token", response.data.access_token)

    if (response.status === 200) {
      try {
        const response: any = await userApi.retrieveCurrentUser()
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
form {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}
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
input, select, textarea, .tiptap {
  width: 100%;
  padding: 1rem;
  outline: none;
  border: 1px solid var(--tertiary);
  font-size: 0.9rem;
}
input:invalid, select:invalid, textarea:invalid, .tiptap:invalid {
  border: 1px solid #ff453a;
}
input:hover, .tiptap:focus, .tiptap:hover input:focus, select:hover, select:focus, textarea:focus, textarea:hover {
  border: 1px solid var(--orange);
}
.form-block {
  padding: 3rem 0;
  text-align: left;
}
label {
  margin-bottom: 0;
  padding-bottom: 0;
}
.form-row {
  display: flex;
  gap: 1rem;
  align-items: center;

}
.file-input-wrapper {
  display: flex;
  gap: 1rem;
  align-items: center;
}

</style>