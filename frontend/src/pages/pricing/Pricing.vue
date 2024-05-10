<script setup lang="ts">
import {useUserStore} from "@/stores/user-store";
import {inject, onMounted, ref} from "vue";
import type {Headline, PriceListItem} from "@/lib/models";
import {headlineApi, pricingApi} from "@/lib/apiHelpers";
import {useRouter} from "vue-router";

const user = useUserStore()
const router = useRouter()
const loading = ref<boolean>(false)
const notificationStore: any = inject('notificationStore')

const priceListItems = ref<PriceListItem[]>([])

const loadPriceListItems = async () => {
  try {
    loading.value = true
    const response = await pricingApi.getPriceListItems()
    priceListItems.value = response.data
  } catch (error: any) {
    notificationStore.addNotification({type: "error", message: "Failed to get price list items: " + error.message})
  } finally {
    loading.value = false
  }
}


onMounted(() => {
  loadPriceListItems()
})
</script>

<template>
  <Container :global="true">
    <Heading>Ceník ko-copywritingu</Heading>
    <Loader v-if="loading"/>
    <div v-else>
      <div class="price-list-item-wrapper">
        <div v-for="priceListItem in priceListItems" :key="priceListItem.id">
          <h3>{{priceListItem.title}}</h3>
          <p>{{priceListItem.description}}</p>
          <p>{{priceListItem.second_description}}</p>
          <div v-for="item in priceListItem.items" :key="item.name" class="item-with-price-wrapper">
            <p>{{ item.name }}</p>
            <p>&nbsp;-&nbsp;</p>
            <p><b>{{ item.price }} Kč</b></p>
          </div>
        </div>
      </div>
    </div>
  </Container>
</template>

<style>
.price-list-item-wrapper {
  display: flex;
  flex-direction: column;
  gap: 2rem;

}
.item-with-price-wrapper {
  display: flex;
  justify-content: center;

}
</style>