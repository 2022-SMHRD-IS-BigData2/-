<template>
  <div id="wrap-box">
    <h3 style="text-align: center;">환자 V/S 추가</h3>
    <table border="1">
      <tr>
        <td>이름</td>
        <td>자동입력</td>
      </tr>
      <tr>
        <td>생년월일</td>
        <td>자동입력</td>
      </tr>
      <tr>
        <td>입력 시간</td>
        <td>자동입력</td>
      </tr>
      <tr>
        <td>HR</td>
        <td><input type="number"></td>
      </tr>
      <tr>
        <td>Temp</td>
        <td><input type="number"></td>
      </tr>
      <tr>
        <td>Resp</td>
        <td><input type="number"></td>
      </tr>
      <tr>
        <td>SBP</td>
        <td><input type="number"></td>
      </tr>
      <tr>
        <td>DBP</td>
        <td><input type="number"></td>
      </tr>
    </table>
    <button type="submit" class="btn">저장</button>
    <button class="btn" @click="closeWindow">취소</button>
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
  methods: {
    closeWindow() {
        window.close();
  }
  }
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
  height: 60%;
}
table tr td{
  height: 40px;
  font-weight: bold;
}
.btn{
  padding: 3px 7px 3px 7px;
  margin: 20px 20px 10px 20px;
  font-weight: bold;
  border: none;
  background-color: #ced6e0;
  box-shadow: 1px 1px 2px;
  border-radius: 5px;
  cursor: pointer;
}
#wrap-box{
  text-align: center;
}
input{
  border: 0;
}
input:focus{
  outline: none;
}
</style>
