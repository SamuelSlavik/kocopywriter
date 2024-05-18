<script lang="ts" setup>
import {inject, ref} from "vue";
import type {NewPriceListItem, PriceListItem} from "@/lib/models";
import {pricingApi} from "@/lib/apiHelpers";
import {useRouter} from "vue-router";

const loading = ref<boolean>(false)
const notificationStore: any = inject('notificationStore')
const router = useRouter()

const newPriceListItem = ref<NewPriceListItem>({
  title: "",
  description: "",
  second_description: "",
  items: [{
    name: "",
    price: 0
  }]
})

const createPriceListItem = async () => {
  try {
    loading.value = true
    const response = await pricingApi.createPriceListItem(newPriceListItem.value)
    if (response.status === 200) {
      await router.push('/admin/pricing')
      notificationStore.addNotification({type: "success", message: "Price list item created successfully"})
    }
  }
  catch (error: any) {
    notificationStore.addNotification({type: "error", message: "Failed to create price list item: " + error.response.data.detail})
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
</script>

<template>
  <Container>
    <Heading>Create Price List Item</Heading>
    <p>Each item can be fully customizable - nothing is required.</p>
    <p>Advising filling at least title or first description if possible.</p>
    <Loader v-if="loading"/>
    <div v-else class="form-block">
      <form @submit.prevent="createPriceListItem">
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