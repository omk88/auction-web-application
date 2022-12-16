<template>
    <p>Profile</p>
    <form @submit.prevent="addItem">
        <div>
            <label>Title:</label><br>
            <input type="text" name="title" v-model="item.title"><br>
            <label>Starting Price:</label><br>
            <input type="number" step="0.01" name="starting_price" v-model="item.starting_price"><br>
            <label>Description:</label><br>
            <input type="text" name="description" v-model="item.description"><br>
            <label>End Date</label><br>
            <input type="date" name="end_date" v-model="item.end_date"><br>
            <label>End Time:</label><br>
            <input type="time" name="end_time" v-model="item.end_time"><br>
            <button type="submit">Submit</button>
        </div>
    </form>

    <form @submit.prevent="editProfile">
        <div>
            <label>Date of Birth:</label><br>
            <input type="date" name="dob" v-model="user.dob"><br>
            <label>Email:</label><br>
            <input type="email" name="email" v-model="user.email"><br>
            <button type="submit">Submit</button>
        </div>
    </form>
</template>

<script>
export default {
}
</script>