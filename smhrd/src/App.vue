<template>
  <div id="header">
    <div id="backward">
      <button id="back" @click="goBack"><i class="fa-solid fa-arrow-left fa-2x"></i></button>
    </div>
        <div id="nav">
          <router-link to="/detected" id="detected">Detected</router-link>
          <router-link to="/" id="all">All patients</router-link>
          <div id="line"></div>
        </div>
            <div id="wrap-time">
              <div id="search">
                <span id="search-glass"><i class="fa-solid fa-magnifying-glass"></i></span>
                <input type="search" id="searchbox" placeholder="환자 ID or 이름 검색" v-model="searchQuery" @input="onSearch">
                <button type="button" @click="onSearch" id="src-btn">검색</button>
              </div>
              <div id="time">
                {{ currentTime }}
              </div>
          </div>
  </div>
  <hr>
<router-view/>
</template>

<script>
import { thisTypeAnnotation } from '@babel/types'
import moment from 'moment';
import axios from 'axios';

export default {
  data () {
    return {
      currentTime: '',
      searchQuery: '',
    }
  },
  created(){
    this.url = this.$route.path;
  },
  methods: {
    goBack() {
      this.$router.go(-1);
    },
    onSearch() {
      // store에 searchQuery 저장
      this.$store.dispatch('setSearchQuery', this.searchQuery);
  },
  },
  mounted () {
    this.moment = moment // moment 함수를 this에 할당합니다.

    this.timer = setInterval(() => {
      this.currentTime = this.moment().format('YYYY년 MM월 DD일 HH:mm:ss')
    }, 1000)
  },
  beforeUnmount () {
    clearInterval(this.timer)
  }
}

</script>

<style scoped>
@import "./assets/App.css";
</style>