<script setup lang="ts">
import {inject, onMounted, ref} from "vue";
import {useRouter} from "vue-router";
import {useUserStore} from "@/stores/user-store";
import type { PriceListItem } from "@/lib/models";
import {pricingApi} from "@/lib/apiHelpers";
// @ts-ignore
import Pencil from "vue-material-design-icons/Pencil.vue";
// @ts-ignore
import Delete from "vue-material-design-icons/Delete.vue";

const loading = ref<boolean>(false)
const user = useUserStore()
const router = useRouter()
const notificationStore: any = inject('notificationStore')

const priceListItems = ref<PriceListItem[]>([])

const loadData = async () => {
  try {
    loading.value = true
    const response = await pricingApi.getPriceListItems()
    priceListItems.value = response.data
  } catch (error: any) {
    notificationStore.addNotification({type: 'error', message: "failed to load price list items" + error.response.data.detail})
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
        await loadData()
      }
    } catch (error: any) {
      notificationStore.addNotification({type: 'error', message: "Failed to delete item: " + error.response.data.detail})
    }
  }
}

onMounted(() => {
  loadData()
})

</script>

<template>
  <Container>
    <Heading>Price list items</Heading>
    <p>Price list items displayed in section "cenník".</p>
    <div class="hr"></div>
    <Loader v-if="loading"/>
    <div class="table" v-else>
      <div class="table__row" v-for="item in priceListItems" key="item.id">
        <div class="table--1">
          <p>{{item.id}}</p>
        </div>
        <div class="table--6">
          <router-link :to="'/admin/pricing/detail/' + item.id">{{item.title}}</router-link>
        </div>
        <div class="table--1">

        </div>
        <div class="table__toolbar">
          <router-link :to="'/admin/pricing/edit/' + item.id"><Pencil :size="24" /></router-link>
          <a @click="deleteItem(item.id)"><Delete :size="24" /></a>
        </div>
      </div>
    </div>
  </Container>
</template>

<style>
.table {
  width: 100%;
  background-color: rgb(246, 246, 247);
  border-radius: 5px;
  margin: 2rem 0;
  padding: 1rem;
  position: relative;

  .table__row {
    width: 100%;
    display: flex;
    justify-content: left;
    border-bottom: solid 1px rgba(60, 60, 67, 0.12);
    padding: 1rem;
    margin: 0;
  }
  .table__row:last-child {
    border-bottom: none;
  }

  .table__toolbar {
    text-align: right;
    display: flex;
    justify-content: right;
    gap: 1rem;
    flex: 1;

    a:hover {
      fill: var(--orange);
      cursor: pointer;
    }

    svg:hover {
      fill: var(--orange);
      cursor: pointer;
    }
  }

  .table--1 {
    flex: 1;
  }
  .table--2 {
    flex: 2;
  }
  .table--3 {
    flex: 3;
  }
  .table--4 {
    flex: 4;
  }
  .table--5 {
    flex: 5;
  }
  .table--6 {
    flex: 6;
  }
  .table--7 {
    flex: 7;
  }
  .table--8 {
    flex: 8;
  }
}
</style>