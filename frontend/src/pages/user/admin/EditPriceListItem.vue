<script setup lang="ts">
import {useUserStore} from "@/stores/user-store";
import {inject, onMounted, ref} from "vue";
import type {Headline, NewPriceListItem} from "@/lib/models";
import {headlineApi, pricingApi} from "@/lib/apiHelpers";
import {useRouter} from "vue-router";

const router = useRouter()
const loading = ref<boolean>(false)
const notificationStore: any = inject('notificationStore')

const item_id = ref<string>(router.currentRoute.value.params.id.toString()) || ""

const newPriceListItem = ref<NewPriceListItem>({
  title: "",
  description: "",
  second_description: "",
  items: [{
    name: "",
    price: 0
  }]
})

const updatePriceListItem = async () => {
  try {
    const response = await pricingApi.updatePriceListItem(item_id.value, newPriceListItem.value)
    if (response.status === 200) {
      await router.push('/admin/pricing')
      notificationStore.addNotification({type: "success", message: "Price list item updated successfully"})
    }
  }
  catch (error: any) {
    notificationStore.addNotification({type: "error", message: "Failed to update price list item: " + error.response.data.detail})
  }
  finally {
    loading.value = false
  }
}

const addItemWithPrice = () => {
  newPriceListItem.value.items.push({
    name: "",
    price: 0
  })
}

const loadData = async () => {
  try {
    loading.value = true
    const response = await pricingApi.getPriceListItem(item_id.value)
    newPriceListItem.value = response.data
  } catch (error: any) {
    notificationStore.addNotification({type: 'error', message: "failed to load price list item" + error.response.data.detail})
  } finally {
    loading.value = false

  }
}

onMounted(() => {
  loadData()
})
</script>

<template>
  <Container>
    <Heading>Edit Price list item</Heading>
    <p>Each item can be fully customizable - nothing is required.</p>
    <p>Advising filling at least title or first description if possible.</p>
    <Loader v-if="loading"/>
    <div v-else class="form-block">
      <form @submit.prevent="updatePriceListItem">
        <div>
          <label>Title</label>
          <input
              type="text"
              name="title"
              v-model="newPriceListItem.title"
              placeholder="Title"
          />
        </div>
        <div>
          <label>Description</label>
          <input
              type="text"
              name="description"
              v-model="newPriceListItem.description"
              placeholder="Description"
          />
        </div>
        <div>
          <label>Second Description</label>
          <input
              type="text"
              name="second_description"
              v-model="newPriceListItem.second_description"
              placeholder="Second Description"
          />
        </div>
        <br/>
        <div>
          <label>Items with price</label>
          <div class="file-input-wrapper" v-for="(item, index) in newPriceListItem.items">
            <input
                type="text"
                name="name"
                v-model="item.name"
                placeholder="Name"
                required
            />
            <input
                type="number"
                name="price"
                v-model="item.price"
                placeholder="Price"
                required
            />
            <button
                class="button"
                type="button"
                @click="() => newPriceListItem.items.splice(index, 1)"
            >Remove Item</button>
          </div>
        </div>
        <button
            class="button"
            type="button"
            @click="addItemWithPrice"
        >
          Add new item
        </button>
        <br/>
        <button
            class="button"
            type="submit"
        >Submit</button>
      </form>
    </div>
  </Container>
</template>

<style>

</style>