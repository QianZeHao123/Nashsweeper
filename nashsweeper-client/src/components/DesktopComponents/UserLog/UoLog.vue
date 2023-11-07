<template>
    <!-- <div>
          <h1 class="border">C-3</h1>
      </div> -->
    <div class="w-11/12 h-11/12">
      <!-- <h1 class="border">C-2</h1> -->
      <div class="grid grid-cols-6 p-2">
        <div class="btn btn-sm px-3" v-on:click="onClickUserPre()">Prev</div>
        <div class="col-span-4">
          <div class="text-xl text-center">User Log Review</div>
        </div>
        <div class="btn btn-sm" v-on:click="onClickUserNext()">Next</div>
      </div>
  
      <div class="grid grid-rows-8">
        <div class="grid grid-cols-8">
          <div class="border" v-bind:class="{ 'chessbtn-brown': Userstep[0] }">&emsp;&emsp;</div>
          <div class="border" v-bind:class="{ 'chessbtn-brown': Userstep[1] }">&emsp;&emsp;</div>
          <div class="border" v-bind:class="{ 'chessbtn-brown': Userstep[2] }">&emsp;&emsp;</div>
          <div class="border" v-bind:class="{ 'chessbtn-brown': Userstep[3] }">&emsp;&emsp;</div>
          <div class="border" v-bind:class="{ 'chessbtn-brown': Userstep[4] }">&emsp;&emsp;</div>
          <div class="border" v-bind:class="{ 'chessbtn-brown': Userstep[5] }">&emsp;&emsp;</div>
          <div class="border" v-bind:class="{ 'chessbtn-brown': Userstep[6] }">&emsp;&emsp;</div>
          <div class="border" v-bind:class="{ 'chessbtn-brown': Userstep[7] }">&emsp;&emsp;</div>
        </div>
  
        <div class="grid grid-cols-8">
          <div class="border" v-bind:class="{ 'chessbtn-brown': Userstep[8] }">&emsp;&emsp;</div>
          <div class="border" v-bind:class="{ 'chessbtn-brown': Userstep[9] }">&emsp;&emsp;</div>
          <div class="border" v-bind:class="{ 'chessbtn-brown': Userstep[10] }">&emsp;&emsp;</div>
          <div class="border" v-bind:class="{ 'chessbtn-brown': Userstep[11] }">&emsp;&emsp;</div>
          <div class="border" v-bind:class="{ 'chessbtn-brown': Userstep[12] }">&emsp;&emsp;</div>
          <div class="border" v-bind:class="{ 'chessbtn-brown': Userstep[13] }">&emsp;&emsp;</div>
          <div class="border" v-bind:class="{ 'chessbtn-brown': Userstep[14] }">&emsp;&emsp;</div>
          <div class="border" v-bind:class="{ 'chessbtn-brown': Userstep[15] }">&emsp;&emsp;</div>
        </div>
  
        <div class="grid grid-cols-8">
          <div class="border" v-bind:class="{ 'chessbtn-brown': Userstep[16] }">&emsp;&emsp;</div>
          <div class="border" v-bind:class="{ 'chessbtn-brown': Userstep[17] }">&emsp;&emsp;</div>
          <div class="border" v-bind:class="{ 'chessbtn-brown': Userstep[18] }">&emsp;&emsp;</div>
          <div class="border" v-bind:class="{ 'chessbtn-brown': Userstep[19] }">&emsp;&emsp;</div>
          <div class="border" v-bind:class="{ 'chessbtn-brown': Userstep[20] }">&emsp;&emsp;</div>
          <div class="border" v-bind:class="{ 'chessbtn-brown': Userstep[21] }">&emsp;&emsp;</div>
          <div class="border" v-bind:class="{ 'chessbtn-brown': Userstep[22] }">&emsp;&emsp;</div>
          <div class="border" v-bind:class="{ 'chessbtn-brown': Userstep[23] }">&emsp;&emsp;</div>
        </div>
  
        <div class="grid grid-cols-8">
          <div class="border" v-bind:class="{ 'chessbtn-brown': Userstep[24] }">&emsp;&emsp;</div>
          <div class="border" v-bind:class="{ 'chessbtn-brown': Userstep[25] }">&emsp;&emsp;</div>
          <div class="border" v-bind:class="{ 'chessbtn-brown': Userstep[26] }">&emsp;&emsp;</div>
          <div class="border" v-bind:class="{ 'chessbtn-brown': Userstep[27] }">&emsp;&emsp;</div>
          <div class="border" v-bind:class="{ 'chessbtn-brown': Userstep[28] }">&emsp;&emsp;</div>
          <div class="border" v-bind:class="{ 'chessbtn-brown': Userstep[29] }">&emsp;&emsp;</div>
          <div class="border" v-bind:class="{ 'chessbtn-brown': Userstep[30] }">&emsp;&emsp;</div>
          <div class="border" v-bind:class="{ 'chessbtn-brown': Userstep[31] }">&emsp;&emsp;</div>
        </div>
  
        <div class="grid grid-cols-8">
          <div class="border" v-bind:class="{ 'chessbtn-brown': Userstep[32] }">&emsp;&emsp;</div>
          <div class="border" v-bind:class="{ 'chessbtn-brown': Userstep[33] }">&emsp;&emsp;</div>
          <div class="border" v-bind:class="{ 'chessbtn-brown': Userstep[34] }">&emsp;&emsp;</div>
          <div class="border" v-bind:class="{ 'chessbtn-brown': Userstep[35] }">&emsp;&emsp;</div>
          <div class="border" v-bind:class="{ 'chessbtn-brown': Userstep[36] }">&emsp;&emsp;</div>
          <div class="border" v-bind:class="{ 'chessbtn-brown': Userstep[37] }">&emsp;&emsp;</div>
          <div class="border" v-bind:class="{ 'chessbtn-brown': Userstep[38] }">&emsp;&emsp;</div>
          <div class="border" v-bind:class="{ 'chessbtn-brown': Userstep[39] }">&emsp;&emsp;</div>
        </div>
  
        <div class="grid grid-cols-8">
          <div class="border" v-bind:class="{ 'chessbtn-brown': Userstep[40] }">&emsp;&emsp;</div>
          <div class="border" v-bind:class="{ 'chessbtn-brown': Userstep[41] }">&emsp;&emsp;</div>
          <div class="border" v-bind:class="{ 'chessbtn-brown': Userstep[42] }">&emsp;&emsp;</div>
          <div class="border" v-bind:class="{ 'chessbtn-brown': Userstep[43] }">&emsp;&emsp;</div>
          <div class="border" v-bind:class="{ 'chessbtn-brown': Userstep[44] }">&emsp;&emsp;</div>
          <div class="border" v-bind:class="{ 'chessbtn-brown': Userstep[45] }">&emsp;&emsp;</div>
          <div class="border" v-bind:class="{ 'chessbtn-brown': Userstep[46] }">&emsp;&emsp;</div>
          <div class="border" v-bind:class="{ 'chessbtn-brown': Userstep[47] }">&emsp;&emsp;</div>
        </div>
  
        <div class="grid grid-cols-8">
          <div class="border" v-bind:class="{ 'chessbtn-brown': Userstep[48] }">&emsp;&emsp;</div>
          <div class="border" v-bind:class="{ 'chessbtn-brown': Userstep[49] }">&emsp;&emsp;</div>
          <div class="border" v-bind:class="{ 'chessbtn-brown': Userstep[50] }">&emsp;&emsp;</div>
          <div class="border" v-bind:class="{ 'chessbtn-brown': Userstep[51] }">&emsp;&emsp;</div>
          <div class="border" v-bind:class="{ 'chessbtn-brown': Userstep[52] }">&emsp;&emsp;</div>
          <div class="border" v-bind:class="{ 'chessbtn-brown': Userstep[53] }">&emsp;&emsp;</div>
          <div class="border" v-bind:class="{ 'chessbtn-brown': Userstep[54] }">&emsp;&emsp;</div>
          <div class="border" v-bind:class="{ 'chessbtn-brown': Userstep[55] }">&emsp;&emsp;</div>
        </div>
  
        <div class="grid grid-cols-8">
          <div class="border" v-bind:class="{ 'chessbtn-brown': Userstep[56] }">&emsp;&emsp;</div>
          <div class="border" v-bind:class="{ 'chessbtn-brown': Userstep[57] }">&emsp;&emsp;</div>
          <div class="border" v-bind:class="{ 'chessbtn-brown': Userstep[58] }">&emsp;&emsp;</div>
          <div class="border" v-bind:class="{ 'chessbtn-brown': Userstep[59] }">&emsp;&emsp;</div>
          <div class="border" v-bind:class="{ 'chessbtn-brown': Userstep[60] }">&emsp;&emsp;</div>
          <div class="border" v-bind:class="{ 'chessbtn-brown': Userstep[61] }">&emsp;&emsp;</div>
          <div class="border" v-bind:class="{ 'chessbtn-brown': Userstep[62] }">&emsp;&emsp;</div>
          <div class="border" v-bind:class="{ 'chessbtn-brown': Userstep[63] }">&emsp;&emsp;</div>
        </div>
      </div>
      <div class="text-base text-center">This is No.{{ User_num }} User Operation</div>
    </div>
  </template>
  
  <script>
  import { NsStore } from "../../../store/index.js";
  import { storeToRefs } from "pinia";
  
  export default {
    name: "UserOperationLog",
    components: {},
    data() {
      const store = NsStore();
      const { Userset, User_num } = storeToRefs(store);
      const Userstep = new Array(64).fill(false);
      // const Userset = [-1, 0, 10, 20, 37, 45, 50];
      return {
        User_num,
        Userstep,
        Userset
      }
    },
    methods: {
      onClickUserPre: function () {
        if (this.User_num > 0) {
          this.User_num -= 1;
          this.Userstep = new Array(64).fill(false);
          this.Userstep[this.Userset[this.User_num]] = true
        }
      },
      onClickUserNext: function () {
        if (this.User_num < this.Userset.length - 1) {
          this.User_num += 1;
          this.Userstep = new Array(64).fill(false);
          this.Userstep[this.Userset[this.User_num]] = true
        }
      }
    },
    mounted() { },
  }
  </script>
  
  <style scoped>
  .chessbtn-brown {
    background-color: #cf731c;
  }
  </style>