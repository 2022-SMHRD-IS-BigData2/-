<template>
  <div id="wrap-box">
    <h3 style="text-align: center;">새 환자 추가</h3>
    <table>
      <tr>
        <td>이름</td>
        <td><input type="text" class="inputcss"></td>
      </tr>
      <tr>
        <td>생년월일</td>
        <td><input type="date" class="inputcss"></td>
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
        <td><input type="number" class="inputcss"></td>
      </tr>
      <tr>
        <td>O2Sat</td>
        <td><input type="number" class="inputcss"></td>
      </tr>
      <tr>
        <td>Temp</td>
        <td><input type="number" class="inputcss"></td>
      </tr>
      <tr>
        <td>Resp</td>
        <td><input type="number" class="inputcss"></td>
      </tr>
      <tr>
        <td>SBP</td>
        <td><input type="number" class="inputcss"></td>
      </tr>
      <tr>
        <td>DBP</td>
        <td><input type="number" class="inputcss"></td>
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
@import "../../assets/AddPatient.css";
</style>
