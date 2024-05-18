<script setup lang="ts">
import { Swiper, SwiperSlide } from 'swiper/vue';
import { Pagination } from 'swiper/modules';
// Import Swiper styles
import 'swiper/css';
import 'swiper/css/pagination';
import {inject, onMounted, ref} from "vue";
import {useUserStore} from "@/stores/user-store";
import {useRouter} from "vue-router";
import type {Reference} from "@/lib/models";
import {referencesApi} from "@/lib/apiHelpers";
import {backend_url} from "@/lib/constants";
import {formatUrl} from "../../lib/utils";

const modules = [Pagination];

const loading = ref<boolean>(false)
const user = useUserStore()
const router = useRouter()
const notificationStore: any = inject('notificationStore')

const references = ref<Reference[]>([])

const loadReferences = async () => {
  loading.value = true
  try {
    const response = await referencesApi.getReferences()
    references.value = response.data
  } catch (error: any) {
    notificationStore.addNotification({
      type: 'error',
      message: 'Failed to load references: ' + error.response.data.detail,
    })
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  loadReferences()
})
</script>

<template>
  <Container id="section-references">
    <Loader v-if="loading"/>
    <swiper
        v-else
        :modules="modules"
        :pagination="{ clickable: true }"
        :slides-per-view="1"
    >

      <swiper-slide v-for="reference in references" key="reference.id">
        <div class="reference">
          <img :src="backend_url + reference.image" alt="reference.name"/>
          <div class="reference__heading">
            <p><b>{{reference.name}}</b> - {{reference.position}}</p>
            <p><a target="_blank" :href="reference.url">{{formatUrl(reference.url)}}</a></p>
          </div>
          <div class="reference__content">
            <p>{{reference.description}}</p>
          </div>
        </div>
      </swiper-slide>

      <div class="swiper-pagination" slot="pagination" />
    </swiper>
  </Container>
</template>

<style>
.reference {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding-top: 3rem;

  img {
    height: 15rem;
    width: 15rem;
    border-radius: 50%;
  }

  .reference__heading {
    margin-top: 2rem;
    text-align: center;
    width: 60%;
  }

  .reference__content {
    margin-top: 2rem;
    text-align: center;
    width: 60%;
  }
}
.swiper-pagination {
  position: relative;
  margin-top: 2rem;
}
.swiper-pagination-bullet-active {
  background-color: var(--orange);
}
</style>