<template>
  <div>
    <div>
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
export default {
  components: {},
  data() {
    return {
      sampleData: ''
    }
  },
  setup() {},
  created() {},
  mounted() {},
  unmounted() {},
  methods:{}
}
</script>