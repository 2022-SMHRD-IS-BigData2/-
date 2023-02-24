<template>
  <div>
    <div id="top-wrap">
      <div id="addpatient">
        <button @click="AddPatient" class="btn">환자 추가</button>
      </div>
      <div id="rerun">
        <span>{{ clickTime }}</span>
        <button @click="reRun" id="rerun-btn" class="btn" >새로고침</button>
      </div>
    </div>
    <div>
      <table>
        <thead>
          <tr>
            <td style="width: 5%;"></td>
            <td style="width: 10%;">PID</td>
            <td style="width: 10%;">Name</td>
            <td style="width: 5%;">Age</td>
            <td style="width: 5%;">Sex</td>
            <td style="width: 10%;">Department</td>
            <td style="width: 10%;">Ward</td>
            <td style="width: 5%;">HR</td>
            <td style="width: 5%;">Temp</td>
            <td style="width: 5%;">Resp</td>
            <td style="width: 5%;">SBP</td>
            <td style="width: 5%;">DBP</td>
            <td style="width: 10%;">S-Score</td>
          </tr>
        </thead>

        <!-- tbody for문 돌리기 10명 -->
        <tbody>
          <tr>
            <td><input type="checkbox" style="width: 20px; height: 20px; cursor: pointer;" @click="addOn(patient.p_id)" /></td>
            <td>
            <router-link :to="{ name: 'PatientView', params: { pid: patients.p_id } }">
          {{ patients.p_id }}
            </router-link>
            </td>
            <td>00</td>
            <td>00</td>
            <td>00</td>
            <td>00</td>
            <td>00</td>
            <td>00</td>
            <td>00</td>
            <td>00</td>
            <td>00</td>
            <td>00</td>
            <td>00</td>
          </tr>
          <tr class="hide" v-if="isAddOn">
            <td colspan="13">
             PID <input type="text" readonly> Name <input type="text" readonly>   HR <input type="text">   Temp <input type="text">   Resp <input type="text">  SBP <input type="text">   DBP <input type="text">   <button id="addbtn"> 추가 </button>
            </td>
        </tr>
        </tbody>
      </table>
    </div>
    <div class="pointer">
        <!-- <a @click="onPageChange(currentPage - 1)"><i class="fa-solid fa-chevron-left"></i></a>
        <a v-for="(paging, index) in pages" :key="index" @click="onPageChange(paging - 1)" :class="paging - 1 === currentPage ? 'currentPage' : ''">{ { paging } }</a>
        <a @click="onPageChange(currentPage + 1)"><i class="fa-solid fa-chevron-right"></i></a> -->
    </div>
  </div>
</template>

<script>
// 아래 페이징 번호 가져와서 구현 https://junhyunny.github.io/spring-boot/vue.js/spring-boot-vue-js-paging-table/
// tbody 환자 10명만 나오게 for문 돌리기 >2페이지 넘어가면 그다음 환자부터
// 환자 추가 버튼 누르고 정보 입력하면 정보 받아와서 반영
// 체크박스 눌렀을때 빠른정보 입력 기능 추가

import moment from 'moment'
import { useRouter } from 'vue-router'
export default {
  components: {},
  data () {
    return {
      clickTime: moment().format('YYYY-MM-DD HH:mm:ss'),
      isAddOn: false
    }
  },
  setup () {
    const router = useRouter()

    const AddPatient = () => {
      window.open(router.resolve({ name: 'AddPatient' }).href, 'AddPatient', 'width=500,height=500')
    }

    return {
      AddPatient
    }
  },
  created () {},
  mounted () {},
  unmounted () {},
  methods: {
    reRun() {
      this.clickTime = moment().format('YYYY-MM-DD HH:mm:ss'),
      window.location.reload()
    },
    addOn(pid) {
      this.isAddOn = !this.isAddOn;
    }
    }
  }


</script>

<style scoped>
*{font-family: 'Nanum Gothic', sans-serif;}
#top-wrap{
  width: 100vw;
  height: 50px;
}
#addpatient{
  float: left;
  margin-left: 70px;
  margin-top: 10px;
}
#rerun{
  float: right;
  margin-right: 70px;
  margin-top: 10px;

}
#rerun-btn{
  margin-left: 20px;
  margin-right: 20px;
}
.btn{
  border: none;
  background-color: #ced6e0;
  font-weight: bold;
  color: #333;
  padding-top: 10px;
  padding-bottom: 10px;
  padding-right: 20px;
  padding-left: 20px;
  border-radius: 5%;
  cursor: pointer;
}
table{
  width: 100%;
  text-align: center;
   border-collapse : collapse;
   margin-top: 20px;
}
thead{
  background-color: #74b9ff;
  height: 70px;
  font-weight: bold;
}
/* tbody tr:nth-child(2n){
  background-color: #F5FFFF;
} */
tbody tr{
  height: 50px;
  border-bottom: 1px solid #ced6e0;
}
.hide{
  font-weight: 150px;
}

#addbtn{
  border: none;
  background-color: #ced6e0;
  font-weight: bold;
  color: #333;
  cursor: pointer;
  padding-top: 5px;
  padding-bottom: 5px;
  padding-right: 10px;
  padding-left: 10px;
  border-radius: 5%;
}

input{
  border: 2px solid #dfe6e9;
  margin-right: 10px;
  width: 70px;
}
</style>
