<script setup lang="ts">
import {inject, onMounted, ref} from "vue";
import {useRouter} from "vue-router";
import {useUserStore} from "@/stores/user-store";
import type {Post} from "@/lib/models";
import {postsApi} from "@/lib/apiHelpers";
// @ts-ignore
import Pencil from "vue-material-design-icons/Pencil.vue";
// @ts-ignore
import Delete from "vue-material-design-icons/Delete.vue";
import {formatDate} from "@/lib/utils";

const loading = ref<boolean>(false)
const user = useUserStore()
const router = useRouter()
const notificationStore: any = inject('notificationStore')

const posts = ref<Post[]>([])

const loadPosts = async () => {
  try {
    loading.value = true
    const response = await postsApi.getPosts()
    posts.value = response.data
  } catch (error: any) {
    notificationStore.addNotification({
      type: 'error',
      message: 'Failed to load posts: ' + error.response.data.detail,
    })
  } finally {
    loading.value = false

  }
}

onMounted(() => {
  loadPosts()
})

const deletePost = async (id: string) => {
  const confirm = window.confirm("Are you sure you want to delete this post?")

  if (confirm) {
    try {
      const response = await postsApi.deletePost(id)
      if (response.status === 200) {
        notificationStore.addNotification({type: 'success', message: "Post deleted"})
        await loadPosts()
      }
    } catch (error: any) {
      notificationStore.addNotification({type: 'error', message: "Failed to delete post: " + error.response.data.detail})
    }
  }
}

</script>

<template>
  <Container>
    <Heading>Manage Posts</Heading>
    <p>Posts displayed in the blog section.</p>
    <p>Ordered by their date</p>
    <div class="hr"></div>
    <Loader v-if="loading"/>
    <div v-else>
      <div class="table">
        <div class="table__row" v-for="post in posts" :key="post.id">
          <div class="table--1">
            <p>{{post.id}}</p>
          </div>
          <div class="table--6">
            <router-link :to="'/admin/posts/detail/' + post.id">{{post.title}}</router-link>
          </div>
          <div class="table--2">
            <p>{{formatDate(post.date)}}</p>
          </div>
          <div class="table--1">

          </div>
          <div class="table__toolbar">
            <router-link :to="'/admin/posts/edit/' + post.id"><Pencil :size="24" /></router-link>
            <a @click="deletePost(post.id)"><Delete :size="24" /></a>
          </div>
        </div>
      </div>
    </div>
  </Container>
</template>

<style>

</style>