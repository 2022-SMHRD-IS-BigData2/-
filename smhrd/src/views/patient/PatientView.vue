<template>
  <div>
    <div>
      <button type="button" @click="getAllPatient">모든환자조회</button>
      <table>
        <thead>
          <tr>
            <td>이름</td>
            <td>나이 성별</td>
            <td>환자번호</td>
            <td>주민번호</td>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td colspan="2">vitalsign 최신/ 클릭시 이동</td>
            <td colspan="2">비고</td>
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
import axios from 'axios';

export default {
  data() {
    return {
      patients: [],
    };
  },
  mounted() {
    axios.get('http://172.30.1.25:8807/api/patients')
      .then(response =>console.log(response.data))
      .catch(error => {
        console.log(error);
      });
  }
}
</script>
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
