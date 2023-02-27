<template>
  <div id="wrap">
    <div id="wrap2">
      <div id="headtable">
        <table border="1" id="patient">
          <thead>
            <tr>
              <td>PID</td>
              <td>{{ patients }}</td>
              <td>Name</td>
              <td>00</td>
              <td>Age</td>
              <td>00</td>
              <td>Sex</td>
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
      <div id="leftarrow"><i class="fa-solid fa-left-long"></i></div>
      <div id="tablewrap">
      <table border="1" id="realtable">
        <thead>
          <tr>
            <td style="width: 25%;">Time</td>
            <td style="width: 15%;">HR</td>
            <td style="width: 15%;">Temp</td>
            <td style="width: 15%;">Resp</td>
            <td style="width: 15%;">SBP</td>
            <td style="width: 15%;">DBP</td>
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
      <div id="rightarrow"><i class="fa-solid fa-right-long"></i></div>
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
      sampleData: '',
      
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
*{font-family: 'Nanum Gothic', sans-serif;}
#wrap{
  width: 100%;
  height: 100%;
}
#wrap2{
  width: 100%;
  height: 25%;
}
#patient{
  border: 3px solid #333;
  width: 80%;
  border-collapse : collapse;
  border-left: 3px solid #333;
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
  border: 3px solid #333;
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
}
#realtable{
  margin-top: 50px;
  /* display: inline-block; */
  border: 3px solid #333;
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
