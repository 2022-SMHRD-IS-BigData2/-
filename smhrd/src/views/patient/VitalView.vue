<template>
  <div id="wrap">
    <div id="wrap2">
      <div id="headtable">
        <table border="1" id="patient">
          <thead>
            <tr>
              <td style="font-weight: bold; background-color: #DFF2F5;">PID</td>
              <td>00</td>
              <td style="font-weight: bold; background-color: #DFF2F5;">Name</td>
              <td >00</td>
              <td style="font-weight: bold; background-color: #DFF2F5;">Age</td>
              <td>00</td>
              <td style="font-weight: bold; background-color: #DFF2F5;">Sex</td>
              <td>00</td>
            </tr>
          </thead>
        </table>
      </div>
      <div id="right">
        <button @click="AddVital" id="addmore">정보추가</button>
        <input type="date" id="src-date">
        <button id="submit">확인</button>
      </div>
    </div>
    <div id="body">
      <div id="leftarrow"><i class="fa-solid fa-left-long fa-3x"></i></div>
      <div id="tablewrap">
      <table border="1" id="realtable">
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
      <div id="rightarrow"><i class="fa-solid fa-right-long fa-3x"></i></div>
    </div>
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

    }
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
  created () {},
  mounted() {
    axios.get('http://127.0.0.1:8002/api/record/'+ this.$route.params.pid) //안되면 p_id 로 해보세요
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
  },
  unmounted () {},
  methods: {}
}
</script>

<style scoped>
*{font-family: 'Do Hyeon', sans-serif;}
#wrap{
  width: 100%;
  height: 100%;
}
#wrap2{
  width: 100%;
  height: 25%;
}
#patient{
  border: 2px solid #333;
  width: 80%;
  border-collapse : collapse;
  border-left: 2px solid #333;
  margin-top: 30px;
  margin-left: auto;
  margin-right: auto;
  margin-bottom: 10px;
  text-align: center;
  height: 10%;
}
#patient thead tr td{
  width: 12.5%;
}
table thead{
  border: 2px solid #333;
}
#right{
  height: 15%;
  width: 100%;
  text-align: right;
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
  border: 2px solid #333;
  width: 100%;
  border-collapse : collapse;
  margin-top: 30px;
  text-align: center;
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
