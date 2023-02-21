<template>
  <div id="header">
    <div id="backward">
      <button id="back" @click="goBack"><i class="fa-solid fa-arrow-left fa-2x"></i></button>
    </div>
        <div id="nav">
          <router-link to="/detected">Detected</router-link>
          <router-link to="/">All patients</router-link>
          <div id="line"></div>
        </div>
            <div id="wrap-time">
              <div id="search">
                <span id="search-glass"><i class="fa-solid fa-magnifying-glass"></i></span>
                <input type="search" id="searchbox" placeholder="환자 ID 혹은 이름 검색">
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
import moment from 'moment'

export default {
  data () {
    return {
      currentTime: ''
    }
  },
  methods: {
    goBack () {
      this.$router.go(-1)
    }
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
*{font-family: 'Nanum Gothic', sans-serif;}
#header{
  width: 100vw;
  height: 100px;
}
#backward{
  width: 70px;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  float: left;
}
#nav{
  width: 300px;
  height: 100%;
  float: left;
  display: flex;
  justify-content: center;
  align-items: center;
  -ms-user-select: none;
  -moz-user-select: -moz-none;
  -khtml-user-select: none;
  -webkit-user-select: none;
  user-select: none;
  font-weight: bold;
}
#nav a{
  display: block;
  width: 70%;
  padding: .75em 0;
  color: #333;
  text-decoration: none;
  text-align: center;
}
#back:link{
  text-decoration: none;
  color: #333;
}
#back:hover{
  text-decoration: none;
  color: none;
}
#back:visited{
  text-decoration: none;
  color: #333;
}
#back:active{
  text-decoration: none;
  color: #333;
}
#back{
  border: 0;
  background-color: transparent;
  cursor: pointer;
}
#nav a:hover{
  text-decoration: underline;
  text-decoration-color: #74b9ff;
  text-underline-position: under;
  text-decoration-thickness: 5px;
}
#nav a.router-link-exact-active{
  text-decoration: underline;
  text-decoration-color: #74b9ff;
  text-underline-position: under;
  text-decoration-thickness: 5px;
}
#searchbox{
  border: 2px solid #333;
  border-radius: 10px;
  width: 200px;
  height: 30px;
  padding: 7px;
  margin-left: 5px;
}
#wrap-time{
  float: right;
  width: 500px;
  height: 100%;
}
#search{
float: left;
width: 50%;
height: 100%;
display: flex;
justify-content: center;
align-items: center;
}
#time{
  float: right;
  height: 100%;
  width: 50%;
  display: flex;
  justify-content: center;
  align-items: center;
  font-weight: bold;
  font-size: medium;
  color: #333;
}
</style>
