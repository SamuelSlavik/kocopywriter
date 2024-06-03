<script setup lang="ts">
import {inject, onMounted, ref} from "vue";
import {useUserStore} from "@/stores/user-store";
import {useRouter} from "vue-router";
import {postsApi} from "@/lib/apiHelpers";
import type {Post} from "@/lib/models";
import {formatDate} from "@/lib/utils";

const loading = ref<boolean>(false)
const user = useUserStore()
const router = useRouter()
const notificationStore: any = inject('notificationStore')

const latestPost = ref<Post>({
  id: "",
  title: "",
  content: "",
  date: "",
  short: "",
  image: ""
})
const posts = ref<Post[]>([])

const getLatestPost = async () => {
  loading.value = true
  try {
    const response = await postsApi.getLatestPost()
    latestPost.value = response.data
  } catch (error: any) {
    notificationStore.addNotification({
      type: 'error',
      message: 'Failed to load latest post: ' + error.response.data.detail,
    })
  } finally {
    loading.value = false
  }
}

const getPosts = async () => {
  loading.value = true
  try {
    const response = await postsApi.getNextToLatestPosts()
    posts.value = response.data
  } catch (error: any) {
    notificationStore.addNotification({
      type: 'error',
      message: 'Failed to load posts',
    })
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  getLatestPost()
  getPosts()
})

</script>

<template>
  <Container id="section-blog">
    <div class="section-blog__heading">
      <Heading>Blog</Heading>
    </div>
    <div class="section-blog">
      <div class="latest-post-container">
        <router-link :to="'/blog/' + latestPost.id">
          <img v-if="latestPost?.image" :src="latestPost.image" alt="thumbnail"/>
        </router-link>
        <h2><router-link :to="'/blog/' + latestPost.id">{{latestPost?.title}}</router-link></h2>
        <p><i>{{formatDate(latestPost?.date)}}</i></p>
        <div class="hr"></div>
        <p>{{latestPost.short}}</p>
      </div>
      <div class="top-posts-container">
        <div class="top-post" v-for="post in posts" :key="post.id">
          <div class="top-post__image">
            <router-link :to="'/blog/' + post.id">
              <img v-if="post?.image" :src="post.image" alt="thumbnail"/>
            </router-link>
          </div>
          <div class="top-post__content">
            <h2><router-link :to="'/blog/' + post.id">{{post?.title}}</router-link></h2>
            <p><i>{{formatDate(post?.date)}}</i></p>
            <p>{{post.short}}</p>
          </div>
        </div>
        <button class="button" @click="router.push('/blog')">Kukuk na všechny</button>
      </div>
    </div>
  </Container>
</template>

<style>
#section-blog {
  margin-top: 6rem;
  @media (max-width: 1024px) {
    margin-top: 6rem;
  }
}
.section-blog__heading {
  margin-bottom: 4rem;
  text-align: center;
}
.section-blog {
  display: flex;
  justify-content: space-between;
  flex-wrap: wrap;
  margin-bottom: 4rem;

  .latest-post-container {
    width: 40%;
    @media (max-width: 1024px) {
      width: 100%;
      margin-bottom: 6rem;

      .hr {
        display: none;
      }
    }

    img {
      width: 100%;
      height: auto;
    }
  }

  .top-posts-container {
    width: 50%;
    @media (max-width: 1024px) {
      width: 100%;
    }

    .top-post {
      width: 100%;
      display: flex;
      justify-content: space-between;
      margin-bottom: 4rem;

      .top-post__image {
        width: 40%;
        height: auto;
        img {
          width: 100%;
          height: auto;
        }
      }

      .top-post__content {
        width: 58%;
      }
    }
  }
}
</style>