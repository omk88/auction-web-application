<template>
  <div>
      <button @click="fetchItems">Get Listings</button>
      <div>
          <ul>
              <li v-for="item in items">
                  {{ item.title }}
                  {{ item.starting_price }}
                  {{ item.description }}
                  {{ item.end_datetime }}
              </li>
          </ul>
      </div>
  </div>
</template>



<script>
export default {
  data() {
      return {
          items: [],
          item: {},
      }
  },
  methods: {
      async fetchItems() {
          let response = await fetch("http://localhost:8000/api/items/" + String)
          let data = await response.json()
          this.items = data.items
      }

      async fetchItems(item_id) {
          let response = await fetch("http://localhost:8000/api/item/" + String(item_id) + "/")
          let data = await response.json()
          this.item = data.item
      }
  }
}
</script>

<style>
/**@import'~bootstrap/dist/css/bootstrap.css'*/
</style>


