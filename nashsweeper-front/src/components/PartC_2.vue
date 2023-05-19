<template>
  <div class="w-11/12 h-11/12">
    <!-- <h1 class="border">C-2</h1> -->
    <div class="grid grid-cols-6 p-2">
      <div class="btn btn-sm px-3" v-on:click="onClickBRPre_left()">Prev</div>
      <div class="col-span-4">
        <div class="text-xl text-center">Player 1 BR Review</div>
      </div>
      <div class="btn btn-sm" v-on:click="onClickBRNext_left()">Next</div>
    </div>

    <div class="grid grid-rows-8">
      <div class="grid grid-cols-8">
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_left[0] }">&emsp;&emsp;</div>
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_left[1] }">&emsp;&emsp;</div>
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_left[2] }">&emsp;&emsp;</div>
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_left[3] }">&emsp;&emsp;</div>
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_left[4] }">&emsp;&emsp;</div>
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_left[5] }">&emsp;&emsp;</div>
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_left[6] }">&emsp;&emsp;</div>
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_left[7] }">&emsp;&emsp;</div>
      </div>

      <div class="grid grid-cols-8">
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_left[8] }">&emsp;&emsp;</div>
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_left[9] }">&emsp;&emsp;</div>
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_left[10] }">&emsp;&emsp;</div>
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_left[11] }">&emsp;&emsp;</div>
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_left[12] }">&emsp;&emsp;</div>
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_left[13] }">&emsp;&emsp;</div>
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_left[14] }">&emsp;&emsp;</div>
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_left[15] }">&emsp;&emsp;</div>
      </div>

      <div class="grid grid-cols-8">
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_left[16] }">&emsp;&emsp;</div>
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_left[17] }">&emsp;&emsp;</div>
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_left[18] }">&emsp;&emsp;</div>
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_left[19] }">&emsp;&emsp;</div>
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_left[20] }">&emsp;&emsp;</div>
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_left[21] }">&emsp;&emsp;</div>
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_left[22] }">&emsp;&emsp;</div>
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_left[23] }">&emsp;&emsp;</div>
      </div>

      <div class="grid grid-cols-8">
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_left[24] }">&emsp;&emsp;</div>
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_left[25] }">&emsp;&emsp;</div>
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_left[26] }">&emsp;&emsp;</div>
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_left[27] }">&emsp;&emsp;</div>
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_left[28] }">&emsp;&emsp;</div>
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_left[29] }">&emsp;&emsp;</div>
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_left[30] }">&emsp;&emsp;</div>
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_left[31] }">&emsp;&emsp;</div>
      </div>

      <div class="grid grid-cols-8">
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_left[32] }">&emsp;&emsp;</div>
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_left[33] }">&emsp;&emsp;</div>
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_left[34] }">&emsp;&emsp;</div>
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_left[35] }">&emsp;&emsp;</div>
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_left[36] }">&emsp;&emsp;</div>
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_left[37] }">&emsp;&emsp;</div>
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_left[38] }">&emsp;&emsp;</div>
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_left[39] }">&emsp;&emsp;</div>
      </div>

      <div class="grid grid-cols-8">
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_left[40] }">&emsp;&emsp;</div>
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_left[41] }">&emsp;&emsp;</div>
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_left[42] }">&emsp;&emsp;</div>
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_left[43] }">&emsp;&emsp;</div>
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_left[44] }">&emsp;&emsp;</div>
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_left[45] }">&emsp;&emsp;</div>
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_left[46] }">&emsp;&emsp;</div>
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_left[47] }">&emsp;&emsp;</div>
      </div>

      <div class="grid grid-cols-8">
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_left[48] }">&emsp;&emsp;</div>
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_left[49] }">&emsp;&emsp;</div>
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_left[50] }">&emsp;&emsp;</div>
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_left[51] }">&emsp;&emsp;</div>
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_left[52] }">&emsp;&emsp;</div>
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_left[53] }">&emsp;&emsp;</div>
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_left[54] }">&emsp;&emsp;</div>
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_left[55] }">&emsp;&emsp;</div>
      </div>

      <div class="grid grid-cols-8">
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_left[56] }">&emsp;&emsp;</div>
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_left[57] }">&emsp;&emsp;</div>
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_left[58] }">&emsp;&emsp;</div>
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_left[59] }">&emsp;&emsp;</div>
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_left[60] }">&emsp;&emsp;</div>
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_left[61] }">&emsp;&emsp;</div>
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_left[62] }">&emsp;&emsp;</div>
        <div class="border" v-bind:class="{ 'chessbtn-green': BRstep_left[63] }">&emsp;&emsp;</div>
      </div>
    </div>
    <div class="text-base text-center">This is No.{{ BestResponse_num_left }} Best Response</div>


  </div>
</template>

<script>
import { NsStore } from "../store/index.js";
import { storeToRefs } from "pinia";

export default {
  name: "PartC_2",
  components: {},
  data() {
    const store = NsStore();
    const { BestResponse_num_left } = storeToRefs(store);
    const BRstep_left = new Array(64).fill(false);
    const BRset_left = [-1, 3, 12, 23, 41, 48, 62];
    return {
      BestResponse_num_left,
      BRstep_left,
      BRset_left
    };
  },
  methods: {
    onClickBRPre_left: function () {
      if (this.BestResponse_num_left > 0) {
        this.BestResponse_num_left -= 1;
        this.BRstep_left = new Array(64).fill(false);
        this.BRstep_left[this.BRset_left[this.BestResponse_num_left]] = true
      }
    },
    onClickBRNext_left: function () {
      if (this.BestResponse_num_left < this.BRset_left.length - 1) {
        this.BestResponse_num_left += 1;
        this.BRstep_left = new Array(64).fill(false);
        this.BRstep_left[this.BRset_left[this.BestResponse_num_left]] = true
      }
    }
  },
  mounted() { },
};
</script>

<style scoped>
.chessbtn-green {
  background-color: #22c55e;
}
</style>