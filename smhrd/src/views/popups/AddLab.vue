<template>
  <div id="wrap-box">
    <h3 style="text-align: center">피검사 데이터 추가</h3>

    <form action="">
      <table>
        <tbody>
          <tr>
            <td>PID</td>
            <td>{{ patients.pid }}</td>
          </tr>
          <tr>
            <td>record_time</td>
            <td>{{ clickTime }}</td>
          </tr>
          <tr>
            <td>EtCO2</td>
            <td>
              <input type="text" v-model="EtCO2" :style="EtCO2 ? 'border-color: green;' : ''" @input="preventInvalidInput($event,'EtCO2')" />
            </td>
          </tr>
          <tr>
            <td>BaseExcess</td>
            <td>
              <input type="text" v-model="BaseExcess" :style="BaseExcess ? 'border-color: green;' : ''" @input="preventInvalidInput($event,'BaseExcess')" />
            </td>
          </tr>
          <tr>
            <td>HCO3</td>
            <td><input type="text" v-model="HCO3" :style="HCO3 ? 'border-color: green;' : ''" @input="preventInvalidInput($event,'HCO3')" /></td>
          </tr>
          <tr>
            <td>FiO2</td>
            <td><input type="text" v-model="FiO2" :style="FiO2 ? 'border-color: green;' : ''" @input="preventInvalidInput($event,'FiO2')" /></td>
          </tr>
          <tr>
            <td>pH</td>
            <td><input type="text" v-model="pH" :style="pH ? 'border-color: green;' : ''" @input="preventInvalidInput($event,'pH')"/></td>
          </tr>
          <tr>
            <td>PaCO2</td>
            <td><input type="text" v-model="PaCO2" :style="PaCO2 ? 'border-color: green;' : ''" @input="preventInvalidInput($event,'PaCO2')" /></td>
          </tr>
          <tr>
            <td>SaO2</td>
            <td><input type="text" v-model="SaO2" :style="SaO2 ? 'border-color: green;' : ''" @input="preventInvalidInput($event,'SaO2')"/></td>
          </tr>
          <tr>
            <td>AST</td>
            <td><input type="text" v-model="AST" :style="AST ? 'border-color: green;' : ''" @input="preventInvalidInput($event,'AST')" /></td>
          </tr>
          <tr>
            <td>BUN</td>
            <td><input type="text" v-model="BUN" :style="BUN ? 'border-color: green;' : ''" @input="preventInvalidInput($event,'BUN')" /></td>
          </tr>
          <tr>
            <td>Alkalinephos</td>
            <td><input type="text" v-model="Alkalinephos" :style="Alkalinephos ? 'border-color: green;' : ''" @input="preventInvalidInput($event,'Alkalinephos')"/></td>
          </tr>
          <tr>
            <td>Calcium</td>
            <td><input type="text" v-model="Calcium" :style="Calcium ? 'border-color: green;' : ''" @input="preventInvalidInput($event,'Calcium')" /></td>
          </tr>
          <tr>
            <td>Chloride</td>
            <td><input type="text" v-model="Chloride" :style="Chloride ? 'border-color: green;' : ''" @input="preventInvalidInput($event,'Chloride')" /></td>
          </tr>
          <tr>
            <td>Creatinine</td>
            <td><input type="text" v-model="Creatinine" :style="Creatinine ? 'border-color: green;' : ''" @input="preventInvalidInput($event,'Creatinine')" /></td>
          </tr>
          <tr>
            <td>Glucose</td>
            <td><input type="text" v-model="Glucose" :style="Glucose ? 'border-color: green;' : ''" @input="preventInvalidInput($event,'Glucose')" /></td>
          </tr>
          <tr>
            <td>Lactate</td>
            <td><input type="text" v-model="Lactate" :style="Lactate ? 'border-color: green;' : ''" @input="preventInvalidInput($event,'Lactate')" /></td>
          </tr>
          <tr>
            <td>Magnesium</td>
            <td><input type="text" v-model="Magnesium" :style="Magnesium ? 'border-color: green;' : ''" @input="preventInvalidInput($event,'Magnesium')"/></td>
          </tr>
          <tr>
            <td>Phosphate</td>
            <td><input type="text" v-model="Phosphate" :style="Phosphate ? 'border-color: green;' : ''" @input="preventInvalidInput($event,'Phosphate')"/></td>
          </tr>
          <tr>
            <td>Potassium</td>
            <td><input type="text" v-model="Potassium" :style="Potassium ? 'border-color: green;' : ''" @input="preventInvalidInput($event,'Potassium')"/></td>
          </tr>
          <tr>
            <td>Bilirubin_total</td>
            <td><input type="text" v-model="Bilirubin_total" :style="Bilirubin_total ? 'border-color: green;' : ''" @input="preventInvalidInput($event,'Bilirubin_total')"/></td>
          </tr>
          <tr>
            <td>Hct</td>
            <td><input type="text" v-model="Hct" :style="Hct ? 'border-color: green;' : ''" @input="preventInvalidInput($event,'Hct')"/></td>
          </tr>
          <tr>
            <td>Hgb</td>
            <td><input type="text" v-model="Hgb" :style="Hgb ? 'border-color: green;' : ''" @input="preventInvalidInput($event,'Hgb')"/></td>
          </tr>
          <tr>
            <td>PTT</td>
            <td><input type="text" v-model="PTT" :style="PTT ? 'border-color: green;' : ''" @input="preventInvalidInput($event,'PTT')"/></td>
          </tr>
          <tr>
            <td>WBC</td>
            <td><input type="text" v-model="WBC" :style="WBC ? 'border-color: green;' : ''" @input="preventInvalidInput($event,'WBC')"/></td>
          </tr>
          <tr>
            <td>Fibrinogen</td>
            <td><input type="text" v-model="Fibrinogen" :style="Fibrinogen ? 'border-color: green;' : ''" @input="preventInvalidInput($event,'Fibrinogen')"/></td>
          </tr>
          <tr>
            <td>Platelets</td>
            <td><input type="text" v-model="Platelets" :style="Platelets ? 'border-color: green;' : ''" @input="preventInvalidInput($event,'Platelets')"/></td>
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
import moment from 'moment'
export default {
  components: {},
  data() {
    return {
      clickTime: moment().format('YYYY-MM-DDTHH:mm:ss'),
      patients: []
    }
  },
  setup() {},
  created() {},
  mounted() {
    axios
      .get('http://127.0.0.1:8002/api/get_latest_all/' + this.$route.params.pid)
      .then((response) => {
        return response.data
      })
      .then((data) => {
        console.log(data[0])
        this.patients = data[0]
        return data
      })
      .then((response) => {
        // this.dbDate = moment(response.birth_date, 'YYYY-MM-DD')
      })
      .catch((error) => {
        console.log(error)
      })
  },
  unmounted() {},
  methods: {
    close() {
      window.close()
    },
      async preventInvalidInput(event, field) {
        const inputVal = event.target.value;
        const valid = /^[\d.]+$/.test(inputVal); // 입력값이 숫자와 소수점으로만 이루어졌는지 확인

        if (valid) {
          // 유효한 값이 입력된 경우, 입력값을 Vue.js 인스턴스의 데이터에 반영
          this[field] = inputVal;
          event.target.style.borderColor = 'green';
        } else {
          // 유효하지 않은 값이 입력된 경우, 이전에 입력된 유효한 값을 사용하여 입력값을 대체
          event.target.value = this[field] || '';
          event.target.style.borderColor = 'red';
        }
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
  width: 150px;
}
input:focus {
  outline: none;
}
</style>
