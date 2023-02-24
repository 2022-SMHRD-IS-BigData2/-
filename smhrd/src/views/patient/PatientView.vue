<template>
  <div id="wrap">
    <div id="table">
      <table border="1" id="fulltable">
          <tr>
<<<<<<< HEAD
            <td><li v-for="patient in patients" :key="patient.pid">{{ patient.p_name }}</li></td>
            <td>{{ diff }} / {{  patients.sex }}</td>
            <td>{{ patients.p_id }}</td>
            <td>{{ patients.birthdate }}</td>
=======
            <td style="font-weight: bold;">이름</td>
            <td>{{ patients.p_name }}</td>
            <td style="font-weight: bold;">HR</td>
            <td>00</td>
>>>>>>> ad775c7fbeda70dc9d4a45733cbd921571ecadd3
          </tr>
          <tr>
            <td style="font-weight: bold;">나이</td>
            <td>{{ diff }}</td>
            <td style="font-weight: bold;">Temp</td>
            <td>00</td>
          </tr>
          <tr>
            <td style="font-weight: bold;">성별</td>
            <td>{{  patients.sex }}</td>
            <td style="font-weight: bold;">Resp</td>
            <td>00</td>
          </tr>
          <tr>
            <td style="font-weight: bold;">환자번호</td>
            <td>{{ patients.p_id }}</td>
            <td style="font-weight: bold;">SBP</td>
            <td>00</td>
          </tr>
          <tr>
            <td style="font-weight: bold;">주민번호</td>
            <td>{{ patients.birthdate }}</td>
            <td style="font-weight: bold;">DBP</td>
            <td>00</td>
          </tr>
      </table>
    </div>
    <div id="under">
      <div id="score">현재 패혈증 점수</div>
      <div id="graph">패혈증 그래프</div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import moment from 'moment'

export default {
  data() {
    return {
      patients: [],
      dbDate: null,
      age: null
    };
  },
  computed: {
    gender() {
      return this.patients.sex === 1 ? 'F' : 'M'
    },
    age() {
      if (!this.dbDate) return null;
      const now = moment();
      const diff = now.diff(this.dbDate, 'years')
      return diff
    }
  },
  mounted() {
    axios.get('http://127.0.0.1:8002/api/patients')
      .then(response =>{
        return response.data
      })
      .then(data => {
        console.log(data)
        this.patients=data;
        return data
      })
      .then(response => {
        // this.dbDate = moment(response.birth_date, 'YYYY-MM-DD')
      })
      .catch(error => {
        console.log(error)
      })
  }
}
</script>

<style scoped>
*{font-family: 'Nanum Gothic', sans-serif;}
#fulltable{
  width: 80%;
  height: 100%;
  border-collapse : collapse;
  margin: 0;
  text-align: center;
  margin-top: 30px;
  margin-left: auto;
  margin-right: auto;
  font-size: large;
}
#fulltable tr td{
  width: 25%;
}
#fulltable thead{
  text-align: center;
}
#comment{
  width: 95%;
  height: 100%;
  resize: none;
  border: none;
  padding: 20px;
  margin: 10px;
}
thead tr{
  height: 50px;
}
 #wrap {
  width: 100%;
  height: 100vh;
}
#table{
  width: 100%;
  height: 30%;
}
#under{
  width: 100%;
  height: 40%;
  margin-top: 20px;
}
#score{
  float: left;
  width: 25%;
  height: 100%;
  border: 1px solid black;
  margin-left: 50px;
}
#graph{
  float: right;
  width: 65%;
  height: 100%;
  border: 1px solid black;
  margin-right: 50px;
}
#smalltable{
  width: 50%;
  height: 100%;
  text-align: center;
}
</style>
<!-- this.patients = response.data.patients -->

<!--
export default {
  components: {},
  data () {
    return {
      sampleData: ''
    }
  },
  setup () {},
  created () {},
  mounted () {},
  unmounted () {},
  methods: {}
} -->
