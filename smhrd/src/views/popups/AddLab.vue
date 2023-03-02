<template>
  <div id="wrap-box">
    <form action="">
      <table>
        <tbody>
          <h3 style="text-align: center">피검사 데이터 추가</h3>
          <tr>
            <td>PID</td>
            <td><input type="text" :value="PID" /></td>
          </tr>
          <tr>
            <td>record_time</td>
            <td><input type="datetime-local" :value="record_time" /></td>
          </tr>
          <tr>
            <td>BaseExcess</td>
            <td>
              <input type="number" step="0.1" :value="BaseExcess" />
            </td>
          </tr>
          <tr>
            <td>HCO3</td>
            <td><input type="number" step="0.1" :value="HCO3" /></td>
          </tr>
          <tr>
            <td>FiO2</td>
            <td><input type="number" step="0.1" :value="FiO2" /></td>
          </tr>
          <tr>
            <td>pH</td>
            <td><input type="number" step="0.1" :value="pH" /></td>
          </tr>
          <tr>
            <td>PaCO2</td>
            <td><input type="number" step="0.1" :value="PaCO2" /></td>
          </tr>
          <tr>
            <td>SaO2</td>
            <td><input type="number" step="0.1" :value="SaO2" /></td>
          </tr>
          <tr>
            <td>AST</td>
            <td><input type="number" step="0.1" :value="AST" /></td>
          </tr>
          <tr>
            <td>Alkalinephos</td>
            <td><input type="number" step="0.1" :value="Alkalinephos" /></td>
          </tr>
          <tr>
            <td>Calcium</td>
            <td><input type="number" step="0.1" :value="Calcium" /></td>
          </tr>
          <tr>
            <td>Chloride</td>
            <td><input type="number" step="0.1" :value="Chloride" /></td>
          </tr>
          <tr>
            <td>Creatinine</td>
            <td><input type="number" step="0.1" :value="Creatinine" /></td>
          </tr>
          <tr>
            <td>Bilirubin_direct</td>
            <td>
              <input type="number" step="0.1" :value="Bilirubin_direct" />
            </td>
          </tr>
          <tr>
            <td>Glucose</td>
            <td><input type="number" step="0.1" :value="Glucose" /></td>
          </tr>
          <tr>
            <td>Lactate</td>
            <td><input type="number" step="0.1" :value="Lactate" /></td>
          </tr>
          <tr>
            <td>Magnesium</td>
            <td><input type="number" step="0.1" :value="Magnesium" /></td>
          </tr>
          <tr>
            <td>Phosphate</td>
            <td><input type="number" step="0.1" :value="Phosphate" /></td>
          </tr>
          <tr>
            <td>Potassium</td>
            <td><input type="number" step="0.1" :value="Potassium" /></td>
          </tr>
          <tr>
            <td>Bilirubin_total</td>
            <td><input type="number" step="0.1" :value="Bilirubin_total" /></td>
          </tr>
          <tr>
            <td>Troponinl</td>
            <td><input type="number" step="0.1" :value="Troponinl" /></td>
          </tr>
          <tr>
            <td>Hct</td>
            <td><input type="number" step="0.1" :value="Hct" /></td>
          </tr>
          <tr>
            <td>Hgb</td>
            <td><input type="number" step="0.1" :value="Hgb" /></td>
          </tr>
          <tr>
            <td>PTT</td>
            <td><input type="number" step="0.1" :value="PTT" /></td>
          </tr>
          <tr>
            <td>WBC</td>
            <td><input type="number" step="0.1" :value="WBC" /></td>
          </tr>
          <tr>
            <td>Fibrinogen</td>
            <td><input type="number" step="0.1" :value="Fibrinogen" /></td>
          </tr>
          <tr>
            <td>Platelets</td>
            <td><input type="number" step="0.1" :value="Platelets" /></td>
          </tr>
        </tbody>
      </table>
      <button type="submit" class="btn" @click="db_input">저장</button>
      <button class="btn" @click="close">취소</button>
    </form>
  </div>
</template>
<script>
import axios from 'axios'

export default {
  components: {},
  data() {
    return {
      PID: '자동입력?',
      record_time: '기록시간',
      BaseExcess: 0.0,
      HCO3: 0.0,
      FiO2: 0.0,
      pH: 0.0,
      PaCO2: 0.0,
      SaO2: 0.0,
      AST: 0.0,
      Alkalinephos: 0.0,
      Calcium: 0.0,
      Chloride: 0.0,
      Creatinine: 0.0,
      Bilirubin_direct: 0.0,
      Glucose: 0.0,
      Lactate: 0.0,
      Magnesium: 0.0,
      Phosphate: 0.0,
      Potassium: 0.0,
      Bilirubin_total: 0.0,
      Troponinl: 0.0,
      Hct: 0.0,
      Hgb: 0.0,
      PTT: 0.0,
      WBC: 0.0,
      Fibrinogen: 0.0,
      Platelets: 0.0
    }
  },
  setup() {},
  created() {},
  mounted() {},
  unmounted() {},
  methods: {
    close() {
      window.close()
    },
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
  height: 20px;
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
  border: 1;
}
input:focus {
  outline: none;
}
</style>
