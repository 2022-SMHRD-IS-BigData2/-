<template>
  <div id="wrap-box">
    <h3 style="text-align: center;">환자 V/S 수정</h3>
    <form @submit.prevent="updateRecord">
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
      <td><input type="text" v-model="hr" :style="hr ? 'border-color: green;' : ''" @input="preventInvalidInput($event, 'hr')"></td>
        </tr>
        <tr>
      <td>O2Sat</td>
      <td><input type="text" v-model="O2Sat" :style="hr ? 'border-color: green;' : ''" @input="preventInvalidInput($event, 'O2Sat')"></td>
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
    <input type="hidden" v-model="patients.p_record_seq">
    <button type="submit" class="btn">저장</button>
    <button class="btn" @click="closeWindow">취소</button>
    <button class="btn">삭제</button>
  </form>
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
      resp: null,
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
        this.O2Sat = this.patients.O2Sat;  // `hr` 프로퍼티 추가
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
      // Vue.js 인스턴스 내부에 preventInvalidInput 메소드 추가
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
  async updateRecord() {
      console.log(this.patients.p_record_seq);
      console.log(this.patients.pid);
      const record_u = {
        pid: parseInt(this.patients.pid),
        p_record_seq: parseInt(this.patients.p_record_seq),
        hr: parseInt(this.hr),
        O2Sat: parseInt(this.O2Sat),
        temp: parseFloat(this.temp),
        resp: parseInt(this.resp),
        sbp: parseInt(this.sbp),
        dbp: parseInt(this.dbp)
      };
    try {
      // API 호출
      const response = await axios.post(`http://127.0.0.1:8002/api/update_record/${this.patients.pid}`,record_u);
      await axios.get(`http://127.0.0.1:8002/api/predict_sepsis/${record_u.pid}`);
      // 응답 데이터 확인
      console.log(response.data);
      alert('업데이트 성공')
      // 창 닫기
      window.close();
    }
    catch (error) {
      console.error(error);
      alert('업데이트 실패')
    }
  },
  },
}
</script>
<style>
@import "../../assets/EditVital.css";
</style>
