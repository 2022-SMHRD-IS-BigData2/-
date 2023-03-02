<template>
  <div id="wrap-box">
    <h3 style="text-align: center;">환자 V/S 수정</h3>
    <table>
      <tr>
        <td>이름</td>
        <td>{{ patients.name }}</td>
      </tr>
      <tr>
        <td>생년월일</td>
        <td>{{ patients.birth_date }}</td>
      </tr>
      <tr>
        <td>입력 시간</td>
        <td>{{ this.$route.params.input }}</td>
      </tr>
      <tr>
        <td>HR</td>
        <td><input type="number"></td>
      </tr>
      <tr>
        <td>Temp</td>
        <td><input type="number"></td>
      </tr>
      <tr>
        <td>Resp</td>
        <td><input type="number"></td>
      </tr>
      <tr>
        <td>SBP</td>
        <td><input type="number"></td>
      </tr>
      <tr>
        <td>DBP</td>
        <td><input type="number"></td>
      </tr>
    </table>
    <button type="submit" class="btn">저장</button>
    <button class="btn" @click="closeWindow">취소</button>
  </div>
</template>
<script>
import { useRouter } from 'vue-router'
import axios from 'axios'

export default {
  components: {},
  data () {
    return {
      patients: []
    }
  },
  setup () {},
  created () {},
  mounted () {
    axios.get("http://127.0.0.1:8002/api/get_latest_all/" + this.$route.params.pid)
    .then(response =>{
        return response.data
      })
      .then(data => {
        console.log(data[0])
        this.patients=data[0];
        return data
      })
      .then(response => {
        // this.dbDate = moment(response.birth_date, 'YYYY-MM-DD')
      })
      .catch(error => {
        console.log(error)
      })

  },
  unmounted () {},
  methods: {
    closeWindow() {
        window.close();
  }
  }
}
</script>
<style>
*{font-family: 'Noto Sans KR', sans-serif;}
#header{
  display: none;
}
hr{
  display: none;
}
table{
  border-collapse: collapse;
  width: 100%;
  text-align: center;
  height: 60%;
  padding: 30px;
}
table tr td{
  height: 40px;
  font-weight: bold;
  border-bottom: 1px solid #ced6e0;
}
.btn{
  padding: 3px 7px 3px 7px;
  margin: 20px 20px 10px 20px;
  font-weight: bold;
  border: none;
  background-color: #ced6e0;
  box-shadow: 1px 1px 2px;
  border-radius: 5px;
  cursor: pointer;
}
.btn:active{
  box-shadow: none;
}
#wrap-box{
  text-align: center;
}
input{
  border: 0;
}
input:focus{
  outline: none;
}
</style>
