<template>
  <div>
    <div>
      <div>
        <table>
          <thead>
            <tr>
              <td>PID</td>
              <td></td>
              <td>Name</td>
              <td></td>
              <td>Age</td>
              <td></td>
              <td>Sex</td>
              <td></td>
            </tr>
          </thead>
        </table>
      </div>
      <div>
        <button @click="AddVital">정보추가</button>
        <input type="date">
      </div>
    </div>
    <div></div>
  </div>
</template>
<script>
import { useRouter } from 'vue-router'
export default {
  components: {},
  data () {
    return {
      sampleData: ''
    }
  },
  setup () {
    const router = useRouter()

    const AddVital = () => {
      window.open(router.resolve({ name: 'AddVital' }).href, 'AddVital', 'width=500,height=500')
    }

    return {
      AddVital
    }
  },
  created () {},
  mounted () {},
  unmounted () {},
  methods: {}
}
</script>
