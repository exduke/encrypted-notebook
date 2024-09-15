<template>
    <div class="notebook-main">
        <el-input v-model="data.title" placeholder="title" />
        <el-input v-model="data.content" placeholder="content" type="textarea"
            :autosize="{ minRows: 10, maxRows: 20 }" />
    </div>
</template>

<script setup>
import { defineModel } from 'vue'

//model
const data = defineModel()

</script>

<style>
.notebook-main{
    width: 90%;
}

.notebook-main>* {
    font-size: 1.25rem;
    margin-top: 20px;
}
</style>