<script setup lang="ts">
import {inject, onMounted, ref} from "vue";
import {useRouter} from "vue-router";
import {useUserStore} from "@/stores/user-store";
import {userApi} from "@/lib/apiHelpers";

const loading = ref<boolean>(false)
const user = useUserStore()
const router = useRouter()
const notificationStore: any = inject('notificationStore')

const newEmail = ref<string>('')
const newEmailConfirm = ref<string>('')

const newPassword = ref<string>('')
const newPasswordConfirm = ref<string>('')

const loadUser = async () => {
  try {
    loading.value = true
    const response: any = await userApi.retrieveCurrentUser()
    newEmail.value = user.email
    if (response.status != 200) {
      await router.push('/login')
    }
  } catch (error: any) {
    notificationStore.addNotification({type: "error", message: "Failed to get user: " + error.response.data.detail})
  } finally {
    loading.value = false
  }
}

const submitEmail = async () => {
  if (newEmail.value !== newEmailConfirm.value) {
    console.log("a")
    notificationStore.addNotification({type: 'error', message: "Emails do not match"})
    return
  }

  try {
    const response = await userApi.updateEmail(newEmail.value)
    if (response.status === 200) {
      await loadUser()
      notificationStore.addNotification({type: 'success', message: "Email updated"})
    }
  } catch (error: any) {
    notificationStore.addNotification({type: 'error', message: "Failed to update email: " + error.response.data.detail})
  } finally {
    loading.value = false
  }
}

const submitPassword = async () => {
if (newPassword.value !== newPasswordConfirm.value) {
    notificationStore.addNotification({type: 'error', message: "Passwords do not match"})
    return
  }

  const passwordRegex = /^(?=.*[0-9])(?=.*[a-zA-Z]).{8,}$/;
  if (!passwordRegex.test(newPassword.value)) {
    notificationStore.addNotification({
      type: 'error',
      message: 'Password must contain at least 8 characters and a number.',
    });
    return;
  }

  try {
    const response = await userApi.updatePassword(newPassword.value)
    if (response.status === 200) {
      await loadUser()
      notificationStore.addNotification({type: 'success', message: "Password updated"})
    }
  } catch (error: any) {
    notificationStore.addNotification({type: 'error', message: "Failed to update password: " + error.response.data.detail})
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  loadUser()
})

</script>

<template>
  <Container>
    <Heading>Edit Profile</Heading>
    <div class="hr"></div>
    <Loader v-if="loading"/>
    <div v-else>
      <p>Enter valid email: admin@admin.com</p>

      <div class="form-block">
        <form @submit.prevent="submitEmail">
          <input
              type="email"
              name="email"
              placeholder="Email"
              v-model="newEmail"
              required
          />
          <input
              type="email"
              name="email-confirm"
              placeholder="Confirm Email"
              v-model="newEmailConfirm"
              required
          />
          <button disabled type="submit" class="button">Update Email</button>
        </form>
      </div>
    </div>

    <div class="hr"></div>

    <Loader v-if="loading"/>
    <div v-else>
      <p>Valid password contains:</p>
      <ul>
        <li>At least 8 chars</li>
        <li>At least 1 number</li>
      </ul>
      <div class="form-block">
        <form @submit.prevent="submitPassword">
          <input
              type="password"
              name="password"
              placeholder="Password"
              v-model="newPassword"
              required
          />
          <input
              type="password"
              name="password-confirm"
              placeholder="Confirm Password"
              v-model="newPasswordConfirm"
              required
          />
          <button disabled type="submit" class="button">Update Password</button>
        </form>
      </div>
    </div>

  </Container>
</template>

<style>

</style>