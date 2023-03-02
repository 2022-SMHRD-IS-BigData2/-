<template>
  <div>
    <div>
      <div>
        <button @click="AddPatient">환자 정보 추가</button>
        <button @click="AddLab">피검사</button>
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
import { useRouter } from 'vue-router'
export default {
  components: {},
  data() {
    return {
      sampleData: ''
    }
  },
  setup() {
    const router = useRouter()

    const AddPatient = () => {
      window.open(
        router.resolve({ name: 'AddPatient' }).href,
        'AddPatient',
        'width=500,height=500'
      )
    }

    const AddLab = () => {
      window.open(
        router.resolve({ name: 'AddLab' }).href,
        'AddLab',
        'width=500,height=500'
      )
    }

    return {
      AddPatient,
      AddLab
    }
  },
  created() {},
  mounted() {},
  unmounted() {},
  methods: {}
}
</script>

<style scoped></style>
