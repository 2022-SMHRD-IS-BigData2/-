<template>
  <div id="wrap-box">
    <h3 style="text-align: center;">환자 V/S 추가</h3>
    <table>
      <tr>
        <td>이름</td>
        <td>{{ patients.name }}</td>
      </tr>
      <tr>
        <td>생년월일</td>
        <td>{{ patients.birth_date  }}</td>
      </tr>
      <tr>
        <td>입력 시간</td>
        <td>{{ clickTime }}</td>
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
import moment from 'moment';

export default {
  components: {},
  data () {
    return {
      clickTime: moment().format('YYYY-MM-DDTHH:mm:ss'),
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
@import "../../assets/AddVital.css";
</style>
