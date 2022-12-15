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
        </div>
    </div>

    <div class="container">

        <form class="form" @submit.prevent=bidItem>
            <div>
                <label>Bid</label>
                <input type="text" v-model="bid" placeholder="Bid">
                <button class="btn" type="submit">Submit</button>
            </div>
        </form>
    </div>
</template>

<script>
export default {
    data() {
        return {
            items: [],
            item: {}
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
        }
    }
}
</script>