<template>
  <div id="wrap">

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
*{font-family: 'Noto Sans KR', sans-serif;}
#wrap{
  width: 100%;
  height: 100%;
}
#patient{
  width: 80%;
  border-collapse : collapse;
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
