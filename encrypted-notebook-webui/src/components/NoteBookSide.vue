<template>
    <div class="notebook-side">
        <div class="controller">
            <el-button @click="onAddBtnClicked">add</el-button>
            <el-button @click="onDelBtnClicked" :disabled="!data.chosenNodeKeys.length">del</el-button>
            <el-button @click="isSaveDialogShow = true">save</el-button>
        </div>
        
        <el-scrollbar>
            <NoteBookSideNode :data="data.root" @chosen="onNoteBookSideNodeChosen" />
        </el-scrollbar>

        <el-dialog :show-close="false" title="input encryption key"
            v-model="isSaveDialogShow">
            <el-input v-model="key" />
            <template #footer>
                <el-button @click="isSaveDialogShow = false">
                    Cancel
                </el-button>
                <el-button type="primary" @click="onSaveDialogConfirmBtnClicked">
                    Confirm
                </el-button>
            </template>
        </el-dialog>
    </div>
</template>

<script>
import { hex_md5 } from '@/utils/md5';
</script>

<script setup>
import { ref, defineProps, defineModel } from 'vue'
import NoteBookSideNode from '@/components/NoteBookSideNode.vue';
import { ElMessage } from 'element-plus';

//props
const props = defineProps(['data'])

//data
const isSaveDialogShow = ref(false)

//model
const key = defineModel('pswd')

//method
const onNoteBookSideNodeChosen = (keys) => {
    props.data.choose(keys)
}
const onAddBtnClicked = () => {
    props.data.add()
}
const onDelBtnClicked = () => {
    props.data.remove()
}
const onSaveDialogConfirmBtnClicked = async () => {
    isSaveDialogShow.value = false

    let res = await fetch('/save?key=' + hex_md5(key.value), {
        method: 'POST',
        body: JSON.stringify(props.data.toJsonObj()),
    })
    if (res.ok) {
        ElMessage.success('succeed')
    }
    else {
        ElMessage.error('failed')
    }
}

</script>

<style>
.notebook-side {
    background-color: white;
    border-right: 1px solid rgba(1, 1, 1, 0.1);
    height: 100%;
    /* min-width: 200px; */
    width: fit-content;
    display: flex;
    flex-direction: column;
}

.notebook-side .controller {
    padding: 10px;
    border-bottom: 1px solid rgba(1, 1, 1, 0.1);
}

.notebook-side .el-scrollbar {
    padding: 10px;
}

.notebook-side .controller .el-button {
    width: 50px;
}

.notebook-side .el-dialog {
    width: 500px;
}
</style>