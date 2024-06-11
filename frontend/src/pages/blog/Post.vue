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
      message: 'Failed to load post: ' + e.response.data.detail,
    })
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  loadPost()
})
</script>

<template>
  <Container :global="true">
    <Loader v-if="loading"/>
    <div class="v-else">
      <div class="post">
        <Heading>{{post.title}}</Heading>
        <p><i>{{formatDate(post.date)}}</i></p>
        <img class="post__thumbnail" v-if="post.image" :src="post.image" alt="thumbnail"/>
        <p class="post__short">{{post.short}}</p>
        <div class="hr"></div>
        <div v-html="post.content" class="post__content"></div>
        <div class="post__signature">
          <img alt="logo" src="@/assets/images/logos/logo.png"/>
          <img alt="logo" src="@/assets/images/logos/logo.png"/>
          <img alt="logo" src="@/assets/images/logos/logo.png"/>
        </div>
        <p>
          Líbil se vám článek? Sledujte mě na
          <a target="_blank" href="https://www.linkedin.com/in/vojtechhulinsky/">LinkedInu</a>, ať vám neuniknou žádné bizarní frky s banální pointou.
        </p>
      </div>
    </div>
  </Container>
</template>

<style>
.post {
  width: 100%;

   .post__thumbnail {
     width: 60%;
     margin: 2rem auto;
   }
  .post__short {
    width: 60%;
    margin: auto;
  }
  .post__content {
    text-align: left;

    img {
      width: 100%;
      height: auto;
    }

    ul {
      list-style-image: url("@/assets/images/logos/favicon.png");
      padding-left: 2rem;
    }
    ol {
      list-style-type: decimal;
      padding-left: 3rem;
    }
  }
  .post__signature {
    display: flex;
    justify-content: center;
    gap: 1rem;
    margin: 3rem 0;

    img {
      width: 5rem;
      height: auto;
    }
  }
}
</style>