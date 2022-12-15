<template>
    <form @submit.prevent="searchItems">
        <div>
            <label>Search</label>
            <input type="text" v-model="searchText" placeholder="Search">
            <button type="submit">Submit</button>
        </div>
    </form>
    <form @submit.prevent="sendQuestion">
        <div>
            <label>Question</label>
            <input type="text" v-model="searchText" placeholder="Search">
            <button type="submit">Submit</button>
        </div>
    </form>

    <form @submit.prevent="sendAnswer">
        <div>
            <label>Answer</label>
            <input type="text" v-model="searchText" placeholder="Search">
            <button type="submit">Submit</button>
        </div>
    </form>
    
    <form @submit.prevent="bidItem">
        <div>
            <label>Bid</label>
            <input type="text" placeholder="Enter amount">
            <button type="submit">Submit</button>
        </div>
    </form>

    <div>
        <button @click="fetchItems">Get Listings</button>
        <div>
            
            <ul>
                <li v-for="item in items" :key="item.id">
                    {{ item.title }}
                    {{ item.starting_price }}
                    {{ item.description }}
                    {{ item.end_date }}
                    {{ item.end_time }}
                    {{ item.id }}
                    <form @submit.prevent="bidItem(item.id)">
                        <div>
                            <label>Bid</label>
                            <input type="text" v-model="bidAmount" placeholder="Enter amount">
                            <input hidden placeholder="">
                            <button type="submit">Submit</button>
                        </div>
                    </form>
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
            bids: [],
            bid: {},
            questions: [],
            answers: [],
            question: {},
            answer: {},
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

        async fetchBids(item_id) {
            let response = await fetch(
                "http://localhost:8000/api/bids/" + String(item_id) + "/",
                {
                    credentials: "include",
                    mode: "cors",
                    referrerPolicy: "no-referrer",
                }
                );
            let data = await response.json();
            this.bids = data.bids;
        },

        async fetchQuestions(item_id) {
            let response = await fetch(
                "http://localhost:8000/api/questions/" + String(item_id) + "/",
                {
                    credentials: "include",
                    mode: "cors",
                    referrerPolicy: "no-referrer",
                }
                );
            let data = await response.json();
            this.questions = data.questions;
        },

        async fetchAnswers(item_id) {
            let response = await fetch(
                "http://localhost:8000/api/answers/" + String(question_id) + "/",
                {
                    credentials: "include",
                    mode: "cors",
                    referrerPolicy: "no-referrer",
                }
                );
            let data = await response.json();
            this.answers = data.answers;
        },

        async searchItems() {
            let response = await fetch('http://localhost:8000/api/search/', 
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
            let data = await response.json();
            this.items = data.items;
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
        },

        async sendQuestion(item_id) {
            var obj = {item: item_id, question: this.questionText};
            let response = await fetch('http://localhost:8000/api/question/', 
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
            this.question = data.question;
        },

        async sendAnswer(item_id, question_id) {
            var obj = {item: item_id, question: question_id, answer: this.answerText};
            let response = await fetch('http://localhost:8000/api/answer/', 
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
            this.answer = data.answer;
        },        
    }
}
</script>


