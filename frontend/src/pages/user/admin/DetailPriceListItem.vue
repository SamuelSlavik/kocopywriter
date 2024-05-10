<script setup lang="ts">
import {inject, onMounted, ref} from "vue";
import {useRouter} from "vue-router";
import {useUserStore} from "@/stores/user-store";
import {pricingApi} from "@/lib/apiHelpers";
import type {PriceListItem} from "@/lib/models";
import Delete from "vue-material-design-icons/Delete.vue";
import Pencil from "vue-material-design-icons/Pencil.vue";

const loading = ref<boolean>(false)
const user = useUserStore()
const router = useRouter()
const notificationStore: any = inject('notificationStore')

const itemId = router.currentRoute.value.params.id.toString() || ""

const priceListItem = ref<PriceListItem>({
  id: "",
  title: "",
  description: "",
  second_description: "",
  items: []
})

const loadData = async () => {
  try {
    loading.value = true
    const response = await pricingApi.getPriceListItem(itemId)
    priceListItem.value = response.data
  } catch (error: any) {
    notificationStore.addNotification({type: 'error', message: "failed to load price list item" + error.message})
  } finally {
    loading.value = false

  }
}

const deleteItem = async (id: string) => {
  const confirm = window.confirm("Are you sure you want to delete this item?")

  if (confirm) {
    try {
      const response = await pricingApi.deletePriceListItem(id)
      if (response.status === 200) {
        notificationStore.addNotification({type: 'success', message: "Item deleted"})
        await router.push("/admin/pricing")
      }
    } catch (error: any) {
      notificationStore.addNotification({type: 'error', message: "Failed to delete item: " + error.message})
    }
  }
}


onMounted(() => {
  loadData()
})

</script>

<template>
  <Container>
    <Loader v-if="loading"/>
    <div v-else v-if="priceListItem.id">
      <Heading>{{priceListItem.title || "No title provided"}}</Heading>
      <div class="toolbar">
        <router-link :to="'/admin/pricing/edit/' + priceListItem.id"><Pencil :size="24" /></router-link>
        <a @click="deleteItem(priceListItem.id)"><Delete :size="24" /></a>
      </div>
      <div class="hr"></div>
      <p v-if="priceListItem.description"><b>Description: </b>{{priceListItem.description}}</p>
      <p v-if="priceListItem.second_description"><b>Second description: </b>{{priceListItem.second_description}}</p>
      <div v-for="item in priceListItem.items" :key="item.name" class="item-with-price-wrapper">
        <p>{{ item.name }}</p>
        <p>&nbsp;-&nbsp;</p>
        <p><b>{{ item.price }} Kč</b></p>
      </div>
    </div>
  </Container>
</template>

<style scoped>
.item-with-price-wrapper {
  display: flex;
  justify-content: left;
  gap: 0.5rem;
}
</style>