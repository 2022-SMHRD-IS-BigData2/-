<template>
  <div id="wrap-box">
    <h3 style="text-align: center;">환자 V/S 추가</h3>
    <form @submit.prevent="insertRecord">
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
      <td><input type="text" v-model="hr" :style="hr ? 'border-color: green;' : ''" @input="preventInvalidInput($event, 'hr')"></td>
        </tr>
        <tr>
        <td>O2Sat</td>
      <td><input type="text" v-model="O2Sat" :style="O2Sat ? 'border-color: green;' : ''" @input="preventInvalidInput($event, 'O2Sat')"></td>
        </tr>
        <tr>
          <td>Temp</td>
          <td><input type="text" v-model="temp" :style="temp ? 'border-color: green;' : ''" @input="preventInvalidInput($event, 'temp')"></td>
        </tr>
        <tr>
          <td>Resp</td>
          <td><input type="text" v-model="resp" :style="resp ? 'border-color: green;' : ''" @input="preventInvalidInput($event, 'resp')"></td>
        </tr>
        <tr>
          <td>SBP</td>
          <td><input type="text" v-model="sbp" :style="sbp ? 'border-color: green;' : ''" @input="preventInvalidInput($event, 'sbp')"></td>
        </tr>
        <tr>
          <td>DBP</td>
          <td><input type="text" v-model="dbp" :style="dbp ? 'border-color: green;' : ''" @input="preventInvalidInput($event, 'dbp')"></td>
        </tr>
    </table>
    <input type="hidden" v-model="patients.pid">
    <input type="hidden" v-model="patients.birth_date">
    <input type="hidden" v-model="patients.sex">

    <button type="submit" class="btn">저장</button>
    <button class="btn" @click="closeWindow">취소</button>
  </form>
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
    },
    async preventInvalidInput(event, field) {
  const inputVal = event.target.value;
  const valid = /^[\d.]*$/.test(inputVal); // 입력값이 숫자와 소수점으로만 이루어졌는지 확인

  if (valid) {
    // 유효한 값이 입력된 경우, 입력값을 Vue.js 인스턴스의 데이터에 반영
    this[field] = inputVal;
    event.target.style.borderColor = 'green';
  } else {
    // 유효하지 않은 값이 입력된 경우, 이전에 입력된 유효한 값을 사용하여 입력값을 대체
    event.target.value = this[field] || '';
    event.target.style.borderColor = 'red';
  }

  if (inputVal === '' && this[field] !== '') {
    this[field] = '';
    event.target.style.borderColor = 'green';
  }
  if (inputVal === '') {
  event.target.style.borderColor = 'red';
  return;
}
},
  async insertRecord() {

// 서버로 보낼 데이터 객체 생성
  const record_i = {
      pid : this.patients.pid,
      input_time: this.clickTime,
      birth_date: this.patients.birth_date,
      sex: this.patients.sex,
      hr: this.hr,
      O2Sat: this.O2Sat,
      temp: this.temp,
      resp: this.resp,
      sbp: this.sbp,
      dbp: this.dbp,
      sepsis_in_six: 0,
      sepsis_percent: 0
    };
    try {
    console.log(record_i);
    // API 호출
    const response = await axios.post(`http://127.0.0.1:8002/api/insert_fast_record/${record_i.pid}`,record_i);
    // 응답 데이터 확인
    console.log(response.data);
    // 창 닫기
    alert("입력 성공");    
    window.close();
  } 
  catch (error) {
    alert("입력값을 확인해주세요.")
    console.error(error);
  }
},

  }
}
</script>
<style>
@import "../../assets/AddVital.css";
</style>
