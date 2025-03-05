<template>
  <div>
    <div v-if="!animePage">
      <h1>Concrec 动漫推荐系统</h1>
      <h3>猜你喜欢:</h3>
      <button @click="loadItems" type="button" class="btn btn-info">刷新</button>
    </div>

    <div v-else>
      <Anime
        :id="currentAnime.anime_id"
        :japanese_title="currentAnime.japanese_title"
        :title="currentAnime.name"
        :img_url="currentAnime.image_url"
        :genres="currentAnime.genre"
        :aired="currentAnime.aired"
        :rating="currentAnime.rating"
        :members="currentAnime.members"
      />
      <br />
      <h3>相似推荐:</h3>
    </div>

    <div class="container cell-grid">
      <div v-for="(group, gIndex) in itemsGroup" :key="gIndex" class="row">
        <div v-for="(item, iIndex) in group" :key="iIndex" class="col">
          <Cell
            :id="item.anime_id"
            :japanese_title="item.japanese_title"
            :title="item.name"
            :img_url="item.image_url"
            :genres="item.genre"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import Cell from './components/cell.vue'
import Anime from './components/anime.vue'
import axios from 'axios'
import _ from 'lodash'

const items = ref([])
const currentAnime = ref({})

const animePage = computed(() => window.location.pathname === '/anime')

// Use lodash to chunk items into groups of 4
const itemsGroup = computed(() => _.chunk(items.value, 4))

async function loadItems () {
  const userId = getUserId()
  const animeId = getAnimeId()
  let url = 'http://localhost:5001/'
  if (!animePage.value) {
    url += `?user_id=${userId}`
  } else {
    url += `sim?anime_id=${animeId}`
  }
  const res = await axios.get(url)
  items.value = res.data
}

async function loadCurrentAnime () {
  const animeId = getAnimeId()
  const url = `http://localhost:5001/anime/${animeId}`
  const res = await axios.get(url)
  currentAnime.value = res.data
}

function getUserId () {
  return new URLSearchParams(window.location.search).get('user_id')
}

function getAnimeId () {
  return new URLSearchParams(window.location.search).get('anime_id')
}

// Lifecycle: Instead of created(), use onMounted()
onMounted(async () => {
  if (animePage.value) {
    await loadCurrentAnime()
  }
  await loadItems()
})
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

.cell-grid {
  margin-top: 50px;
  margin-bottom: 50px;
}
</style>