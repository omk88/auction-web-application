<template>
    <p>Auction</p>

    <form @submit.prevent="bidItem(item.id)">
        <div>
            <label>Bid</label>
            <input type="text" v-model="bidAmount" placeholder="Enter amount">
            <input hidden placeholder="">
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
</template>

<script>
export default {
}
</script>