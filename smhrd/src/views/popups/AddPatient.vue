<template>
  <div id="wrap-box">
    <h3 style="text-align: center;">새 환자 추가</h3>
    <table border="1">
      <tr>
        <td>이름</td>
        <td><input type="text"></td>
      </tr>
      <tr>
        <td>생년월일</td>
        <td><input type="date"></td>
      </tr>
      <tr>
        <td>성별</td>
        <td>
          <input type="radio" name="Sex" value="M">M
          <input type="radio" name="Sex" value="F">F
        </td>
      </tr>
      <tr>
        <td>HR</td>
        <td><input type="text"></td>
      </tr>
      <tr>
        <td>Temp</td>
        <td><input type="text"></td>
      </tr>
      <tr>
        <td>Resp</td>
        <td><input type="text"></td>
      </tr>
      <tr>
        <td>SBP</td>
        <td><input type="text"></td>
      </tr>
      <tr>
        <td>DBP</td>
        <td><input type="text"></td>
      </tr>
    </table>
  </div>
</template>
<script>
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
}
</script>
<style>
*{font-family: 'Nanum Gothic', sans-serif;}
#header{
  display: none;
}
hr{
  display: none;
}
table{
  border: 3px solid #333;
  border-collapse: collapse;
  width: 100%;
  text-align: center;
  height: 100%;
}
table tr td{
  height: 50px;
  font-weight: bold;
}
</style>
