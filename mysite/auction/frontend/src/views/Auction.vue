<template>
    <p>Auction</p>

    <form @submit.prevent="bidIem">
        <div>
            <label>Bid</label>
            <input type="text" v-model="bid.amount" placeholder="Enter amount">
            <input hidden v-model="bid.item" placeholder="">
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
</template>

<script>
export default {
    
}
</script>