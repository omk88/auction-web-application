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

            <span class="item-title">{{item.title}}<br></span>
            <span class="item-price">{{item.starting_price}}<br></span>
            <span class="item-description">{{item.description}}<br></span>
            <span class="item-end_date">{{item.end_date}}<br></span>
            <span class="item-end_time">{{item.end_time}}<br></span>
            <span class="item-id">{{item.id}}<br></span>
        </div>
    </div>

    <div class="container">

        
    </div>
</template>

<script>
export default {
    data() {
        return {
            items: [],
            item: {},
            bid: {}
        }
    },
    mounted() {
        this.fetchItems()
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

        async bidItem(item_id) {
            var obj = {item: item_id, amount: this.bidAmount};
            let response = await fetch('http://localhost:8000/api/bid/', 
            {
                method: "post",
                credentials: "include",
                mode: "cors",
                referrerPolicy: "no-referrer",
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(obj)
            }
            );
            let data = await response.json();
            this.bid = data.bid;
        }
    }
}
</script>