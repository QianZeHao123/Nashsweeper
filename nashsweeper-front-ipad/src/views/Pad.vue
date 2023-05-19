<template>
  <div class="h-screen border">

    <div class="grid grid-cols-4 border h-full w-full">
      <div class="border h-full">
        <!-- sidebar  -->

        <div class="grid grid-cols-4 gap-1 h-15 p-3">
          <div class="col-span-3 card-title">Nashsweeper</div>
          <button class="col-span-1 btn btn-sm">⇦</button>
        </div>

        <div class="flex justify-center items-center border-4">
          <select class="select w-11/12 max-w-xs">
            <option disabled selected>Select your game types</option>
            <option>Prisoner Dilemma</option>
            <option>Battle of the Sexes</option>
            <option>Zero-Sum</option>
            <option>Random</option>
          </select>
        </div>
        <div class="flex justify-center items-center p-3">
          <div class="grid grid-cols-2 gap-3 h-1/4">
            <div><a class="flex justify-center items-center btn btn-sm p-2"
                href="http://127.0.0.1:5000/UploadPage/uploadfile">Load Data</a></div>
            <div><button class="flex justify-center items-center btn btn-sm p-2">Export Data</button></div>
          </div>
        </div>

        <PartB />
        <PartC />
      </div>


      <div class="col-span-3 border h-full w-full">
        <!-- main part -->
        <div class="grid grid-rows-3 w-full h-full align-middle">
          <div class="flex justify-center items-center row-span-2 h-full">
            <!-- checkerboard -->
            <PadCheckerBoard />
          </div>
          <div class="border h-full w-full">
            <!-- Part C-x -->
            <div class="grid grid-cols-3 h-full w-full">
              <div class="flex justify-center items-center h-full border w-full">
                <PartC_1 />
              </div>
              <div class="flex justify-center items-center h-full border w-full">
                <PartC_2 />
              </div>
              <div class="flex justify-center items-center h-full border w-full">
                <PartC_3 />
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- main part -->
  </div>
</template>

<script>
import PadCheckerBoard from '../components/Pad_COM/PadCheckerBoard.vue'
import PartC_1 from '../components/Pad_COM/PartC_1.vue'
import PartC_2 from '../components/Pad_COM/PartC_2.vue'
import PartC_3 from '../components/Pad_COM/PartC_3.vue'
import PartA from '../components/PartA.vue'
import PartB from '../components/Pad_COM/PartB.vue'
import PartC from '../components/PartC.vue'
export default {
  name: "",
  components: {
    PadCheckerBoard,
    PartC_1, PartC_2, PartC_3,
    PartA, PartB, PartC,
  },
  data() {
    return {}
  },
  methods: {},
  mounted() { },
}
</script>

<style scoped></style>