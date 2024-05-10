<script setup lang="ts">
import {inject, onMounted, ref} from "vue";
import {useRouter} from "vue-router";
import {useUserStore} from "@/stores/user-store";
// @ts-ignore
import Pencil from "vue-material-design-icons/Pencil.vue";
// @ts-ignore
import Delete from "vue-material-design-icons/Delete.vue";
import type {Post} from "@/lib/models";
import {postsApi} from "@/lib/apiHelpers";
import {backend_url} from "@/lib/constants";
import {formatDate} from "../../../lib/utils";

const loading = ref<boolean>(false)
const user = useUserStore()
const router = useRouter()
const notificationStore: any = inject('notificationStore')

const postId = router.currentRoute.value.params.id.toString() || ""

const post = ref<Post>({
      id: "",
      title: "",
      content: "",
      date: "",
      short: "",
      image: ""
    }
)

const loadPost = async () => {
  try {
    loading.value = true
    const response = await postsApi.getPost(postId)
    post.value = response.data
  } catch (e: any) {
    notificationStore.addNotification({
      type: 'error',
      message: 'Failed to load post',
    })
  } finally {
    loading.value = false
  }
}

const deletePost = async (id: string) => {
  const confirm = window.confirm("Are you sure you want to delete this post?")

  if (confirm) {
    try {
      const response = await postsApi.deletePost(id)
      if (response.status === 200) {
        notificationStore.addNotification({type: 'success', message: "Post deleted"})
        await router.push("/admin/posts")
      }
    } catch (error: any) {
      notificationStore.addNotification({type: 'error', message: "Failed to delete post: " + error.message})
    }
  }
}

onMounted(() => {
  loadPost()
})


</script>

<template>
  <Container>
    <Loader v-if="loading"/>
    <div v-else v-if="post.title">
      <Heading>{{post.title}}</Heading>
      <div class="toolbar">
        <router-link :to="'/admin/posts/edit/' + post.id"><Pencil :size="24" /></router-link>
        <a @click="deletePost(post.id)"><Delete :size="24" /></a>
      </div>
      <div class="hr"></div>
      <p><b>Date: </b>{{formatDate(post.date)}}</p>
      <p><b>Short description: </b>{{post.short}}</p>
      <img class="image-detail" :src="backend_url + post.image" alt="thumbnail" v-if="post.image"/>
      <div class="hr"></div>
      <div v-html="post.content"></div>
    </div>
  </Container>
</template>

<style>

</style>