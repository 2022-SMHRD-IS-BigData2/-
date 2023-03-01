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
            <td style="width: 13%;">InputTime</td>
            <td style="width: 12%;">PID</td>
            <td style="width: 10%;">Name</td>
            <td style="width: 5%;">Age</td>
            <td style="width: 5%;">Sex</td>
            <td style="width: 5%;">HR</td>
            <td style="width: 5%;">Temp</td>
            <td style="width: 5%;">Resp</td>
            <td style="width: 5%;">SBP</td>
            <td style="width: 5%;">DBP</td>
            <td style="width: 15%;">Sepsis-Score</td>
          </tr>
        </thead>

        <!-- tbody for문 돌리기 10명 -->
        <tbody v-for="(patient, index) in (searchData && searchData.length) ? searchData : patients" :key="index">
          <tr>
            <td><input type="checkbox" style="width: 20px; height: 20px; cursor: pointer;" @click="addOn(index)"/></td>
            <td>{{ patient.input_time }}</td>
            <td>
            <router-link :to="{ name: 'PatientView', params: { pid: patient.pid, date: patient.input_time.slice(0, 10) } }">
          {{ patient.pid }}
            </router-link>
            </td>
            <td>{{ patient.name }}</td>
            <td>{{ patient.age }}</td>
            <td>{{  gender[index] }}</td>
            <td>{{ patient.hr }}</td>
            <td>{{ patient.temp }}</td>
            <td>{{ patient.resp }}</td>
            <td>{{ patient.sbp }}</td>
            <td>{{ patient.dbp }}</td>
            <td>{{ patient.sepsis_percent }}</td>
          </tr>
          <tr v-if="patient.isAddOn">
            <td colspan="13">
              PID <input type="text" readonly v-model="patient.pid" > Name <input type="text" readonly v-model="patient.p_name">   HR <input type="number">   Temp <input type="number">   Resp <input type="number">  SBP <input type="number">   DBP <input type="number">   <button type="submit" id="addbtn" @click="detailAdd"> 추가 </button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <div class="pointer">
    <div class="pagination-container">
      <ul class="pagination">
        <li :class="{disabled: currentPage === 1}">
          <a @click="onchange(1)">〈〈</a>
        </li>
        <li :class="{disabled: currentPage === 1}">
          <a @click="onchange(currentPage - 1)" :style="{ pointerEvents: currentPage === 1 ? 'none' : 'auto', opacity: currentPage === 1 ? 0.5 : 1 }">〈</a>
        </li>
        <li v-for="n in pages" :key="n" :class="{active: n === currentPage}">
          <a @click="onchange(n)">{{ n }}</a>
        </li>
        <li :class="{disabled: currentPage === pageCount}">
          <a @click="onchange(currentPage + 1)" :style="{ pointerEvents: currentPage === pageCount ? 'none' : 'auto', opacity: currentPage === pageCount ? 0.5 : 1 }">〉</a>
        </li>
        <li :class="{disabled: currentPage === pageCount}">
          <a @click="onchange(pageCount)" :style="{cursor: currentPage === pageCount ? 'default' : 'pointer'}">〉〉</a>
        </li>
      </ul>
      <div>
      </div>
      <div class="page-search-container">
        <input type="text" v-model="pageSearchTerm" placeholder="Search page" id="page-src">
        <button @click="goToPage" id="page-btn">Go</button>
      </div>
    </div>
  </div>
  </div>
</template>

<script>
// 아래 페이징 번호 가져와서 구현 https://junhyunny.github.io/spring-boot/vue.js/spring-boot-vue-js-paging-table/
// tbody 환자 10명만 나오게 for문 돌리기 >2페이지 넘어가면 그다음 환자부터
// 환자 추가 버튼 누르고 정보 입력하면 정보 받아와서 반영

import moment from 'moment'
import axios from 'axios'
import { useRouter } from 'vue-router'
export default {
  components: {
  },
  data () {
    return {
      clickTime: moment().format('YYYY-MM-DD HH:mm:ss'),
      isAddOn: false,
      patients: [],
      addOnIndex: -1,
      selectedPatients: [],
      selectedPatient: null,
      count: 0,
      perPage:10,
      currentPage:1,
      page: {
                page: 0,
                limit: 10,
      },
      pages:[],
      searchTerm: '',
      pageSearchTerm: '',
      currentDate: "",
      searchQuery:"",
      searchData: [], // 검색 결과 데이터
      path:""
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
  async created () {
    this.fetchData();
  },
  watch: {
  '$store.state.searchQuery'(newSearchQuery, oldSearchQuery) {
    this.searchQuery=this.$store.state.searchQuery
    if (newSearchQuery !== oldSearchQuery) {
      this.fetchData();
    }
    if (this.searchQuery === "") {
      this.searchQuery = '';
      this.currentPage = 1;
      this.fetchData();
    }
    }
  },
  async mounted() {
  try {
    const response = await axios.get('http://127.0.0.1:8002/api/data');
    this.patients = response.data.data;
    this.count = response.data.count;
    this.page = response.data.page;
  } catch (error) {
    console.log(error);
  }
  },
  unmounted () {},
  methods: {
    reRun() {
      this.clickTime = moment().format('YYYY-MM-DD HH:mm:ss'),
      window.location.reload()
    },
    addOn(index) {
  const patient = this.patients[index];
  if (patient) {
    if (!patient.isAddOn) {
      this.selectedPatient = {}; // 추가 입력 행이 닫힌 경우, 선택한 환자 정보 초기화
    }
    patient.isAddOn = !patient.isAddOn;
    if (patient.isAddOn) {
      this.selectPatient(patient, index);
    }
  }
},
  selectPatient(patient, index) {
    if (!patient) return;
    this.selectedPatient = {
      pid: patient.pid,
      p_name: patient.p_name,
      index: index // 선택된 환자의 인덱스도 함께 저장
    };
  },
  async fetchData() {
    let axiurl = 'http://127.0.0.1:8002/api/data';
    let params = {
      limit: this.perPage,
      page: this.currentPage,
    };
    this.patients = [];
    this.searchData = [];
    
    if (this.searchQuery) { // 검색어가 있으면 url 바꿔줌
      console.log(this.searchQuery,this.$store.state.searchQuery);
      axiurl = 'http://127.0.0.1:8002/api/get_search_data';
      this.path=this.$route.path;
      params = {
        path: this.path,
        search_str: this.searchQuery,
        limit: this.perPage,
        page: this.currentPage,
      };
    }else{
      this.patients = []; // 검색어가 없을 경우, patients 배열 초기화
    }
    const response = await axios.get(axiurl, { params });
    if (this.searchQuery) { // 검색어가 있으면 저장하는 객체 이름 바꿔주고 v-if문으로 구분함
      this.searchData = response.data.data;
      this.count = response.data.count;
      this.page = response.data.page.page;
    } else {
      this.patients = response.data.data;
      this.count = response.data.count;
      this.page = response.data.page.page;

    }
    // 강제 업데이트!
    this.$forceUpdate();
  },
    // 검색어 변경
    onSearch(query) {
      this.searchQuery = query;
      this.currentPage = 1;
      this.fetchData();
    },
    // 페이지 변경
    onchange(page) {
      this.currentPage = page;
      this.fetchData();
    },
    goToPage() {
      if (this.pageSearchTerm === '') return;
      const pageNum = parseInt(this.pageSearchTerm);
      if (!isNaN(pageNum) && pageNum > 0 && pageNum <= this.pageCount) {
        this.currentPage = pageNum;
      }
      this.pageSearchTerm = '';
},
  },
    computed: {
      gender() {
        return this.patients.map(patient => patient.sex === 1 ? 'F' : 'M');
      }, 
      pageCount() {
        const count = this.count;
        const perPage = this.perPage;
        return Math.ceil(count / perPage);
      },
      pages() {
        const pagesToShow = 10;
        const pages = [];
        const halfPagesToShow = Math.floor(pagesToShow / 2);
        let start = this.currentPage - halfPagesToShow;
        if (start < 1) {
          start = 1;
        }
        let end = start + pagesToShow - 1;
        if (end > this.pageCount) {
          end = this.pageCount;
          start = end - pagesToShow + 1;
          if (start < 1) {
            start = 1;
          }
        }
        for (let i = start; i <= end; i++) {
          pages.push(i);
        }
          return pages;
      },
    }
  }


</script>

<style scoped>
*{font-family: 'Noto Sans KR', sans-serif;}
#top-wrap{
  width: 100%;
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
  box-shadow: 1px 1px 2px;
}
.btn:active{
  box-shadow: none;
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
  box-shadow: 1px 1px 2px;
}

#addbtn:active{
  box-shadow: none;
}

input{
  border: 2px solid #dfe6e9;
  margin-right: 10px;
  width: 70px;
}
tbody tr td a{
  text-decoration: none;
  color: black;
}
a:visited { text-decoration: none;
color: black; }
a:hover { text-decoration: none;
  color: black; }
a:focus { text-decoration: none;
  color: black; }
a:hover, a:active { text-decoration: none;
  color: black; }

  /* 페이징처리 출력부 */
  .pagination-frame {
    height: 10%;
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    list-style: none;
    margin: 1vh 0vw 0vh 0vw;
    padding: 0px;

    /* 드래그 막기 */
    -ms-user-select: none;
    -moz-user-select: -moz-none;
    -khtml-user-select: none;
    -webkit-user-select: none;
    user-select: none;
  }
  .pagination-container {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-bottom: 10px;
}

.page-search-container {
  display: flex;
  align-items: center;
}

.page-search-container input[type="text"] {
  margin-right: 5px;
}

.pagination {
  display: flex;
  justify-content: center;
  align-items: center;
  list-style: none;
  margin-top: 30px;
  padding: 0;
}

.pagination li {
  margin-right: 5px;
}

.pagination li a {
  display: inline-block;
  padding: 5px 10px;
  border-radius: 3px;
  text-align: center;
  background-color: #fff;
  border: 1px solid #ddd;
  color: #333;
  cursor: pointer;
  transition: all 0.3s ease;
}

.pagination li.active a {
  background-color: #007bff;
  border-color: #007bff;
  color: #fff;
}

.pagination li.active a:hover {
  background-color: #0062cc;
  border-color: #005cbf;
  color: #fff;
}

.pagination li.disabled a {
  opacity: 0.5;
  cursor: default;
}

#page-src{
  margin-top: 15px;
  width: 80px;
  border: 2px solid #333;
  border-radius: 5px;
}

#page-btn{
  margin-top: 15px;
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
  box-shadow: 1px 1px 2px;
}

#page-btn:active{
  box-shadow: none;
}

</style>
