<template>
  <!-- <div>
        <h1 class="border">C-3</h1>
    </div> -->
  <div class="w-11/12 h-11/12">
    <!-- <h1 class="border">C-2</h1> -->
    <div class="grid grid-cols-6 p-2">
      <div class="btn btn-sm px-3" v-on:click="onClickBRPre_right()">Prev</div>
      <div class="col-span-4">
        <div class="text-xl text-center">Player 2 BR Review</div>
      </div>
      <div class="btn btn-sm" v-on:click="onClickBRNext_right()">Next</div>
    </div>

    <div class="grid grid-rows-8">
      <div class="grid grid-cols-8">
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_right[0] }">&emsp;&emsp;</div>
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_right[1] }">&emsp;&emsp;</div>
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_right[2] }">&emsp;&emsp;</div>
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_right[3] }">&emsp;&emsp;</div>
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_right[4] }">&emsp;&emsp;</div>
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_right[5] }">&emsp;&emsp;</div>
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_right[6] }">&emsp;&emsp;</div>
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_right[7] }">&emsp;&emsp;</div>
      </div>

      <div class="grid grid-cols-8">
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_right[8] }">&emsp;&emsp;</div>
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_right[9] }">&emsp;&emsp;</div>
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_right[10] }">&emsp;&emsp;</div>
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_right[11] }">&emsp;&emsp;</div>
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_right[12] }">&emsp;&emsp;</div>
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_right[13] }">&emsp;&emsp;</div>
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_right[14] }">&emsp;&emsp;</div>
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_right[15] }">&emsp;&emsp;</div>
      </div>

      <div class="grid grid-cols-8">
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_right[16] }">&emsp;&emsp;</div>
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_right[17] }">&emsp;&emsp;</div>
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_right[18] }">&emsp;&emsp;</div>
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_right[19] }">&emsp;&emsp;</div>
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_right[20] }">&emsp;&emsp;</div>
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_right[21] }">&emsp;&emsp;</div>
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_right[22] }">&emsp;&emsp;</div>
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_right[23] }">&emsp;&emsp;</div>
      </div>

      <div class="grid grid-cols-8">
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_right[24] }">&emsp;&emsp;</div>
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_right[25] }">&emsp;&emsp;</div>
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_right[26] }">&emsp;&emsp;</div>
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_right[27] }">&emsp;&emsp;</div>
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_right[28] }">&emsp;&emsp;</div>
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_right[29] }">&emsp;&emsp;</div>
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_right[30] }">&emsp;&emsp;</div>
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_right[31] }">&emsp;&emsp;</div>
      </div>

      <div class="grid grid-cols-8">
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_right[32] }">&emsp;&emsp;</div>
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_right[33] }">&emsp;&emsp;</div>
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_right[34] }">&emsp;&emsp;</div>
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_right[35] }">&emsp;&emsp;</div>
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_right[36] }">&emsp;&emsp;</div>
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_right[37] }">&emsp;&emsp;</div>
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_right[38] }">&emsp;&emsp;</div>
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_right[39] }">&emsp;&emsp;</div>
      </div>

      <div class="grid grid-cols-8">
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_right[40] }">&emsp;&emsp;</div>
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_right[41] }">&emsp;&emsp;</div>
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_right[42] }">&emsp;&emsp;</div>
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_right[43] }">&emsp;&emsp;</div>
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_right[44] }">&emsp;&emsp;</div>
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_right[45] }">&emsp;&emsp;</div>
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_right[46] }">&emsp;&emsp;</div>
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_right[47] }">&emsp;&emsp;</div>
      </div>

      <div class="grid grid-cols-8">
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_right[48] }">&emsp;&emsp;</div>
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_right[49] }">&emsp;&emsp;</div>
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_right[50] }">&emsp;&emsp;</div>
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_right[51] }">&emsp;&emsp;</div>
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_right[52] }">&emsp;&emsp;</div>
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_right[53] }">&emsp;&emsp;</div>
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_right[54] }">&emsp;&emsp;</div>
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_right[55] }">&emsp;&emsp;</div>
      </div>

      <div class="grid grid-cols-8">
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_right[56] }">&emsp;&emsp;</div>
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_right[57] }">&emsp;&emsp;</div>
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_right[58] }">&emsp;&emsp;</div>
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_right[59] }">&emsp;&emsp;</div>
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_right[60] }">&emsp;&emsp;</div>
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_right[61] }">&emsp;&emsp;</div>
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_right[62] }">&emsp;&emsp;</div>
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_right[63] }">&emsp;&emsp;</div>
      </div>
    </div>
    <div class="text-base text-center">This is No.{{ BestResponse_num_right }} Best Response</div>
  </div>
</template>

<script>
import { NsStore } from "../store/index.js";
import { storeToRefs } from "pinia";

export default {
  name: "PartC_3",
  components: {},
  data() {
    const store = NsStore();
    const { BestResponse_num_right } = storeToRefs(store);
    const BRstep_right = new Array(64).fill(false);
    const BRset_right = [-1, 0, 10, 20, 37, 45, 50];
    return {
      BestResponse_num_right,
      BRstep_right,
      BRset_right
    }
  },
  methods: {
    onClickBRPre_right: function () {
      if (this.BestResponse_num_right > 0) {
        this.BestResponse_num_right -= 1;
        this.BRstep_right = new Array(64).fill(false);
        this.BRstep_right[this.BRset_right[this.BestResponse_num_right]] = true
      }
    },
    onClickBRNext_right: function () {
      if (this.BestResponse_num_right < this.BRset_right.length - 1) {
        this.BestResponse_num_right += 1;
        this.BRstep_right = new Array(64).fill(false);
        this.BRstep_right[this.BRset_right[this.BestResponse_num_right]] = true
      }
    }
  },
  mounted() { },
}
</script>

<style scoped>
.chessbtn-green {
  background-color: #22c55e;
}
</style>