import { createMemoryHistory, createRouter } from 'vue-router'

import FileManager from '@/components/FileManager.vue';
import NoteBook from '@/components/NoteBook.vue';

const routes = [
  { path: '/', component: NoteBook },
  { path: '/file', component: FileManager },
]

const router = createRouter({
  history: createMemoryHistory(),
  routes,
})

export default router;