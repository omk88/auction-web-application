<template>
    <form @submit.prevent="searchItems">
        <div>
            <label>Search</label>
            <input type="text" v-model="searchText" placeholder="Enter text here...">
            <button type="submit">Submit</button>
        </div>
    </form>
    <form @submit.prevent="sendQuestion(1)">
        <div>
            <label>Question</label>
            <input type="text" v-model="questionText" placeholder="Enter text here...">
            <button type="submit">Submit</button>
        </div>
    </form>

    <form @submit.prevent="sendAnswer(1, 2)">
        <div>
            <label>Answer</label>
            <input type="text" v-model="answerText" placeholder="Enter text here...">
            <button type="submit">Submit</button>
        </div>
    </form>

    <div>
        <button @click="fetchItems">Get Listings</button>
        <button @click="getUser">Get User</button>
        <button @click="fetchBids(1)">Get Bid</button>
        <button @click="fetchQuestions(1)">Get Question</button>
        <button @click="fetchAnswers(1)">Get Answer</button>
        <div> 
            <ul>
                <li v-for="item in items" :key="item.id">
                    <img v-bind:src="sliceString(item.item_image)" id="item_pic"/>
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
            user: {},
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

        async fetchAnswers(question_id) {
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

        async getUser() {
            let response = await fetch(
                "http://localhost:8000/api/user/",
                {
                    credentials: "include",
                    mode: "cors",
                    referrerPolicy: "no-referrer",
                }
                );
        let data = await response.json();
        this.user = data.user;
        },

        sliceString(string) {
            string = String(string);
            var result = string.substring(string.lastIndexOf("/"));
            return result;
            
        }
    }
}

</script>


