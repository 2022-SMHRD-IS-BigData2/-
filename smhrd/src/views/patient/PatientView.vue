<template>
  <div id="wrap">
    <div id="table">
      <div id="right">
        <button @click="AddVital" id="addmore">정보추가</button>
        <input type="date" id="src-date">
        <button id="submit">확인</button>
      </div>
      <div id="table-wrap">
      <table id="fulltable">
        <tr>
            <td style="font-weight: bold; background-color: #DFF2F5;">이름</td>
            <td>{{ patients.name }}</td>
        </tr>
        <tr>
            <td style="font-weight: bold; background-color: #DFF2F5;">나이</td>
            <td>{{ patients.age }}</td>
        </tr>
        <tr>
            <td style="font-weight: bold; background-color: #DFF2F5;">성별</td>
            <td>{{ gender }}</td>
        </tr>
        <tr>
            <td style="font-weight: bold; background-color: #DFF2F5;">환자번호</td>
            <td>{{ patients.pid }}</td>
        </tr>
        <tr>
            <td style="font-weight: bold; background-color: #DFF2F5;">생년월일</td>
            <td>{{ patients.birth_date }}</td>
        </tr>
      </table>
    </div>
      <div id="score" :style="{'background-color': bgColor}">
        <div id="real-score">{{ patients.sepsis_percent }}</div>
        <div id="scoreup">
          <i class="fa-solid fa-caret-up"></i>00
          <!-- <i class="fa-solid fa-caret-down"></i>00 -->
        </div>
      </div>
      <div id="graph">
        <Chart style="width: 700px; height: 250px;"/>
      </div>
  </div>
    <div id="under">

    <div id="body">
      <div id="leftarrow"><i class="fa-solid fa-left-long fa-3x" style="color: #ced6e0;"></i></div>
      <div id="tablewrap">
      <table id="realtable">
        <thead>
          <tr>
            <td style="width: 25%; font-weight: bold; background-color: #DFF2F5;">Time</td>
            <td style="width: 15%; font-weight: bold; background-color: #DFF2F5;">HR</td>
            <td style="width: 15%; font-weight: bold; background-color: #DFF2F5;">Temp</td>
            <td style="width: 15%; font-weight: bold; background-color: #DFF2F5;">Resp</td>
            <td style="width: 15%; font-weight: bold; background-color: #DFF2F5;">SBP</td>
            <td style="width: 15%; font-weight: bold; background-color: #DFF2F5;">DBP</td>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>00</td>
            <td>00</td>
            <td>00</td>
            <td>00</td>
            <td>00</td>
            <td>00</td>
          </tr>
        </tbody>
      </table>
    </div>
      <div id="rightarrow"><i class="fa-solid fa-right-long fa-3x" style="color: #ced6e0;"></i></div>
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
    const AddVital = () => {
      window.open(router.resolve({ name: 'AddVital' }).href, 'AddVital', 'width=500,height=500')
    }

    return {
      AddVital
    }
  },
  computed: {
    gender() {
      return this.patients.sex === 1 ? 'F' : 'M'
    },
    bgColor() {
      return this.patients.sepsis_percent >= 80 ? '#fab1a0' : '#85E9A7';
    }
  },
  methods: {
    getPatientName() {
      const result = this.patients.filter( patient => patient.pid  === this.$route.params.pid );

  }
},
  mounted() {
    axios.all([axios.get('http://127.0.0.1:8002/api/get_latest_all/'+ this.$route.params.pid)
    ,axios.get("http://127.0.0.1:8002/api/get_select_date?pid=" + this.$route.params.pid +"&input_time=" + this.route.params.pid)])
    .then(
      axios.spread((res1, res2) => {
        this.patients = res1.data[0];
        return data
      })
    )
      .then(response =>{
        return response.data
      })
      // .then(data => {
      //   console.log(data[0])
      //   this.patients=data[0];
      //   return data
      // })
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
*{font-family: 'Noto Sans KR', sans-serif;}
#fulltable{
  width: 100%;
  height: 100%;
  border-collapse : collapse;
  margin: 0;
  text-align: center;
}
#fulltable tr td{
  width: 50%;
  border-bottom: 1px solid #ced6e0;
}
#fulltable thead{
  text-align: center;
}
#table-wrap{
  width: 30%;
  height: 100%;
  display: inline-block;
  float: left;
  margin: 30px 20px 0px 20px;
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
  height: 25%;
}
#under{
  width: 100%;
  height: 40%;
}
#score{
  height: 100%;
  width: 20%;
  text-align: center;
  position: relative;
  float: left;
  margin: 30px 0px 0px 80px;
  border-radius: 15%;
}
#real-score{
    display: inline-block;
    height: 50%;
    width: 100%;
    font-size: 100px;
}
#scoreup{
    display: inline-block;
    height: 50%;
    width: 100%;
    font-size: 40px;
    padding-top: 20px;
}
#graph{
  float: right;
  width: 40%;
  height: 100%;
  margin-top: 30px;
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
  color: black;
cursor: pointer; }
a:focus { text-decoration: none;
  color: black; }
a:hover, a:active { text-decoration: none;
  color: black; }

  #right{
  height: 15%;
  width: 100%;
  text-align: right;
  padding-top: 20px;
}
#addmore{
  margin-right: 10px;
  padding: 5px 10px 5px 10px;
  border-radius: 5px;
  border: none;
  background-color: #ced6e0;
  font-weight: bold;
  cursor: pointer;
  box-shadow: 1px 1px 2px;
}
#addmore:active{
  box-shadow: none;
}
#src-date{
  padding: 5px 10px 5px 10px;
  border: 2px solid #ced6e0;
  border-radius: 5px;
}
#submit{
  margin-left: 10px;
  padding: 5px 10px 5px 10px;
  border-radius: 5px;
  border: none;
  background-color: #ced6e0;
  font-weight: bold;
  cursor: pointer;
  box-shadow: 1px 1px 2px;
}
#submit:active{
  box-shadow: none;
}
#realtable{
  margin-top: 50px;
  /* display: inline-block; */
  width: 100%;
  border-collapse : collapse;
  margin-top: 30px;
  text-align: center;
}
#realtable tr td{
  border-bottom: 1px solid #ced6e0;
}
#tablewrap{
  display: inline-block;
  width: 80%;
}
#body{
  width: 100%;
}
#leftarrow{
width: 10%;
display: inline-block;
text-align: center;
}
#rightarrow{
  width: 10%;
display: inline-block;
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
