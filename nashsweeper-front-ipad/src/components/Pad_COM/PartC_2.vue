<template>
  <div class="w-11/12 h-full">
    <!-- <h1 class="border text-xs">C-1</h1>
          <div>NEcounter:{{ NEcounter }}</div>
          <div>{{ time.hour }}:{{ time.minute }}:{{ time.second }}</div> -->
    <!-- <div class="text-lg text-center">Best Response Review </div> -->
    <div class="grid grid-cols-6 p-2">
      <div class="btn btn-xs px-3" v-on:click="onClickBRPre()">Prev</div>
      <div class="col-span-4">
        <div class="text-base text-center">BR Review</div>
      </div>
      <div class="btn btn-xs" v-on:click="onClickBRNext()">Next</div>
    </div>


    <div class="grid grid-rows-8">
      <div class="grid grid-cols-8">
        <div class="border text-xs" v-bind:class="{ 'chessbtn-green': BRstep[0] }">&emsp;&emsp;</div>
        <div class="border text-xs" v-bind:class="{ 'chessbtn-green': BRstep[1] }">&emsp;&emsp;</div>
        <div class="border text-xs" v-bind:class="{ 'chessbtn-green': BRstep[2] }">&emsp;&emsp;</div>
        <div class="border text-xs" v-bind:class="{ 'chessbtn-green': BRstep[3] }">&emsp;&emsp;</div>
        <div class="border text-xs" v-bind:class="{ 'chessbtn-green': BRstep[4] }">&emsp;&emsp;</div>
        <div class="border text-xs" v-bind:class="{ 'chessbtn-green': BRstep[5] }">&emsp;&emsp;</div>
        <div class="border text-xs" v-bind:class="{ 'chessbtn-green': BRstep[6] }">&emsp;&emsp;</div>
        <div class="border text-xs" v-bind:class="{ 'chessbtn-green': BRstep[7] }">&emsp;&emsp;</div>
      </div>

      <div class="grid grid-cols-8">
        <div class="border text-xs" v-bind:class="{ 'chessbtn-green': BRstep[8] }">&emsp;&emsp;</div>
        <div class="border text-xs" v-bind:class="{ 'chessbtn-green': BRstep[9] }">&emsp;&emsp;</div>
        <div class="border text-xs" v-bind:class="{ 'chessbtn-green': BRstep[10] }">&emsp;&emsp;</div>
        <div class="border text-xs" v-bind:class="{ 'chessbtn-green': BRstep[11] }">&emsp;&emsp;</div>
        <div class="border text-xs" v-bind:class="{ 'chessbtn-green': BRstep[12] }">&emsp;&emsp;</div>
        <div class="border text-xs" v-bind:class="{ 'chessbtn-green': BRstep[13] }">&emsp;&emsp;</div>
        <div class="border text-xs" v-bind:class="{ 'chessbtn-green': BRstep[14] }">&emsp;&emsp;</div>
        <div class="border text-xs" v-bind:class="{ 'chessbtn-green': BRstep[15] }">&emsp;&emsp;</div>
      </div>

      <div class="grid grid-cols-8">
        <div class="border text-xs" v-bind:class="{ 'chessbtn-green': BRstep[16] }">&emsp;&emsp;</div>
        <div class="border text-xs" v-bind:class="{ 'chessbtn-green': BRstep[17] }">&emsp;&emsp;</div>
        <div class="border text-xs" v-bind:class="{ 'chessbtn-green': BRstep[18] }">&emsp;&emsp;</div>
        <div class="border text-xs" v-bind:class="{ 'chessbtn-green': BRstep[19] }">&emsp;&emsp;</div>
        <div class="border text-xs" v-bind:class="{ 'chessbtn-green': BRstep[20] }">&emsp;&emsp;</div>
        <div class="border text-xs" v-bind:class="{ 'chessbtn-green': BRstep[21] }">&emsp;&emsp;</div>
        <div class="border text-xs" v-bind:class="{ 'chessbtn-green': BRstep[22] }">&emsp;&emsp;</div>
        <div class="border text-xs" v-bind:class="{ 'chessbtn-green': BRstep[23] }">&emsp;&emsp;</div>
      </div>

      <div class="grid grid-cols-8">
        <div class="border text-xs" v-bind:class="{ 'chessbtn-green': BRstep[24] }">&emsp;&emsp;</div>
        <div class="border text-xs" v-bind:class="{ 'chessbtn-green': BRstep[25] }">&emsp;&emsp;</div>
        <div class="border text-xs" v-bind:class="{ 'chessbtn-green': BRstep[26] }">&emsp;&emsp;</div>
        <div class="border text-xs" v-bind:class="{ 'chessbtn-green': BRstep[27] }">&emsp;&emsp;</div>
        <div class="border text-xs" v-bind:class="{ 'chessbtn-green': BRstep[28] }">&emsp;&emsp;</div>
        <div class="border text-xs" v-bind:class="{ 'chessbtn-green': BRstep[29] }">&emsp;&emsp;</div>
        <div class="border text-xs" v-bind:class="{ 'chessbtn-green': BRstep[30] }">&emsp;&emsp;</div>
        <div class="border text-xs" v-bind:class="{ 'chessbtn-green': BRstep[31] }">&emsp;&emsp;</div>
      </div>

      <div class="grid grid-cols-8">
        <div class="border text-xs" v-bind:class="{ 'chessbtn-green': BRstep[32] }">&emsp;&emsp;</div>
        <div class="border text-xs" v-bind:class="{ 'chessbtn-green': BRstep[33] }">&emsp;&emsp;</div>
        <div class="border text-xs" v-bind:class="{ 'chessbtn-green': BRstep[34] }">&emsp;&emsp;</div>
        <div class="border text-xs" v-bind:class="{ 'chessbtn-green': BRstep[35] }">&emsp;&emsp;</div>
        <div class="border text-xs" v-bind:class="{ 'chessbtn-green': BRstep[36] }">&emsp;&emsp;</div>
        <div class="border text-xs" v-bind:class="{ 'chessbtn-green': BRstep[37] }">&emsp;&emsp;</div>
        <div class="border text-xs" v-bind:class="{ 'chessbtn-green': BRstep[38] }">&emsp;&emsp;</div>
        <div class="border text-xs" v-bind:class="{ 'chessbtn-green': BRstep[39] }">&emsp;&emsp;</div>
      </div>

      <div class="grid grid-cols-8">
        <div class="border text-xs" v-bind:class="{ 'chessbtn-green': BRstep[40] }">&emsp;&emsp;</div>
        <div class="border text-xs" v-bind:class="{ 'chessbtn-green': BRstep[41] }">&emsp;&emsp;</div>
        <div class="border text-xs" v-bind:class="{ 'chessbtn-green': BRstep[42] }">&emsp;&emsp;</div>
        <div class="border text-xs" v-bind:class="{ 'chessbtn-green': BRstep[43] }">&emsp;&emsp;</div>
        <div class="border text-xs" v-bind:class="{ 'chessbtn-green': BRstep[44] }">&emsp;&emsp;</div>
        <div class="border text-xs" v-bind:class="{ 'chessbtn-green': BRstep[45] }">&emsp;&emsp;</div>
        <div class="border text-xs" v-bind:class="{ 'chessbtn-green': BRstep[46] }">&emsp;&emsp;</div>
        <div class="border text-xs" v-bind:class="{ 'chessbtn-green': BRstep[47] }">&emsp;&emsp;</div>
      </div>

      <div class="grid grid-cols-8">
        <div class="border text-xs" v-bind:class="{ 'chessbtn-green': BRstep[48] }">&emsp;&emsp;</div>
        <div class="border text-xs" v-bind:class="{ 'chessbtn-green': BRstep[49] }">&emsp;&emsp;</div>
        <div class="border text-xs" v-bind:class="{ 'chessbtn-green': BRstep[50] }">&emsp;&emsp;</div>
        <div class="border text-xs" v-bind:class="{ 'chessbtn-green': BRstep[51] }">&emsp;&emsp;</div>
        <div class="border text-xs" v-bind:class="{ 'chessbtn-green': BRstep[52] }">&emsp;&emsp;</div>
        <div class="border text-xs" v-bind:class="{ 'chessbtn-green': BRstep[53] }">&emsp;&emsp;</div>
        <div class="border text-xs" v-bind:class="{ 'chessbtn-green': BRstep[54] }">&emsp;&emsp;</div>
        <div class="border text-xs" v-bind:class="{ 'chessbtn-green': BRstep[55] }">&emsp;&emsp;</div>
      </div>

      <div class="grid grid-cols-8">
        <div class="border text-xs" v-bind:class="{ 'chessbtn-green': BRstep[56] }">&emsp;&emsp;</div>
        <div class="border text-xs" v-bind:class="{ 'chessbtn-green': BRstep[57] }">&emsp;&emsp;</div>
        <div class="border text-xs" v-bind:class="{ 'chessbtn-green': BRstep[58] }">&emsp;&emsp;</div>
        <div class="border text-xs" v-bind:class="{ 'chessbtn-green': BRstep[59] }">&emsp;&emsp;</div>
        <div class="border text-xs" v-bind:class="{ 'chessbtn-green': BRstep[60] }">&emsp;&emsp;</div>
        <div class="border text-xs" v-bind:class="{ 'chessbtn-green': BRstep[61] }">&emsp;&emsp;</div>
        <div class="border text-xs" v-bind:class="{ 'chessbtn-green': BRstep[62] }">&emsp;&emsp;</div>
        <div class="border text-xs" v-bind:class="{ 'chessbtn-green': BRstep[63] }">&emsp;&emsp;</div>
      </div>
    </div>

    <div class="text-sm text-center">This is No.{{ BestResponse_num }} Best Response</div>
  </div>
</template>
  
<script>
import { NsStore } from "../../store/index.js";
import { storeToRefs } from "pinia";

export default {
  name: "PartC_2",
  components: {},
  data() {
    const store = NsStore();
    const { BestResponse_num, BRset } = storeToRefs(store);
    const BRstep = new Array(64).fill(false);
    // const BRset = [-1, 3, 12, 23, 41, 48, 62];
    return {
      BestResponse_num,
      BRstep,
      BRset
    };
  },
  methods: {
    onClickBRPre: function () {
      if (this.BestResponse_num > 0) {
        this.BestResponse_num -= 1;
        this.BRstep = new Array(64).fill(false);
        this.BRstep[this.BRset[this.BestResponse_num]] = true
      }
    },
    onClickBRNext: function () {
      if (this.BestResponse_num < this.BRset.length - 1) {
        this.BestResponse_num += 1;
        this.BRstep = new Array(64).fill(false);
        this.BRstep[this.BRset[this.BestResponse_num]] = true
      }
    }
  },
  mounted() { },
};
</script>
  
<style scoped>
.chessbtn-green {
  background-color: rgba(0, 255, 0, 0.493);
}
</style>
  