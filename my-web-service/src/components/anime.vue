<template>
  <div class="container anime">
    <div class="row">
      <div class="col-4">
        <img :src="img_url" />
      </div>
      <div class="col">
        <table class="table table-striped table-borderless info-table">
          <tbody>
            <tr>
              <th>片名</th>
              <td>{{ japanese_title }}</td>
            </tr>
            <tr>
              <th>英文名</th>
              <td>{{ title }}</td>
            </tr>
            <tr>
              <th>上映时间</th>
              <td>{{ aired }}</td>
            </tr>
            <tr>
              <th>评分</th>
              <td>{{ rating }}</td>
            </tr>
            <tr>
              <th>会员人数</th>
              <td>{{ members }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script setup>
import { defineProps } from 'vue'

const props = defineProps({
  id: String,
  japanese_title: String,
  title: String,
  img_url: String,
  genres: String,
  aired: String,
  rating: String,
  members: String
})
</script>

<style>
.info-table {
  margin-top: 50px;
  width: 80%;
}
</style>