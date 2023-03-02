<template>
  <div>
    <form action="">
      <table>
        <tbody>
          <h1 align="center">Lab_Data</h1>
          <tr>
            <td>HCO3</td>
            <td><input type="number" /></td>
          </tr>
          <tr>
            <td>FiO2</td>
            <td><input type="number" /></td>
          </tr>
          <tr>
            <td>pH</td>
            <td><input type="number" /></td>
          </tr>
          <tr>
            <td>PaCO2</td>
            <td><input type="number" /></td>
          </tr>
          <tr>
            <td>SaO2</td>
            <td><input type="number" /></td>
          </tr>
          <tr>
            <td>AST</td>
            <td><input type="number" /></td>
          </tr>
          <tr>
            <td>Alkalinephos</td>
            <td><input type="number" /></td>
          </tr>
          <tr>
            <td>Calcium</td>
            <td><input type="number" /></td>
          </tr>
          <tr>
            <td>Chloride</td>
            <td><input type="number" /></td>
          </tr>
          <tr>
            <td>Creatinine</td>
            <td><input type="number" /></td>
          </tr>
          <tr>
            <td>Bilirubin_direct</td>
            <td><input type="number" /></td>
          </tr>
          <tr>
            <td>Glucose</td>
            <td><input type="number" /></td>
          </tr>
          <tr>
            <td>Lactate</td>
            <td><input type="number" /></td>
          </tr>
          <tr>
            <td>Magnesium</td>
            <td><input type="number" /></td>
          </tr>
          <tr>
            <td>Phosphate</td>
            <td><input type="number" /></td>
          </tr>
          <tr>
            <td>Potassium</td>
            <td><input type="number" /></td>
          </tr>
          <tr>
            <td>Bilirubin_total</td>
            <td><input type="number" /></td>
          </tr>
          <tr>
            <td>Troponinl</td>
            <td><input type="number" /></td>
          </tr>
          <tr>
            <td>Hct</td>
            <td><input type="number" /></td>
          </tr>
          <tr>
            <td>Hgb</td>
            <td><input type="number" /></td>
          </tr>
          <tr>
            <td>PTT</td>
            <td><input type="number" /></td>
          </tr>
          <tr>
            <td>WBC</td>
            <td><input type="number" /></td>
          </tr>
          <tr>
            <td>Fibrinogen</td>
            <td><input type="number" /></td>
          </tr>
          <tr>
            <td>Platelets</td>
            <td><input type="number" /></td>
          </tr>
        </tbody>
      </table>
      <button @click="db_input">저장</button>
      <button class="close">취소</button>
    </form>
  </div>
</template>
<script>
import axios from 'axios'

export default {
  components: {},
  data() {
    return {
      HCO3: '',
      FiO2: '',
      pH: '',
      PaCO2: '',
      SaO2: '',
      AST: '',
      Alkalinephos: '',
      Calcium: '',
      Chloride: '',
      Creatinine: '',
      Bilirubin_direct: '',
      Glucose: '',
      Lactate: '',
      Magnesium: '',
      Phosphate: '',
      Potassium: '',
      Bilirubin_total: '',
      Troponinl: '',
      Hct: '',
      Hgb: '',
      PTT: '',
      WBC: '',
      Fivrinogen: '',
      Platelets: ''
    }
  },
  setup() {},
  created() {},
  mounted() {},
  unmounted() {},
  methods: {
    close() {},
    db_input() {}
  }
}
</script>
<style>
* {
  font-family: 'Noto Sans KR', sans-serif;
}
#header {
  display: none;
}
hr {
  display: none;
}
table {
  border-collapse: collapse;
  width: 100%;
  text-align: center;
  height: 60%;
  padding: 30px;
}
table tr td {
  height: 40px;
  font-weight: bold;
  border-bottom: 1px solid #ced6e0;
}
.btn {
  padding: 3px 7px 3px 7px;
  margin: 20px 20px 10px 20px;
  font-weight: bold;
  border: none;
  background-color: #ced6e0;
  box-shadow: 1px 1px 2px;
  border-radius: 5px;
  cursor: pointer;
}
.btn:active {
  box-shadow: none;
}
#wrap-box {
  text-align: center;
}
input {
  border: 0;
}
input:focus {
  outline: none;
}
</style>
