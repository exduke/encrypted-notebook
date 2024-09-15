<template>
    <el-container class="notebook">
        <el-side>
            <NoteBookSide :data="data" v-model:pswd="key" />
        </el-side>
        <el-main>
            <NoteBookMain v-model="notebookNodeChosen" />
        </el-main>

        <el-dialog v-model="isLoadDialogShow" :close-on-click-modal="false" :show-close="false"
            :close-on-press-escape="false" title="input encryption key">
            <el-input ref="input" v-model="key" @keyup.native.enter="onLoadDialogConfirmBtnClicked" />
            <template #footer>
                <el-button type="danger" @click="isLoadDialogShow = false">
                    New
                </el-button>
                <!-- <el-button @click="this.$router.replace('/file')"> -->
                <el-button @click="onLoadDialogLeaveBtnClicked">
                    Leave
                </el-button>
                <el-button type="primary" @click="onLoadDialogConfirmBtnClicked">
                    Confirm
                </el-button>
            </template>
        </el-dialog>
    </el-container>
</template>

<script>
import { hex_md5 } from '@/utils/md5';
import { ElMessage } from 'element-plus';
</script>

<script setup>
import { ref, reactive, computed, onMounted, nextTick } from 'vue'
import NoteBookSide from '@/components/NoteBookSide.vue';
import NoteBookMain from '@/components/NoteBookMain.vue';
import NoteBookObj from '@/types/NoteBook';

//data
const data = reactive(new NoteBookObj())
data.fromJsonObj(['notebook', 'u can use this encrypted notebook for sth like ur pswd or neth else...\n\nhowever it\'s not safe enough, for those really important, mutiple encrytion using FileManager woubld be a better choice', []])
const key = ref('')
const isLoadDialogShow = ref(false)

//components
const input = ref(null)

//onMounted
onMounted(() => {
    isLoadDialogShow.value = true

    nextTick(() => {
        input.value.focus()
    })
})

//computed
const notebookNodeChosen = computed(() => {
    return data.find(data.chosenNodeKeys)
})

//method
const onLoadDialogConfirmBtnClicked = async () => {

    let res = await fetch('/load?key=' + hex_md5(key.value), {
        method: 'GET',
    })

    if (res.ok) {
        try {
            data.fromJsonObj(JSON.parse(await res.text()))
            isLoadDialogShow.value = false
        }
        catch (e) {
            ElMessage.error('failed')
        }
    }
    else{
        ElMessage.error('failed')
    }


}
const onLoadDialogLeaveBtnClicked = () => {
    window.router.replace('/file')
}
</script>

<style>
.notebook {
    height: 100%;
    width: 100%;
}

.notebook .el-dialog {
    width: 500px;
}

.notebook .el-main {
    display: flex;
    justify-content: center;
}
</style>