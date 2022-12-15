<template>
    <div>
        <section>
            <div class="home">
                <title>Check out the items for auction!</title>
            </div>
        </section>

        <div class="item-desc" v-for="item in items" v-bind:key="item.id">
            <figure class="item-image" >
                <img v-bind:src="item.item_image"/>
            </figure>

            <span class="item-title">{{item.title}}</span>
            <span class="item-price">{{item.starting_price}}</span>
        </div>
    </div>    
</template>

<script>
export default {
    name: 'Home',
    data() {
        return {
            items: [],
            item: {}
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