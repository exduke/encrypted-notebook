<template>
    <div class="file-manager">

        <el-input v-model="key" placeholder="encrypt/decrypt key here" />

        <el-upload drag :before-upload="onEncryptBeforeUpload">
            <el-icon class="el-icon--upload">
                <upload-filled />
            </el-icon>
            <div class="el-upload__text">
                <p>encrypt</p>
                Drop file here or <em>click to upload</em>
            </div>
        </el-upload>

        <el-upload drag :before-upload="onDecryptBeforeUpload">
            <el-icon class="el-icon--upload">
                <upload-filled />
            </el-icon>
            <div class="el-upload__text">
                <p>decrypt</p>
                Drop file here or <em>click to upload</em>
            </div>
        </el-upload>

    </div>
</template>

<script>
import { hex_md5 } from '@/utils/md5.js';
import download from '@/utils/download.js'
import { ElMessage } from 'element-plus';
</script>

<script setup>
import { ref } from 'vue'

//data
const key = ref('')

// method
const onEncryptBeforeUpload = (file) => {
    let fileReader = new FileReader()
    fileReader.onloadend = async () => {

        let res = await fetch('/encrypt?key=' + hex_md5(key.value), {
            method: 'POST',
            body: fileReader.result,
        })
        if (res.ok) {
            download(await res.blob(), file.name + '.lck')
        }
        else {
            ElMessage.error('failed')
        }
    }
    // fileReader.readAsBinaryString(file)
    fileReader.readAsArrayBuffer(file)
    return false
}

const onDecryptBeforeUpload = (file) => {
    let fileReader = new FileReader()
    fileReader.onloadend = async () => {
        let res = await fetch('/decrypt?key=' + hex_md5(key.value), {
            method: 'POST',
            body: fileReader.result,
        })
        if (res.ok) {
            download(await res.blob(), file.name.replace('.lck', ''))
        }
        else {
            ElMessage.error('failed')
        }
    }
    // fileReader.readAsBinaryString(file)
    fileReader.readAsArrayBuffer(file)
    return false
}

</script>

<style>
.file-manager {
    width: 80%;
}

.file-manager>* {
    margin-top: 50px;
}
</style>