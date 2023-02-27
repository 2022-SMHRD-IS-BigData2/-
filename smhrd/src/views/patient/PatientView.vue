<template>
  <div id="wrap">
    <div id="table">
      <table border="1" id="fulltable">
          <tr>
            <td style="font-weight: bold;">이름</td>
            <td>{{ patients.p_name }}</td>
            <td style="font-weight: bold;">
              <router-link v-if="typeof patients.pid !== 'undefined'"
             v-bind:to="{ name: 'VitalView', params: { pid: patients.pid } }">
          HR
            </router-link></td>
            <td>{{ patients.hr }}</td>
          </tr>
          <tr>
            <td style="font-weight: bold;">나이</td>
            <td>{{ patients.p_age }}</td>
            <td style="font-weight: bold;"><router-link v-if="typeof patients.pid !== 'undefined'"
             v-bind:to="{ name: 'VitalView', params: { pid: patients.pid } }">
          Temp
            </router-link></td>
            <td>{{patients.temp}}</td>
          </tr>
          <tr>
            <td style="font-weight: bold;">성별</td>
            <td>{{ gender }}</td>
            <td style="font-weight: bold;"><router-link v-if="typeof patients.pid !== 'undefined'"
             v-bind:to="{ name: 'VitalView', params: { pid: patients.pid } }">
          Resp
            </router-link></td>
            <td>{{ patients.resp }}</td>
          </tr>
          <tr>
            <td style="font-weight: bold;">환자번호</td>
            <td>{{ patients.pid }}</td>
            <td style="font-weight: bold;"><router-link v-if="typeof patients.pid !== 'undefined'"
             v-bind:to="{ name: 'VitalView', params: { pid: patients.pid } }">
          SBP
            </router-link></td>
            <td>{{ patients.sbp }}</td>
          </tr>
          <tr>
            <td style="font-weight: bold;">생년월일</td>
            <td>{{ patients.birth_date }}</td>
            <td style="font-weight: bold;"><router-link v-if="typeof patients.pid !== 'undefined'"
             v-bind:to="{ name: 'VitalView', params: { pid: patients.pid } }">
          DBP
            </router-link></td>
            <td>{{ patients.dbp }}</td>
          </tr>
      </table>
    </div>
    <div id="under">
      <div id="score">
        <div id="real-score">90</div>
        <div id="scoreup">
          <i class="fa-solid fa-caret-up"></i>00
          <!-- <i class="fa-solid fa-caret-down"></i>00 -->
        </div>
      </div>
      <div id="graph">
        <Chart />
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import Chart from '../../components/Chart.vue'
import { useRouter } from 'vue-router'

export default {
  data() {
    return {
      patients: [],
      dbDate: null
    };
  },
  components: {
    Chart,
  },
  setup () {
    const router = useRouter()
  },
  computed: {
    gender() {
      return this.patients.sex === 1 ? 'F' : 'M'
    }
  },
  methods: {
    getPatientName() {
      const result = this.patients.filter( patient => patient.pid  === this.$route.params.pid );

  }
},
  mounted() {
    axios.get('http://127.0.0.1:8002/api/get_latest_all/'+ this.$route.params.pid) //안되면 p_id 로 해보세요
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
      }),
      this.getPatientName();
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
  border: 3px solid #333;
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
  border: 3px solid #333;
  margin-left: 50px;
  text-align: center;
  position: relative;
}
#real-score{
    display: inline-block;
    font-size: 100px;
    height: 50%;
    width: 100%;
    padding-top: 50px;
}
#scoreup{
    display: inline-block;
    font-size: 30px;
    height: 50%;
    width: 100%;

}
#graph{
  float: right;
  width: 65%;
  height: 100%;
  border: 3px solid #333;
  margin-right: 50px;
}
#smalltable{
  width: 50%;
  height: 100%;
  text-align: center;
}
canvas{
  margin: 0 auto;
  height: 100%;
  width: 100%;
}
a{
  text-decoration: none;
  color: black;
}
a:visited { text-decoration: none;
color: black; }
a:hover { text-decoration: none;
  color: black; }
a:focus { text-decoration: none;
  color: black; }
a:hover, a:active { text-decoration: none;
  color: black; }
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
