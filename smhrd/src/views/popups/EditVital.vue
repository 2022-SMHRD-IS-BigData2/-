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
        <td><input type="number" v-model="hr"></td>
      </tr>
      <tr>
        <td>Temp</td>
        <td><input type="number" v-model="temp"></td>
      </tr>
      <tr>
        <td>Resp</td>
        <td><input type="number" v-model="resp"></td>
      </tr>
      <tr>
        <td>SBP</td>
        <td><input type="number" v-model="sbp"></td>
      </tr>
      <tr>
        <td>DBP</td>
        <td><input type="number" v-model="dbp"></td>
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
      patients: [],
      modifiedInput: '',
      hr: null,
      temp: null,
      sbp: null,
      dbp: null,
      resp: null
    }
  },
  setup () {},
  created () {
    let input = this.$route.params.input;
    this.modifiedInput = input.replace(/:/g, "%3A");
  },
  mounted () {
    axios.get("http://127.0.0.1:8002/api/get_select_record/" + this.$route.params.pid + "?input_time=" + this.modifiedInput )

    .then(response =>{
        return response.data
      })
      .then(data => {
        console.log(data['data'])
        this.patients=data['data'];
        this.hr = this.patients.hr;  // `hr` 프로퍼티 추가
        this.temp = this.patients.temp;  // `temp` 프로퍼티 추가
        this.sbp = this.patients.sbp;  // `sbp` 프로퍼티 추가
        this.dbp = this.patients.dbp;  // `dbp` 프로퍼티 추가
        this.resp = this.patients.resp;  // `resp` 프로퍼티 추가
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
@import "../../assets/EditVital.css";
</style>
