<script setup lang="ts">
import {useUserStore} from "@/stores/user-store";
import {useRouter} from "vue-router";
import {inject} from "vue";

const user = useUserStore()
const router = useRouter()
const notificationStore: any = inject('notificationStore')


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
  <div class="dashboard">
    <div v-if="user.token"></div>
    <div v-else class="dashboard__content">
      <div>
        <p>{{user.email}}</p>
      </div>
      <div class="hr"></div>
      <div>
        <p><router-link to="/admin/profile/edit">Edit profile</router-link></p>
        <br/>
        <p><router-link to="/admin/headline/edit">Edit headline</router-link></p>
        <br/>
        <p><router-link to="/admin/images">Manage images</router-link></p>
        <p><router-link to="/admin/images/create">Add image</router-link></p>
        <br/>
        <p><router-link to="/admin/brands">Manage brands</router-link></p>
        <p><router-link to="/admin/brands/create">Add brand</router-link></p>
        <br/>
        <p><router-link to="/admin/pricing">Manage price list items</router-link></p>
        <p><router-link to="/admin/pricing/create">Create new price list item</router-link></p>
        <br/>
        <p><router-link to="/admin/references">Manage references</router-link></p>
        <p><router-link to="/admin/references/create">Create new reference</router-link></p>
        <br/>
        <p><router-link to="/admin/projects">Manage projects</router-link></p>
        <p><router-link to="/admin/projects/create">Create new project</router-link></p>
        <br/>
        <p><router-link to="/admin/posts">Manage posts</router-link></p>
        <p><router-link to="/admin/posts/create">Create new post</router-link></p>
      </div>
      <div class="hr"></div>
      <div>
        <button @click="logout" class="button">Log Out</button>
      </div>
    </div>
  </div>
</template>

<style>
.dashboard {
  background-color: rgb(246, 246, 247);
  width: calc((100% - (1280px - 64px)) / 2 + 350px - 32px);
  min-width: 350px;
  height: auto;
  min-height: 100vh;

  .dashboard__content {
    width: 350px;
    margin-right: 0;
    margin-left: auto;
    padding: 2rem 2rem 2rem 1rem;

    a {
      color: var(--secondary)
    }
    .router-link-active {
      color: var(--orange)
    }
  }
}
</style>