<template>
    <div class="notebook-side-node">
        <div class="self">

            <div class="title" :class="{ chosen: data.chosen, empty: !data.title }" @click="emit('chosen', [])">
                {{ data.title ? data.title : 'none title'}}
            </div>

            <el-icon v-if="data.children.length" @click="isChildrenShow = !isChildrenShow">
                <ArrowDown v-show="isChildrenShow" />
                <ArrowUp v-show="!isChildrenShow" />
            </el-icon>
        </div>
        <div class="children" v-show="isChildrenShow">
            <div class="offset" />
            <div class="list">
                <NoteBookSideNode :key="i" v-for="i in data.children.length" :data="data.children[i - 1]"
                    @chosen="(keys) => { onChildrenChoosen(keys, i - 1) }" />
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, defineProps, defineEmits } from 'vue'

// props
const props = defineProps(['data'])

//emits
const emit = defineEmits(['chosen'])

//data
const isChildrenShow = ref(true)

//method
const onChildrenChoosen = (keys, i) => {
    keys.unshift(i)
    emit('chosen', keys)
}


</script>

<style>
.notebook-side-node {
    width: 100%;
}

.notebook-side-node .list {
    width: 100%;
}

.notebook-side-node .self {
    height: 1.5rem;
    display: flex;
    align-items: center;
}

.notebook-side-node .self .title {
    width: 100%;
}

.notebook-side-node .self .title:hover {
    color: rgba(1, 1, 1, 0.5);
    cursor: pointer;
}

.notebook-side-node .self .empty {
    color: rgba(1, 1, 1, 0.3);
}

.notebook-side-node .self .chosen {
    color: rgb(100, 140, 240);
}

.notebook-side-node .children {
    display: flex;
}

.notebook-side-node .offset {
    width: 30px;
    border-right: 1px solid rgba(1, 1, 1, 0.5);
}

.notebook-side-node .list {
    margin-left: 5px;
}

/* .notebook-side-node .self .el-icon{
    margin-left: auto;
} */

.notebook-side-node .self .el-icon:hover {
    color: rgba(1, 1, 1, 0.5);
    cursor: pointer;
}
</style>