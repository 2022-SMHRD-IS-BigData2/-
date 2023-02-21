<template>
  <div>
    <div>
      <div>
        <button>환자 정보 추가</button>
      </div>
      <div>
        <span>새로고침한 시간</span>
        <button>새로고침</button>
      </div>
    </div>
    <div>
      <table>
        <thead>
          <tr>
            <td>위험환자</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
          </tr>
        </thead>
        <!-- tbody for문 돌리기 10명 -->
        <tbody>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
        </tbody>
      </table>
    </div>
   <div>
    <span><a href="">페이징 번호 1~10</a></span>
   </div>
  </div>
</template>
<script>
export default {
  components: {},
  data () {
    return {
      dialog: false,
      name: '',
      email: ''
    }
  },
  setup () {},
  created () {},
  mounted () {},
  unmounted () {},
  methods: {
    submitForm () {
      // 입력 받은 값 처리
      console.log('이름:', this.name)
      console.log('이메일:', this.email)

      // 팝업창 닫기
      this.dialog = false
    }
  }
}
</script>
