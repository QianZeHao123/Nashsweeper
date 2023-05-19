<template>
    <div class="w-11/12 h-full">
      <!-- <h1 class="border text-xs">C-1</h1>
          <div>NEcounter:{{ NEcounter }}</div>
          <div>{{ time.hour }}:{{ time.minute }}:{{ time.second }}</div> -->
      <div class="text-lg text-center">Nash Equilibrium Review</div>
      <div class="grid grid-rows-8">
        <div class="grid grid-cols-8">
          <div class="border text-xs">&emsp;&emsp;</div>
          <div class="border text-xs">&emsp;&emsp;</div>
          <div class="border text-xs">&emsp;&emsp;</div>
          <div class="border text-xs">&emsp;&emsp;</div>
          <div class="border text-xs">&emsp;&emsp;</div>
          <div class="border text-xs">&emsp;&emsp;</div>
          <div class="border text-xs">&emsp;&emsp;</div>
          <div class="border text-xs">&emsp;&emsp;</div>
        </div>
  
        <div class="grid grid-cols-8">
          <div class="border text-xs">&emsp;&emsp;</div>
          <div class="border text-xs">&emsp;&emsp;</div>
          <div class="border text-xs">&emsp;&emsp;</div>
          <div class="border text-xs">&emsp;&emsp;</div>
          <div class="border text-xs">&emsp;&emsp;</div>
          <div class="border text-xs">&emsp;&emsp;</div>
          <div class="border text-xs">&emsp;&emsp;</div>
          <div class="border text-xs">&emsp;&emsp;</div>
        </div>
  
        <div class="grid grid-cols-8">
          <div class="border text-xs">&emsp;&emsp;</div>
          <div class="border text-xs">&emsp;&emsp;</div>
          <div class="border text-xs">&emsp;&emsp;</div>
          <div class="border text-xs">&emsp;&emsp;</div>
          <div class="border text-xs">&emsp;&emsp;</div>
          <div class="border text-xs">&emsp;&emsp;</div>
          <div class="border text-xs">&emsp;&emsp;</div>
          <div class="border text-xs">&emsp;&emsp;</div>
        </div>
  
        <div class="grid grid-cols-8">
          <div class="border text-xs">&emsp;&emsp;</div>
          <div class="border text-xs">&emsp;&emsp;</div>
          <div class="border text-xs">&emsp;&emsp;</div>
          <div class="border text-xs">&emsp;&emsp;</div>
          <div class="border text-xs">&emsp;&emsp;</div>
          <div class="border text-xs ">&emsp;&emsp;</div>
          <div class="border text-xs">&emsp;&emsp;</div>
          <div class="border text-xs">&emsp;&emsp;</div>
        </div>
  
        <div class="grid grid-cols-8">
          <div class="border text-xs">&emsp;&emsp;</div>
          <div class="border text-xs">&emsp;&emsp;</div>
          <div class="border text-xs">&emsp;&emsp;</div>
          <div class="border text-xs">&emsp;&emsp;</div>
          <div class="border text-xs">&emsp;&emsp;</div>
          <div class="border text-xs">&emsp;&emsp;</div>
          <div class="border text-xs">&emsp;&emsp;</div>
          <div class="border text-xs">&emsp;&emsp;</div>
        </div>
  
        <div class="grid grid-cols-8">
          <div class="border text-xs">&emsp;&emsp;</div>
          <div class="border text-xs">&emsp;&emsp;</div>
          <div class="border text-xs">&emsp;&emsp;</div>
          <div class="border text-xs">&emsp;&emsp;</div>
          <div class="border text-xs">&emsp;&emsp;</div>
          <div class="border text-xs">&emsp;&emsp;</div>
          <div class="border text-xs">&emsp;&emsp;</div>
          <div class="border text-xs">&emsp;&emsp;</div>
        </div>
  
        <div class="grid grid-cols-8">
          <div class="border text-xs">&emsp;&emsp;</div>
          <div class="border text-xs">&emsp;&emsp;</div>
          <div class="border text-xs">&emsp;&emsp;</div>
          <div class="border text-xs">&emsp;&emsp;</div>
          <div class="border text-xs">&emsp;&emsp;</div>
          <div class="border text-xs">&emsp;&emsp;</div>
          <div class="border text-xs">&emsp;&emsp;</div>
          <div class="border text-xs">&emsp;&emsp;</div>
        </div>
  
        <div class="grid grid-cols-8">
          <div class="border text-xs">&emsp;&emsp;</div>
          <div class="border text-xs">&emsp;&emsp;</div>
          <div class="border text-xs ">&emsp;&emsp;</div>
          <div class="border text-xs">&emsp;&emsp;</div>
          <div class="border text-xs">&emsp;&emsp;</div>
          <div class="border text-xs">&emsp;&emsp;</div>
          <div class="border text-xs">&emsp;&emsp;</div>
          <div class="border text-xs">&emsp;&emsp;</div>
        </div>
      </div>
      <div class="text-sm text-center">This is Nash Equilibrium {{ NashEquilibrium }}</div>
    </div>
  </template>
  
  <script>
  import { NsStore } from "../../store/index.js";
  import { storeToRefs } from "pinia";
  
  export default {
    name: "PartC_1",
    components: {},
    data() {
      const store = NsStore();
      const { time, NashEquilibrium } = storeToRefs(store);
      // const second = storeToRefs(store.time.second)
      return {
        time,
        NashEquilibrium,
      };
    },
    methods: {},
    mounted() {},
  };
  </script>
  
  <style scoped></style>
  