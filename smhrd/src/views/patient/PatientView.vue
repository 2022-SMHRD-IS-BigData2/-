<template>
  <div>
    <div>
      <table border="1" id="fulltable">
        <thead>
          <tr>
            <td>이름</td>
            <td>나이/성별</td>
            <td>환자번호</td>
            <td>주민번호</td>
          </tr>
          <tr>
            <td>{{ patients.p_name }}</td>
            <td>{{ diff }} / {{  patients.sex }}</td>
            <td>{{ patients.p_id }}</td>
            <td>{{ patients.birthdate }}</td>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>
              <table border="0" id="smalltable">
                <tr>
                  <td>HR</td>
                  <td>00</td>
                </tr>
                <tr>
                  <td>Temp</td>
                  <td>00</td>
                </tr>
                <tr>
                  <td>Resp</td>
                  <td>00</td>
                </tr>
                <tr>
                  <td>SBP</td>
                  <td>00</td>
                </tr>
                <tr>
                  <td>DBP</td>
                  <td>00</td>
                </tr>
              </table>
            </td>
            <td colspan="3"><textarea id="comment" rows="10"></textarea></td>
          </tr>
        </tbody>
      </table>
    </div>
    <div>
      <div>현재 패혈증 점수</div>
      <div>패혈증 그래프</div>
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
    axios.get('http://127.0.0.1:8000/api/patients')
      .then(response =>{
        return response.data
      })
      .then(data => {
        console.log(data)
        this.patients=data
      })
      .then(response => {
        this.dbDate = moment(response.patients.birth_date, 'YYYY-MM-DD')
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
  width: 100%;
  height: 50%;
  border-collapse : collapse;
}
#fulltable thead{
  text-align: center;
}
#comment{
  width: 99%;
  height: 100%;
  resize: none;
  border: 2px solid #333;
}
thead tr{
  height: 50px;
}
#smalltable{
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
