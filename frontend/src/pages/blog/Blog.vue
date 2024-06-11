<script setup lang="ts">
import {inject, onMounted, ref} from "vue";
import {useUserStore} from "@/stores/user-store";
import {useRouter} from "vue-router";
import type {Post} from "@/lib/models";
import {postsApi} from "@/lib/apiHelpers";
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

</script>

<template>
  <Container :global="true">
    <Heading>Články</Heading>
    <div class="hr"></div>
    <Loader v-if="loading"/>
    <div v-else class="blog">
      <article class="blog-post" v-for="(post, index) in posts" key="post.id">
        <div class="blog-post__image">
          <router-link :to="'/blog/' + post.id">
            <img v-if="post.image" :src="post.image" alt="thumbnail"/>
          </router-link>
        </div>
        <div class="blog-post__content">
          <Heading><router-link :to="'/blog/' + post.id">{{post.title}}</router-link></Heading>
          <p><i>{{formatDate(post.date)}}</i></p>
          <p>{{post.short}}</p>
        </div>
      </article>
    </div>
  </Container>
</template>

<style>
.blog {
  width: 80%;
  margin: auto;

  article {
    width: 100%;
    text-align: left;
    display: flex;
    justify-content: space-between;
    margin-bottom: 6rem;
    flex-wrap: wrap;

    .blog-post__image {
      width: 30%;
      @media (max-width: 1024px) {
        width: 100%;
      }

      img {
        width: 100%;
        height: auto;
      }
    }

    .blog-post__content {
      width: 65%;

      h2 {
        font-size: 1.5rem;
      }
    }
  }
}
</style>