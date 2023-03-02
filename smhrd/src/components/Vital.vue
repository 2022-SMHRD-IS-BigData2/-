<template>
  <div>
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
            <td>RECENT</td>
            <td>{{ patients.hr }}</td>
            <td>{{ patients.temp }}</td>
            <td>{{ patients.resp }}</td>
            <td>{{ patients.sbp }}</td>
            <td>{{ patients.dbp }}</td>
          </tr>
          <tr v-for="(vs, index) in all" :key="index">
            <td>{{ vs.input_time}}</td>
            <td>{{ vs.hr }}</td>
            <td>{{ vs.temp }}</td>
            <td>{{ vs.resp }}</td>
            <td>{{ vs.sbp }}</td>
            <td>{{ vs.dbp}}</td>
          </tr>
        </tbody>
      </table>
  </div>
</template>
<script>
import axios from 'axios'
export default {
  name: "Vital",
  props: {
    patients: Object,
    dbDate: null,
    selectedDate: String,
    currentDate: String,
    loadpid: String
  },
  components: {},
  data() {
    return {
      all: []
    }
  },
  setup() {},
  created() {},
  watch: {
  currentDate(newVal, oldVal) {
    this.getDataFromServer();
  }
},
  mounted() {
    this.getDataFromServer();
  },
  unmounted() {},
  methods:{
    getDataFromServer() {
      axios.get("http://127.0.0.1:8002/api/get_select_date?pid=" + this.loadpid + "&date=" + this.currentDate)
    .then(data => {
        console.log(data['data'])
        this.all=data['data'];
        return data
      })
    }
  },
  computed: {
    tomorrow() {
      return moment(this.currentDate).add(1, "day").format("YYYY-MM-DD");
    },
    yesterday() {
      return moment(this.currentDate).subtract(1, "day").format("YYYY-MM-DD");
    }
  }
}
</script>
<style scoped>
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
  height: 50px;
}
</style>