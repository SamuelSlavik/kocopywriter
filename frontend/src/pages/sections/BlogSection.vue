<script setup lang="ts">

import {ref} from "vue";

const loading = ref(false)

const latestPost = ref()
const topPosts = ref()

const fetchLatestPost = async () => {
  loading.value = true
  try {
  } catch (error) {
    console.error(error)
  } finally {
    loading.value = false
  }
}

const fetchTopPosts = async () => {
  loading.value = true
  try {
  } catch (error) {
    console.error(error)
  } finally {
    loading.value = false
  }
}

</script>

<template>
  <Container id="section-blog">
    <div class="latest-post-container">
      post
    </div>
    <div class="top-posts-container">
      posts
    </div>
  </Container>
</template>

<style>
#section-blog {
  display: flex;
  justify-content: space-between;

  .latest-post-container {
    width: 40%;
  }

  .top-posts-container {
    width: 55%;
  }
}
</style>