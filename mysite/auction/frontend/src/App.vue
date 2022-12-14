<template>
    <form @submit.prevent="searchItems">
        <div>
            <label>Search</label>
            <input type="text" v-model="searchText" placeholder="Search">
            <button type="submit">Submit</button>
        </div>
    </form>

    <form @submit.prevent="bidItem">
        <div>
            <label>Bid</label>
            <input type="text" v-model="bid" placeholder="Bid">
            <button type="submit">Submit</button>
        </div>
    </form>

    <div>
        <button @click="fetchItems">Get Listings</button>
        <div>
            <ul>
                <li v-for="item in items">
                    {{ item.title }}
                    {{ item.starting_price }}
                    {{ item.description }}
                    {{ item.end_date }}
                    {{ item.end_time }}
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
            let response = await fetch(
                "http://localhost:8000/api/items/",
                {
                    credentials: "include",
                    mode: "cors",
                    referrerPolicy: "no-referrer",
                }
                );
        let data = await response.json();
        this.items = data.items;
        },

        async fetchItem(item_id) {
            let response = await fetch(
                "http://localhost:8000/api/item/" + String(item_id) + "/",
                {
                    credentials: "include",
                    mode: "cors",
                    referrerPolicy: "no-referrer",
                }
                );
            let data = await response.json();
            this.item = data.item;
        },

        async searchItems() {
            fetch('http://localhost:8000/api/search/', 
            {
                method: "post",
                credentials: "include",
                mode: "cors",
                referrerPolicy: "no-referrer",
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(this.searchText)
            }
            );
        }
    }
}
</script>


