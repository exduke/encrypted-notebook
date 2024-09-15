<template>
  <el-container>
    <el-header>
      <RouterLink to="/">NoteBook</RouterLink>
      <RouterLink to="/file">FileManager</RouterLink>
    </el-header>
    <el-main>
      <RouterView />
    </el-main>
  </el-container>
</template>

<script setup>
import { RouterLink } from 'vue-router';
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /* text-align: center; */
  color: #2c3e50;
}

#app>.el-container {
  height: 100vh;
}

#app>.el-container>.el-header {
  border-bottom: 1px solid rgba(1, 1, 1, 0.1);
  display: flex;
  padding: 0;
}

#app>.el-container>.el-main {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin: 0;
  padding: 0;
  background-color: rgba(1, 1, 1, 0.01);
}

#app>.el-container>.el-header a {
  text-decoration: none;
  color: black;
  display: flex;
  height: 100%;
  min-width: 100px;
  align-items: center;
  justify-content: center;
  margin-left: 20px;
}

#app>.el-container>.el-header a:hover {
  color: rgba(1, 1, 1, 0.5);
}

#app>.el-container>.el-header .router-link-active {
  color: rgb(100, 140, 240);
}
</style>
