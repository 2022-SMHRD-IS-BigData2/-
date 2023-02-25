<template>
  <div>
    <form>
      <table border="1">
        <tr align="center">새 환자 추가</tr>
        <tr>
          <td>환자번호 {{}}</td>
          <td></td>
        </tr>
        <tr>
          <td>이름</td>
          <td><input type="text" /></td>
        </tr>
        <tr>
          <td>생년월일</td>
          <td><input type="text" /></td>
        </tr>
        <tr>
          <td>담당과</td>
          <td><input type="text" /></td>
        </tr>
        <tr>
          <td>병동 번호</td>
          <td><input type="text" /></td>
        </tr>
        <tr>
          <td>
          제일 최근 바이탈 사인
          </td>
          <tr>
          <td>
            sbp :
            <td><input type="text" /></td>
          </td>
          </tr>
          <tr>
          <td>
            dbp :
            <td><input type="text" /></td>
          </td>
          </tr>
          <tr>
          <td>
            hr :
            <td><input type="text" /></td>
          </td>
          </tr>
          <tr>
          <td>
            resp :
            <td><input type="text" /></td>
          </td>
          </tr>
          <tr>
          <td>
            temp :
           <td> <input type="text" /></td>
          </td>
          </tr>
        </tr>
      </table>
      <button @click="db_input">저장</button>
      <button class="close">취소</button>
    </form>
  </div>
</template>
<script>
export default {
  components: {},
  data() {
    return {
      p_id: '',
      p_name: '',
      birth_date: '',
      emp_id: ''
    }
  },
  setup() {},
  created() {},
  mounted() {},
  unmounted() {},
  methods: {
    close() {
      
    },
    db_input() {
      
    }
  }
}
</script>
<style>
#header {
  display: none;
}
hr {
  display: none;
}
</style>
