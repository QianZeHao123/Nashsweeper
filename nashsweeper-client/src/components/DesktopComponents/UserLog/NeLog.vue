<template>
    <div class="w-11/12 h-11/12">
      <!-- <h1 class="border">C-1</h1>
          <div>NEcounter:{{ NEcounter }}</div>
          <div>{{ time.hour }}:{{ time.minute }}:{{ time.second }}</div> -->
  
  
  
      <div class="grid grid-cols-6 p-2">
        <div class="btn btn-sm px-3" v-on:click="onClickNEPre()">Prev</div>
        <div class="col-span-4">
          <div class="text-xl text-center">Nash Equilibrium Review</div>
        </div>
        <div class="btn btn-sm" v-on:click="onClickNENext()">Next</div>
      </div>
  
  
      <div class="grid grid-rows-8">
        <div class="grid grid-cols-8">
          <div class="border" v-bind:class="{ 'chessbtn-blue': NEstep[0] }">&emsp;&emsp;</div>
          <div class="border" v-bind:class="{ 'chessbtn-blue': NEstep[1] }">&emsp;&emsp;</div>
          <div class="border" v-bind:class="{ 'chessbtn-blue': NEstep[2] }">&emsp;&emsp;</div>
          <div class="border" v-bind:class="{ 'chessbtn-blue': NEstep[3] }">&emsp;&emsp;</div>
          <div class="border" v-bind:class="{ 'chessbtn-blue': NEstep[4] }">&emsp;&emsp;</div>
          <div class="border" v-bind:class="{ 'chessbtn-blue': NEstep[5] }">&emsp;&emsp;</div>
          <div class="border" v-bind:class="{ 'chessbtn-blue': NEstep[6] }">&emsp;&emsp;</div>
          <div class="border" v-bind:class="{ 'chessbtn-blue': NEstep[7] }">&emsp;&emsp;</div>
        </div>
  
        <div class="grid grid-cols-8">
          <div class="border" v-bind:class="{ 'chessbtn-blue': NEstep[8] }">&emsp;&emsp;</div>
          <div class="border" v-bind:class="{ 'chessbtn-blue': NEstep[9] }">&emsp;&emsp;</div>
          <div class="border" v-bind:class="{ 'chessbtn-blue': NEstep[10] }">&emsp;&emsp;</div>
          <div class="border" v-bind:class="{ 'chessbtn-blue': NEstep[11] }">&emsp;&emsp;</div>
          <div class="border" v-bind:class="{ 'chessbtn-blue': NEstep[12] }">&emsp;&emsp;</div>
          <div class="border" v-bind:class="{ 'chessbtn-blue': NEstep[13] }">&emsp;&emsp;</div>
          <div class="border" v-bind:class="{ 'chessbtn-blue': NEstep[14] }">&emsp;&emsp;</div>
          <div class="border" v-bind:class="{ 'chessbtn-blue': NEstep[15] }">&emsp;&emsp;</div>
        </div>
  
        <div class="grid grid-cols-8">
          <div class="border" v-bind:class="{ 'chessbtn-blue': NEstep[16] }">&emsp;&emsp;</div>
          <div class="border" v-bind:class="{ 'chessbtn-blue': NEstep[17] }">&emsp;&emsp;</div>
          <div class="border" v-bind:class="{ 'chessbtn-blue': NEstep[18] }">&emsp;&emsp;</div>
          <div class="border" v-bind:class="{ 'chessbtn-blue': NEstep[19] }">&emsp;&emsp;</div>
          <div class="border" v-bind:class="{ 'chessbtn-blue': NEstep[20] }">&emsp;&emsp;</div>
          <div class="border" v-bind:class="{ 'chessbtn-blue': NEstep[21] }">&emsp;&emsp;</div>
          <div class="border" v-bind:class="{ 'chessbtn-blue': NEstep[22] }">&emsp;&emsp;</div>
          <div class="border" v-bind:class="{ 'chessbtn-blue': NEstep[23] }">&emsp;&emsp;</div>
        </div>
  
        <div class="grid grid-cols-8">
          <div class="border" v-bind:class="{ 'chessbtn-blue': NEstep[24] }">&emsp;&emsp;</div>
          <div class="border" v-bind:class="{ 'chessbtn-blue': NEstep[25] }">&emsp;&emsp;</div>
          <div class="border" v-bind:class="{ 'chessbtn-blue': NEstep[26] }">&emsp;&emsp;</div>
          <div class="border" v-bind:class="{ 'chessbtn-blue': NEstep[27] }">&emsp;&emsp;</div>
          <div class="border" v-bind:class="{ 'chessbtn-blue': NEstep[28] }">&emsp;&emsp;</div>
          <div class="border" v-bind:class="{ 'chessbtn-blue': NEstep[29] }">&emsp;&emsp;</div>
          <div class="border" v-bind:class="{ 'chessbtn-blue': NEstep[30] }">&emsp;&emsp;</div>
          <div class="border" v-bind:class="{ 'chessbtn-blue': NEstep[31] }">&emsp;&emsp;</div>
        </div>
  
        <div class="grid grid-cols-8">
          <div class="border" v-bind:class="{ 'chessbtn-blue': NEstep[32] }">&emsp;&emsp;</div>
          <div class="border" v-bind:class="{ 'chessbtn-blue': NEstep[33] }">&emsp;&emsp;</div>
          <div class="border" v-bind:class="{ 'chessbtn-blue': NEstep[34] }">&emsp;&emsp;</div>
          <div class="border" v-bind:class="{ 'chessbtn-blue': NEstep[35] }">&emsp;&emsp;</div>
          <div class="border" v-bind:class="{ 'chessbtn-blue': NEstep[36] }">&emsp;&emsp;</div>
          <div class="border" v-bind:class="{ 'chessbtn-blue': NEstep[37] }">&emsp;&emsp;</div>
          <div class="border" v-bind:class="{ 'chessbtn-blue': NEstep[38] }">&emsp;&emsp;</div>
          <div class="border" v-bind:class="{ 'chessbtn-blue': NEstep[39] }">&emsp;&emsp;</div>
        </div>
  
        <div class="grid grid-cols-8">
          <div class="border" v-bind:class="{ 'chessbtn-blue': NEstep[40] }">&emsp;&emsp;</div>
          <div class="border" v-bind:class="{ 'chessbtn-blue': NEstep[41] }">&emsp;&emsp;</div>
          <div class="border" v-bind:class="{ 'chessbtn-blue': NEstep[42] }">&emsp;&emsp;</div>
          <div class="border" v-bind:class="{ 'chessbtn-blue': NEstep[43] }">&emsp;&emsp;</div>
          <div class="border" v-bind:class="{ 'chessbtn-blue': NEstep[44] }">&emsp;&emsp;</div>
          <div class="border" v-bind:class="{ 'chessbtn-blue': NEstep[45] }">&emsp;&emsp;</div>
          <div class="border" v-bind:class="{ 'chessbtn-blue': NEstep[46] }">&emsp;&emsp;</div>
          <div class="border" v-bind:class="{ 'chessbtn-blue': NEstep[47] }">&emsp;&emsp;</div>
        </div>
  
        <div class="grid grid-cols-8">
          <div class="border" v-bind:class="{ 'chessbtn-blue': NEstep[48] }">&emsp;&emsp;</div>
          <div class="border" v-bind:class="{ 'chessbtn-blue': NEstep[49] }">&emsp;&emsp;</div>
          <div class="border" v-bind:class="{ 'chessbtn-blue': NEstep[50] }">&emsp;&emsp;</div>
          <div class="border" v-bind:class="{ 'chessbtn-blue': NEstep[51] }">&emsp;&emsp;</div>
          <div class="border" v-bind:class="{ 'chessbtn-blue': NEstep[52] }">&emsp;&emsp;</div>
          <div class="border" v-bind:class="{ 'chessbtn-blue': NEstep[53] }">&emsp;&emsp;</div>
          <div class="border" v-bind:class="{ 'chessbtn-blue': NEstep[54] }">&emsp;&emsp;</div>
          <div class="border" v-bind:class="{ 'chessbtn-blue': NEstep[55] }">&emsp;&emsp;</div>
        </div>
  
        <div class="grid grid-cols-8">
          <div class="border" v-bind:class="{ 'chessbtn-blue': NEstep[56] }">&emsp;&emsp;</div>
          <div class="border" v-bind:class="{ 'chessbtn-blue': NEstep[57] }">&emsp;&emsp;</div>
          <div class="border" v-bind:class="{ 'chessbtn-blue': NEstep[58] }">&emsp;&emsp;</div>
          <div class="border" v-bind:class="{ 'chessbtn-blue': NEstep[59] }">&emsp;&emsp;</div>
          <div class="border" v-bind:class="{ 'chessbtn-blue': NEstep[60] }">&emsp;&emsp;</div>
          <div class="border" v-bind:class="{ 'chessbtn-blue': NEstep[61] }">&emsp;&emsp;</div>
          <div class="border" v-bind:class="{ 'chessbtn-blue': NEstep[62] }">&emsp;&emsp;</div>
          <div class="border" v-bind:class="{ 'chessbtn-blue': NEstep[63] }">&emsp;&emsp;</div>
        </div>
      </div>
      <div class="text-base text-center">This is No.{{ NashEquilibrium_num }} Nash Equilibrium</div>
    </div>
  </template>
  
  <script>
  import { NsStore } from "../../../store/index.js";
  import { storeToRefs } from "pinia";
  
  export default {
    name: "PartC_1",
    components: {},
    data() {
      const store = NsStore();
      const { time, NEcounter, NashEquilibrium_num, NEset } = storeToRefs(store);
      // const NEset = [-1, 29, 58];
      // const NEset = [];
      const NEstep = new Array(64).fill(false);
      return {
        time,
        NEcounter,
        NashEquilibrium_num,
        NEset,
        NEstep,
      };
    },
    methods: {
      onClickNEPre: function () {
        if (this.NashEquilibrium_num > 0) {
          this.NashEquilibrium_num -= 1;
          this.NEstep = new Array(64).fill(false);
          this.NEstep[this.NEset[this.NashEquilibrium_num]] = true
        }
      },
      onClickNENext: function () {
        if (this.NashEquilibrium_num < this.NEset.length - 1) {
          this.NashEquilibrium_num += 1;
          this.NEstep = new Array(64).fill(false);
          this.NEstep[this.NEset[this.NashEquilibrium_num]] = true
        }
      }
    },
    mounted() { },
  };
  </script>
  
  <style scoped>
  .chessbtn-blue {
    background-color: #3b82f6;
  }
  </style>
  